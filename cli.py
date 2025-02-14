import argparse
from src.embedding.pdf_embedder import process_pdf
from src.search.full_text import full_text_search
from src.search.semantic import semantic_search
from src.search.hybrid import hybrid_search
from src.qa.qa_engine import generate_qa_response
from src.utils.file_operations import save_results_to_csv, save_qa_results
from src.config import DEFAULT_OUTPUT_PATH


def main_menu():
    while True:
        print("Welcome to IntelliDoc")
        print("Please choose an option:")
        print("1) Embedding")
        print("2) Search")
        print("3) Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == "1":
            embedding_menu()
        elif choice == "2":
            search_menu()
        elif choice == "3":
            print("Exiting IntelliDoc. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def embedding_menu():
    file_path = input("Enter the file path of the PDF to embed: ")
    file_name = input("Enter a name for this file: ")
    print(f"Embedding process started for file: {file_path} with name: {file_name}")
    # Here you would call the actual embedding function

def search_menu():
    print("Select search type:")
    print("1) Hybrid Search")
    print("2) Full Text Search")
    print("3) Semantic Search")
    print("4) RAG Search")
    
    search_type = input("Enter your choice (1, 2, or 3): ")
    
    if search_type == "1":
        print("Performing Hybrid Search")
        search_type = "hybrid"
        search_text = input("Enter the search text: ")
        document_id = input("Enter the document ID: ")
        output = input("Enter the output directory (or press Enter for default): ")
        results = globals()[f"{search_type}_search"](search_text, int(document_id))
        output_path = output if output else DEFAULT_OUTPUT_PATH
        perform_search(search_type, search_text, document_id, output_path)
    elif search_type == "2":
        print("Performing Full Text Search")
        search_type = "full_text"
        search_text = input("Enter the search text: ")
        document_id = input("Enter the document ID: ")
        output = input("Enter the output directory (or press Enter for default): ")
        results = globals()[f"{search_type}_search"](search_text, int(document_id))
        output_path = output if output else DEFAULT_OUTPUT_PATH
        perform_search(search_type, search_text, document_id, output_path)
    elif search_type == "3":
        print("Performing Semantic Search")
        search_type = "semantic"
        search_text = input("Enter the search text: ")
        document_id = input("Enter the document ID: ")
        output = input("Enter the output directory (or press Enter for default): ")
        results = globals()[f"{search_type}_search"](search_text, int(document_id))
        output_path = output if output else DEFAULT_OUTPUT_PATH
        perform_search(search_type, search_text, document_id, output_path)
    elif search_type == "4":
        print("RAG Search")
        search_type = input("Enter the search type (full_text, semantic, hybrid): ")
        search_text = input("Enter the search text: ")
        document_id = input("Enter the document ID: ")
        output = input("Enter the output directory (or press Enter for default): ")
        question = input("Enter your question for LLM: ")
        model = input("Enter the LLM model (default is gpt-4): ") or "gpt-4"
        llm_response = generate_qa_response(search_type, search_text, int(document_id), question, model)
        print("\nLLM Response:")
        print(llm_response)

        output_path = output if output else DEFAULT_OUTPUT_PATH
        filename = save_qa_results(search_text, document_id, search_type, model, question, 
                                   "Context not saved in file for brevity", llm_response, output_path)
        print(f"\nResults and response saved to {filename}")
    else:
        print("Invalid search type. Returning to main menu.")

    # Here you would call the actual search function based on the type

def perform_search(search_type, search_text, document_id, output):
    results = globals()[f"{search_type}_search"](search_text, int(document_id))
    filename = save_results_to_csv(results, search_type, search_text, document_id, output)
    print(f"Search results saved to {filename}")

main_menu()
