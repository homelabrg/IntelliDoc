# src/search/hybrid.py

from src.database.connection import connect_to_db
from src.embedding.pdf_embedder import get_embedding

def hybrid_search(search_text, document_id, n=10):
    conn = connect_to_db()
    if not conn:
        return []

    cursor = conn.cursor()
    query_embedding = get_embedding(search_text)

    query = """
    WITH full_text_results AS (
        SELECT id, page_number, content, 
               ts_rank(to_tsvector('english', content), plainto_tsquery('english', %s)) AS rank,
               0 AS distance
        FROM embeddings
        WHERE document_id = %s AND to_tsvector('english', content) @@ plainto_tsquery('english', %s)
    ),
    vector_results AS (
        SELECT id, page_number, content,
               0 AS rank,
               embedding <=> %s::vector AS distance
        FROM embeddings
        WHERE document_id = %s
    )
    SELECT * FROM (
        SELECT * FROM full_text_results
        UNION ALL
        SELECT * FROM vector_results
    ) combined_results
    ORDER BY (rank + (1 - distance)) DESC
    LIMIT %s;
    """

    cursor.execute(query, (search_text, document_id, search_text, query_embedding, document_id, n))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results
