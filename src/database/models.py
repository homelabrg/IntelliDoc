from src.database.connection import connect_to_db

def create_tables():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id bigserial primary key,
                file_name text not null,
                upload_date timestamp not null default current_timestamp
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS embeddings (
                id bigserial primary key,
                document_id bigint references documents(id),
                page_number integer not null,
                page_title text,
                entities jsonb,
                content text not null,
                tokens integer not null,
                embedding vector(1536)
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
