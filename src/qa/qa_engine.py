# src/qa/qa_engine.py

from src.search.full_text import full_text_search
from src.search.semantic import semantic_search
from src.search.hybrid import hybrid_search
from src.config import OPENAI_API_KEY
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)

def get_search_results(search_type, search_text, document_id):
    if search_type == 'full_text':
        return full_text_search(search_text, document_id)
    elif search_type == 'semantic':
        return semantic_search(search_text, document_id)
    elif search_type == 'hybrid':
        return hybrid_search(search_text, document_id)
    else:
        raise ValueError("Invalid search type")

def get_llm_response(context, query, model="gpt-4"):
    prompt = f"Context:\n{context}\n\nQuery: {query}\n\nAnswer:"
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the given context."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

def generate_qa_response(search_type, search_text, document_id, llm_query, model="gpt-4"):
    results = get_search_results(search_type, search_text, document_id)
    context = "\n".join([f"Page {r[1]}: {r[2]}" for r in results])
    return get_llm_response(context, llm_query, model)
