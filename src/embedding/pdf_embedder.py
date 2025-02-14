# src/embedding/pdf_embedder.py

import fitz  # PyMuPDF
import re
from openai import OpenAI
from src.database.connection import connect_to_db
from src.config import OPENAI_API_KEY

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def extract_and_chunk_text(pdf_path, max_tokens=500):
    chunks = []
    try:
        with fitz.open(pdf_path) as pdf:
            for page_num in range(len(pdf)):
                page = pdf[page_num]
                text = page.get_text()
                words = text.split()
                current_chunk = []
                current_token_count = 0

                for word in words:
                    token_count = len(re.findall(r'\w+', word))
                    if current_token_count + token_count > max_tokens:
                        chunks.append((page_num + 1, ' '.join(current_chunk)))
                        current_chunk = [word]
                        current_token_count = token_count
                    else:
                        current_chunk.append(word)
                        current_token_count += token_count

                if current_chunk:
                    chunks.append((page_num + 1, ' '.join(current_chunk)))
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return chunks

def get_embedding(text):
    response = client.embeddings.create(input=text, model="text-embedding-ada-002")
    return response.data[0].embedding

def process_pdf(pdf_path, file_name):
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        # Insert document into documents table
        cursor.execute("INSERT INTO documents (file_name) VALUES (%s) RETURNING id", (file_name,))
        document_id = cursor.fetchone()[0]

        chunks = extract_and_chunk_text(pdf_path)

        for page_num, content in chunks:
            embedding = get_embedding(content)
            tokens = len(content.split())
            
            cursor.execute("""
                INSERT INTO embeddings (document_id, page_number, content, tokens, embedding)
                VALUES (%s, %s, %s, %s, %s)
            """, (document_id, page_num, content, tokens, embedding))

        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error processing PDF: {e}")
    finally:
        cursor.close()
        conn.close()

# Example usage can be moved to main.py or a separate script
