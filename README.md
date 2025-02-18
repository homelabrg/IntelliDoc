
# IntelliDoc

**IntelliDoc** is an open-source document processing and search engine that combines full-text, semantic, and hybrid search capabilities with AI-powered question answering. It leverages **PostgreSQL with pgvector** for efficient vector storage and similarity search.

## Features

- **PDF Text Extraction and Embedding:** Extract text from PDFs and generate embeddings.
- **Full-Text Search:** Utilize PostgreSQL's full-text search capabilities.
- **Semantic Search:** Implement vector-based semantic search using `pgvector`.
- **Hybrid Search:** Combine full-text and semantic search for enhanced results.
- **AI-Powered Question Answering:** Use OpenAI's GPT models for answering questions based on document content.
- **Command-Line Interface (CLI):** A flexible CLI for various operations.

---

## **Database Setup**

IntelliDoc requires a **PostgreSQL database** with the **pgvector** extension enabled. It uses two primary tables: `documents` and `embeddings`.

### **1. Prerequisites**
Ensure you have:
- **PostgreSQL 14+** installed. [Download PostgreSQL](https://www.postgresql.org/download/)
- **pgvector extension** installed. [Install pgvector](https://github.com/pgvector/pgvector)
- **Python 3.8+** installed.
- **Database connection configured** via environment variables.

_**You can alternatively run the PostgreSQL with pgvector via the provided docker-compose file in the repo docker-compose-pgvector.yml**_

### **2. Database Schema**
IntelliDoc uses the following table structures:

#### **`documents` Table**
Stores document metadata.

| Column        | Type      | Description                                    |
|--------------|----------|------------------------------------------------|
| `id`         | `bigserial` | Unique document identifier (Primary Key).    |
| `file_name`  | `text`      | Name of the uploaded file.                   |
| `upload_date` | `timestamp` | Timestamp when the file was uploaded (defaults to current time). |

#### **`embeddings` Table**
Stores embeddings for document pages.

| Column       | Type        | Description                                    |
|-------------|------------|------------------------------------------------|
| `id`        | `bigserial` | Unique embedding identifier (Primary Key).    |
| `document_id` | `bigint`  | Foreign key referencing `documents(id)`.      |
| `page_number` | `integer`  | Page number of the document.                  |
| `page_title` | `text`     | Title of the page (if available).             |
| `entities`   | `jsonb`    | Extracted named entities from the page.       |
| `content`    | `text`     | Text content of the page.                     |
| `tokens`     | `integer`  | Token count in the page.                      |
| `embedding`  | `vector(1536)` | Vector representation of the page's content. |

### **3. Setting Up the Database**
1. **Start PostgreSQL** and ensure the `pgvector` extension is enabled.
   
   ```sql
   CREATE EXTENSION vector;
   ```

2. **Create the Database and Tables**
   You can create the tables manually using SQL commands or run the provided Python script.

   **Method 1: Manual SQL Execution**
   Run the following SQL commands in your PostgreSQL database:

   ```sql
   CREATE TABLE IF NOT EXISTS documents (
       id bigserial primary key,
       file_name text not null,
       upload_date timestamp not null default current_timestamp
   );

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
   ```

   **Method 2: Using Python**
   Run the following Python script to create the required tables:

   ```bash
   python -c "from src.database.connection import create_tables; create_tables()"
   ```

3. **Verify Table Creation**
   You can check if the tables were created successfully:

   ```sql
   SELECT * FROM documents;
   SELECT * FROM embeddings;
   ```

---

## **Installation Guide**
### **1. Clone the Repository**
```bash
git clone https://github.com/homelabrg/IntelliDoc.git
cd IntelliDoc
```

### **2. Set Up a Virtual Environment**
```bash
python3 -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure Environment Variables**
Create a `.env` file in the project root with the following content:

```env
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=postgresql://user:password@localhost:5432/intellidoc
```
Replace `your_openai_api_key`, `user`, `password`, and `localhost:5432/intellidoc` with actual values.

---

## **Usage Guide**
### **Ingest Documents**
Extract text from a PDF and store it in the database:
```bash
python cli.py ingest --file path/to/document.pdf
```

### **Perform Searches**
- **Full-Text Search**
  ```bash
  python cli.py search --type fulltext --query "search term"
  ```
- **Semantic Search**
  ```bash
  python cli.py search --type semantic --query "search term"
  ```
- **Hybrid Search**
  ```bash
  python cli.py search --type hybrid --query "search term"
  ```

### **Ask Questions**
Query the AI-powered system:
```bash
python cli.py ask --question "What is the main topic of the document?"
```

---

## **Contributing**
We welcome contributions from the community! To contribute:
1. **Fork the Repository** – Click the "Fork" button at the top.
2. **Create a Branch** – `git checkout -b feature-branch`
3. **Make Changes** – Implement your feature or fix.
4. **Commit and Push** – `git commit -m "Added feature"` → `git push origin feature-branch`
5. **Submit a Pull Request** – Open a PR on GitHub.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

 

