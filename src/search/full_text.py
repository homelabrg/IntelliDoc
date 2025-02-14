# src/search/full_text.py

from src.database.connection import connect_to_db

def full_text_search(search_text, document_id):
    conn = connect_to_db()
    if not conn:
        return []

    cursor = conn.cursor()

    query = """
    SELECT id, page_number, content
    FROM embeddings
    WHERE document_id = %s AND to_tsvector('english', content) @@ websearch_to_tsquery('english', %s)
    ORDER BY ts_rank(to_tsvector('english', content), websearch_to_tsquery('english', %s)) DESC
    LIMIT 10;
    """

    cursor.execute(query, (document_id, search_text, search_text))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results
