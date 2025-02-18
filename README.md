# IntelliDoc

IntelliDoc is an intermediate-level project designed to demystify Retrieval-Augmented Generation (RAG) and vector search techniques. It serves as a hands-on introduction to building a document processing and querying system, combining full-text, semantic, and hybrid search capabilities with AI-powered question answering. By leveraging PostgreSQL with pgvector for efficient vector storage and similarity search, IntelliDoc offers a practical, scalable approach to implementing RAG concepts.

## Features

- **PDF Text Extraction and Embedding:** Extract text from PDFs and generate embeddings for semantic analysis.
- **Full-Text Search:** Utilize PostgreSQL's full-text search capabilities.
- **Semantic Search:** Implement vector-based semantic search using pgvector.
- **Hybrid Search:** Combine full-text and semantic search for enhanced results.
- **AI-Powered Question Answering:** Leverage OpenAI's GPT models for answering questions based on document content.
- **Command-Line Interface (CLI):** A flexible CLI for various operations.

## Prerequisites

Before setting up IntelliDoc, ensure you have the following:

- **Python 3.8 or higher:** [Download Python](https://www.python.org/downloads/)
- **PostgreSQL 14 or higher:** [Download PostgreSQL](https://www.postgresql.org/download/)
- **pgvector Extension:** Install the pgvector extension in your PostgreSQL database.
- **OpenAI API Key:** Sign up at [OpenAI](https://platform.openai.com/signup) to obtain your API key.

## Installation

Follow these steps to set up IntelliDoc:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/homelabrg/IntelliDoc.git
   cd IntelliDoc
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   Create a `.env` file in the project root with the following content:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   DATABASE_URL=postgresql://user:password@localhost:5432/intellidoc
   ```

   Replace `your_openai_api_key`, `user`, `password`, and `localhost:5432/intellidoc` with your actual OpenAI API key and PostgreSQL credentials.

5. **Set Up PostgreSQL with pgvector:**

   - **Install pgvector Extension:**

     Follow the instructions in the [pgvector GitHub repository](https://github.com/pgvector/pgvector) to install the extension.

   - **Create the Database and Enable pgvector:**

     ```sql
     CREATE DATABASE intellidoc;
     \c intellidoc
     CREATE EXTENSION vector;
     ```

6. **Run Migrations:**

   Use the migration tool of your choice (e.g., Alembic) to set up the database schema. Ensure all necessary tables and indexes are created.

## Usage

With the setup complete, you can start using IntelliDoc:

1. **Ingest Documents:**

   Use the CLI to ingest PDF documents into the system:

   ```bash
   python cli.py ingest --file path/to/your/document.pdf
   ```

   This command extracts text from the PDF, generates embeddings, and stores them in the PostgreSQL database.

2. **Perform Searches:**

   - **Full-Text Search:**

     ```bash
     python cli.py search --type fulltext --query "your search term"
     ```

   - **Semantic Search:**

     ```bash
     python cli.py search --type semantic --query "your search term"
     ```

   - **Hybrid Search:**

     ```bash
     python cli.py search --type hybrid --query "your search term"
     ```

3. **Ask Questions:**

   Utilize the AI-powered question-answering feature:

   ```bash
   python cli.py ask --question "What is the main topic of the document?"
   ```

   This command uses OpenAI's GPT model to provide answers based on the ingested documents.

## Contributing

We welcome contributions from the community. To contribute:

1. **Fork the Repository:** Click the "Fork" button at the top right of the repository page.
2. **Create a New Branch:** Use `git checkout -b your-feature-branch` to create a new branch.
3. **Make Changes:** Implement your feature or fix.
4. **Commit Changes:** Use `git commit -m "Description of your changes"` to commit.
5. **Push to Branch:** Use `git push origin your-feature-branch` to push your changes.
6. **Create a Pull Request:** Navigate to the original repository and click "New Pull Request."

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
