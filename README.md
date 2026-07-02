# Document Question Answering Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to upload a PDF document and ask questions about its contents.

The system extracts text from the PDF, generates embeddings for document chunks, retrieves the most relevant information using cosine similarity, and generates answers using a Large Language Model (LLM).

---

## Features

- PDF text extraction
- Text chunking with overlap
- Semantic embeddings generation
- In-memory vector storage
- Similarity search using NumPy
- Top-3 chunk retrieval
- LLM-based answer generation
- Conversation history support (Bonus)

---

## Project Structure

```text
document_qa_assistant/
│
├── main.py
├── pdf_processor.py
├── embedding.py
├── rag.py
├── llm.py
├── requirements.txt
├── .env
└── sample.pdf
```

---

## Project Workflow

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings Generation
 ↓
Similarity Search
 ↓
Top-3 Relevant Chunks
 ↓
LLM
 ↓
Final Answer
```

---

## File Descriptions

### 1. pdf_processor.py

Responsible for:

- Reading the PDF
- Extracting text from all pages
- Returning a single text string

Libraries used:

- pypdf

---

### 2. embedding.py

Responsible for:

- Loading the embedding model
- Generating vector embeddings for document chunks

Embedding model used:

```python
all-MiniLM-L6-v2
```

Libraries used:

- sentence-transformers

---

### 3. rag.py

Responsible for:

- Text chunking
- Cosine similarity calculation
- Retrieving the top-k most relevant chunks

Libraries used:

- NumPy

---

### 4. llm.py

Responsible for:

- Connecting to Gemini API
- Sending retrieved context to the LLM
- Returning generated answers

Libraries used:

- google-generativeai
- python-dotenv

---

### 5. main.py

Responsible for:

- Running the entire pipeline
- Accepting user questions
- Maintaining conversation history
- Displaying answers

---

## Chunking Strategy

The extracted text is divided into:

- Chunk Size: 500 characters
- Overlap: 50 characters

Example:

```text
Chunk 1: Characters 0 - 500
Chunk 2: Characters 450 - 950
Chunk 3: Characters 900 - 1400
```

The overlap helps preserve context between neighboring chunks.

---

## Embedding Generation

Each chunk is converted into a dense vector representation using:

```text
all-MiniLM-L6-v2
```

These vectors capture semantic meaning, allowing the system to perform semantic search instead of simple keyword matching.

---

## Similarity Search

For every user query:

1. Generate query embedding.
2. Compute similarity between query embedding and every chunk embedding.
3. Rank chunks by similarity score.
4. Retrieve the top 3 chunks.

---

## Retrieval Process

```text
User Question
      ↓
Generate Query Embedding
      ↓
Compute Similarity Scores
      ↓
Sort Scores
      ↓
Retrieve Top 3 Chunks
      ↓
Pass Context to LLM
```

---

## Conversation History (Bonus)

The application stores previous user queries and answers and includes them in the prompt to maintain context across multiple questions.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Ayush-kr-007/simple-rag
cd document_qa_assistant
```

### Create Virtual Environment

Windows:

```bash
python -m venv myenv
myenv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Application

```bash
python main.py
```

Provide the path of the PDF:

```text
Enter PDF path:
sample.pdf
```

Ask questions:

```text
Ask a question:
---

## Technologies Used

- Python
- PyPDF
- Sentence Transformers
- NumPy
- Gemini API
- Python Dotenv

---

## Future Improvements

- Streamlit UI
- Persistent vector storage
- Hybrid search (Keyword + Semantic)
- Support for multiple PDFs
- Citation of source chunks
- Reranking of retrieved results

---