# src/search/semantic.py

from src.database.connection import connect_to_db
from src.embedding.pdf_embedder import get_embedding

def semantic_search(search_text, document_id):
    query_embedding = get_embedding(search_text)
    
    conn = connect_to_db()
    cursor = conn.cursor()

    query = """
    SELECT e.id, e.page_number, e.content, e.embedding <=> %s::vector AS distance
    FROM embeddings e
    WHERE e.document_id = %s
    ORDER BY distance ASC
    LIMIT 10;
    """
    
    cursor.execute(query, (query_embedding, document_id))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results
