# main.py

import argparse
from src.embedding.pdf_embedder import process_pdf
from src.search.full_text import full_text_search
from src.search.semantic import semantic_search
from src.search.hybrid import hybrid_search
from src.qa.qa_engine import generate_qa_response
from src.utils.file_operations import save_results_to_csv, save_qa_results
from src.config import DEFAULT_OUTPUT_PATH

def main():
    parser = argparse.ArgumentParser(description="Process a PDF file, perform search, and get LLM responses.")
    parser.add_argument("--embed", nargs=2, metavar=('PDF_PATH', 'FILE_NAME'), help="Embed a PDF file")
    parser.add_argument("--search", nargs=3, metavar=('SEARCH_TYPE', 'SEARCH_TEXT', 'DOCUMENT_ID'), 
                        help="Perform search. SEARCH_TYPE can be 'full_text', 'semantic', or 'hybrid'")
    parser.add_argument("--qa", nargs=4, metavar=('SEARCH_TYPE', 'SEARCH_TEXT', 'DOCUMENT_ID', 'QUESTION'),
                        help="Perform search and get LLM response")
    parser.add_argument("--model", default="gpt-4", help="LLM model to use for QA")
    parser.add_argument("--output", help="Specify output directory for results")
    
    args = parser.parse_args()

    if args.embed:
        pdf_path, file_name = args.embed
        process_pdf(pdf_path, file_name)
        print(f"Processed PDF: {file_name}")

    if args.search:
        search_type, search_text, document_id = args.search
        if search_type in ['full_text', 'semantic', 'hybrid']:
            results = globals()[f"{search_type}_search"](search_text, int(document_id))
            output_path = args.output if args.output else DEFAULT_OUTPUT_PATH
            filename = save_results_to_csv(results, search_type, search_text, document_id, output_path)
            print(f"Search results saved to {filename}")
        else:
            print(f"Invalid search type: {search_type}")

    if args.qa:
        search_type, search_text, document_id, question = args.qa
        llm_response = generate_qa_response(search_type, search_text, int(document_id), question, args.model)
        print("\nLLM Response:")
        print(llm_response)

        output_path = args.output if args.output else DEFAULT_OUTPUT_PATH
        filename = save_qa_results(search_text, document_id, search_type, args.model, question, 
                                   "Context not saved in file for brevity", llm_response, output_path)
        print(f"\nResults and response saved to {filename}")

if __name__ == "__main__":
    main()
