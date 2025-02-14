# src/utils/file_operations.py

import csv
import os
from datetime import datetime
from src.config import DEFAULT_OUTPUT_PATH

def save_results_to_csv(results, search_type, search_text, document_id, output_path=None):
    if output_path is None:
        output_path = DEFAULT_OUTPUT_PATH

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{search_type}_search_{search_text.replace(' ', '_').lower()}_doc{document_id}_{timestamp}.csv"
    full_path = os.path.join(output_path, filename)

    os.makedirs(output_path, exist_ok=True)

    with open(full_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Page Number", "Content", "Rank", "Distance"])
        for row in results:
            writer.writerow(row)

    return full_path

def save_qa_results(search_text, document_id, search_type, model, llm_query, context, llm_response, output_path=None):
    if output_path is None:
        output_path = DEFAULT_OUTPUT_PATH

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{search_type}_search_llm_response_{timestamp}.txt"
    full_path = os.path.join(output_path, filename)

    os.makedirs(output_path, exist_ok=True)

    with open(full_path, 'w') as f:
        f.write(f"Search Query: {search_text}\n")
        f.write(f"Document ID: {document_id}\n")
        f.write(f"Search Type: {search_type}\n")
        f.write(f"LLM Model: {model}\n")
        f.write(f"LLM Query: {llm_query}\n\n")
        f.write("Context:\n")
        f.write(context)
        f.write("\n\nLLM Response:\n")
        f.write(llm_response)

    return full_path