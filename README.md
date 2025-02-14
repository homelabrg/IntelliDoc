```markdown
# IntelliDoc

Welcome to IntelliDoc, an intermediate-level project designed to demystify Retrieval-Augmented Generation (RAG) and vector search techniques. This project serves as a hands-on introduction to building a document processing and querying system, combining full-text, semantic, and hybrid search capabilities with AI-powered question answering. By leveraging PostgreSQL with pgvector for efficient vector storage and similarity search, IntelliDoc offers a practical, scalable approach to implementing RAG concepts. Whether you're a developer looking to understand RAG, a data scientist exploring vector databases, or an AI enthusiast eager to build your first intelligent document system, IntelliDoc provides a solid foundation. It's more than just a demo—it's a learning journey that bridges the gap between theoretical knowledge and practical implementation, setting you on the path to creating sophisticated AI-driven document analysis tools.

## Features

- PDF text extraction and embedding
- Full-text search using PostgreSQL
- Semantic search using vector embeddings
- Hybrid search combining full-text and semantic search
- AI-powered question answering using OpenAI's GPT models
- Flexible command-line interface for various operations

## Prerequisites

Before you begin with IntelliDoc, ensure you have the following set up:

1. PostgreSQL (version 12 or higher) with pgvector extension installed.
2. Python 3.10 or higher.
3. OpenAI API key for generating embeddings.

### PostgreSQL and pgvector Setup

1. Install PostgreSQL: [PostgreSQL Downloads](https://www.postgresql.org/download/)
2. Install pgvector:
   ```
   CREATE EXTENSION vector;
   ```
Note: You might also plan to use docker to run postgressql with pgvector. Check the docker-compose-pgvector.yml for details.

### Database Schema

IntelliDoc requires two main tables in your PostgreSQL database:

1. `documents` table:
   ```
   CREATE TABLE documents (
       id SERIAL PRIMARY KEY,
       file_name TEXT NOT NULL,
       upload_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
   );
   ```
   This table stores metadata about the uploaded documents.
   - `id`: Unique identifier for each document.
   - `file_name`: Name of the uploaded file.
   - `upload_date`: Timestamp of when the document was uploaded.

2. `embeddings` table:
   ```
   CREATE TABLE embeddings (
       id SERIAL PRIMARY KEY,
       document_id INTEGER REFERENCES documents(id),
       page_number INTEGER NOT NULL,
       content TEXT NOT NULL,
       embedding vector(1536)
   );
   ```
   This table stores the actual content and embeddings of document chunks.
   - `id`: Unique identifier for each embedding.
   - `document_id`: Foreign key referencing the `documents` table.
   - `page_number`: Page number of the chunk in the original document.
   - `content`: Text content of the chunk.
   - `embedding`: Vector representation of the content (1536-dimensional for OpenAI's ada-002 model).

Ensure these tables are created in your database before running IntelliDoc.
```

## Installation

1. Clone this repository:

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Note: Python 3.10 and above is recommended.

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your PostgreSQL database and update the connection details in `src/config.py`.

5. Set your OpenAI API key in `src/config.py` or as an environment variable.

## Usage

### Embedding a PDF

```
python main.py --embed "/path/to/your/pdf/file.pdf" "file_name_to_store.pdf"
```

### Performing a Search

```
python main.py --search <search_type> "your search query" <document_id> --output "/path/to/output/directory"
```
Replace `<search_type>` with either `full_text`, `semantic`, or `hybrid`.

### Question Answering

```
python main.py --qa <search_type> "your search query" <document_id> "your question" --model gpt-4 --output "/path/to/output/directory"
```

## Project Structure

```
IntelliDoc/
├── src/
│   ├── embedding/
│   │   ├── pdf_embedder.py
│   │   └── embeddings.py
│   ├── search/
│   │   ├── full_text.py
│   │   ├── semantic.py
│   │   └── hybrid.py
│   ├── qa/
│   │   └── qa_engine.py
│   ├── utils/
│   │   └── file_operations.py
│   ├── database/
│   │   ├── connection.py
│   │   └── models.py
│   └── config.py
├── main.py
├── requirements.txt
├── docker-compose-pgvector.yml
├── README.md
└── LICENSE
```

## Configuration

Update `src/config.py` with your database credentials and OpenAI API key.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer and License

### Educational Purpose

IntelliDoc is an open-source project developed for educational and demonstration purposes. It is intended to serve as a learning tool for understanding and implementing Retrieval-Augmented Generation (RAG) concepts and vector search techniques. While efforts have been made to ensure the accuracy and functionality of the code, it may not be suitable for production environments without further development and testing.

### No Warranty

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

### Use at Your Own Risk

The use of IntelliDoc in production environments or for processing sensitive or critical data is not recommended without thorough review, testing, and potential modifications to meet specific security and performance requirements. Users implement and use this software at their own risk.

### License

IntelliDoc is released under the MIT License. See the [LICENSE](LICENSE) file for details.

By using IntelliDoc, you acknowledge that you have read this disclaimer and agree to its terms.
