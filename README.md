# IntelliDoc

**IntelliDoc** is an open-source document processing and search engine that enables users to **embed PDF documents, perform full-text and semantic searches, and generate AI-driven responses**. It leverages **PostgreSQL with pgvector** for efficient vector storage and similarity search.

## Features

- **PDF Embedding:** Extract text from PDFs and generate vector embeddings.
- **Full-Text Search:** Perform PostgreSQL-powered full-text search.
- **Semantic Search:** Retrieve similar documents using `pgvector`.
- **Hybrid Search:** Combine full-text and semantic search for optimal results.
- **RAG (Retrieval-Augmented Generation) Search:** Ask questions based on document content using OpenAI’s GPT.
- **Command-Line Interface (CLI):** A user-friendly CLI to interact with the system.

---

## **Database Setup**

IntelliDoc requires a **PostgreSQL database** with the **pgvector** extension enabled. It uses two primary tables: `documents` and `embeddings`.

### **1. Prerequisites**
Ensure you have:
- **PostgreSQL 14+** installed. [Download PostgreSQL](https://www.postgresql.org/download/)
- **pgvector extension** installed. [Install pgvector](https://github.com/pgvector/pgvector)
- **Python 3.8+** installed.
- **Database connection configured** via environment variables.

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

## **CLI Usage Guide**
To start the IntelliDoc CLI, run the following command:

```bash
python cli.py
```

### **Main Menu Options:**
Upon running the CLI, you will see a menu with the following options:

### **1) Embedding PDFs**
- Select this option to **embed a PDF file** into the database.
- You will be prompted to **enter the file path** and **provide a name for the file**.

#### **Example:**
```
Enter the file path of the PDF to embed: path/to/document.pdf
Enter a name for the file: Financial_Report
```

---

### **2) Search Documents**
Select this option to **search the database**. A sub-menu will allow you to choose from the following search types:

#### **Hybrid Search**
- Enter the **search text**.
- Enter the **document ID**.
- Enter the **output directory** (or press **Enter** for the default directory).

#### **Example:**
```
Enter search text: revenue growth in 2023
Enter document ID: 5
Enter output directory: /home/user/output
```

---

#### **Full-Text Search**
- Enter the **search text**.
- Enter the **document ID**.
- Enter the **output directory** (or press **Enter** for the default directory).

#### **Example:**
```
Enter search text: tax benefits
Enter document ID: 10
Enter output directory: ./results
```

---

#### **Semantic Search**
- Enter the **search text**.
- Enter the **document ID**.
- Enter the **output directory** (or press **Enter** for the default directory).

#### **Example:**
```
Enter search text: future AI investments
Enter document ID: 7
Enter output directory: /output
```

---

### **3) RAG (Retrieval-Augmented Generation) Search**
This option performs **AI-powered question-answering** on documents.

- Enter the **search type** (`full_text`, `semantic`, `hybrid`).
- Enter the **search text**.
- Enter the **document ID**.
- Enter the **output directory** (or press **Enter** for the default directory).
- Enter the **question** for the AI model.
- Enter the **language model** to use (`gpt-4` by default).

#### **Example:**
```
Enter search type: semantic
Enter search text: major acquisitions
Enter document ID: 3
Enter output directory: ./answers
Enter your question for the AI model: What companies were acquired in 2023?
Enter the language model to use (default is gpt-4): gpt-4
```

---

### **4) Exit**
Select this option to exit the IntelliDoc CLI.

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

