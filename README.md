# AI Research Assistant using RAG

An AI-powered Research Assistant built using Retrieval-Augmented Generation (RAG) that allows users to interact with PDF documents using natural language queries.

Users can upload a document, create embeddings, store information in a vector database, retrieve relevant context, and generate responses grounded in the uploaded content.

This project combines AI engineering concepts with backend APIs and MLOps-oriented project structure.

---

## Project Goal

Traditional LLMs answer questions using pre-trained knowledge and can hallucinate when asked about external documents.

This project solves that problem using a Retrieval-Augmented Generation (RAG) pipeline:

- Extract content from PDF documents
- Split content into manageable chunks
- Convert chunks into embeddings
- Store embeddings in a vector database
- Retrieve relevant context
- Generate document-aware answers

---

## Demo Flow

```text
Upload PDF
     ↓
PDF Loader
     ↓
Text Chunking
     ↓
Embeddings
     ↓
Chroma Vector Database
     ↓
Retriever
     ↓
LLM
     ↓
FastAPI
     ↓
Streamlit UI
```

---

## Features

### Document Processing

- PDF ingestion
- Automatic document loading
- Text extraction

### Retrieval Pipeline

- Recursive text chunking
- Sentence Transformer embeddings
- Chroma vector storage
- Semantic search

### AI Layer

- Retrieval-Augmented Generation (RAG)
- Context-aware question answering
- LLM integration

### Backend

- FastAPI endpoints
- Request validation using Pydantic

### Frontend

- Streamlit user interface

### MLOps Structure

- Docker setup
- Jenkins pipeline
- Kubernetes deployment templates
- GitHub Actions workflow
- Test folder structure

---

## Tech Stack

### AI / ML

- LangChain
- Sentence Transformers
- HuggingFace Embeddings
- OpenAI API
- ChromaDB

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Frontend

- Streamlit

### MLOps

- Docker
- Jenkins
- Kubernetes
- GitHub Actions

### Language

- Python 3.11

---

## Project Structure

```text
ai-research-assistant-rag/

├── data/
│   └── raw/
│
├── notebooks/
│
├── src/
│   ├── ingestion/
│   ├── preprocessing/
│   ├── embeddings/
│   ├── vectorstore/
│   ├── retrieval/
│   ├── llm/
│   ├── pipeline/
│   ├── api/
│   └── config/
│
├── tests/
├── ui/
├── k8s/
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── run.py
└── README.md
```

---

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
   "status":"API running"
}
```

### Ask Questions

```http
POST /ask
```

Request:

```json
{
   "question":"Summarize this document"
}
```

Response:

```json
{
   "answer":"..."
}
```

---

## Installation

Clone repository

```bash
git clone https://github.com/Uppalapati10/AI-Research-Assistant-Rag.git
```

Move into project:

```bash
cd AI-Research-Assistant-Rag
```

Create environment:

```bash
python3.11 -m venv .venv
```

Activate:

Mac/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create:

```text
.env
```

Add:

```env
OPENAI_API_KEY=your_api_key
```

---

## Run Backend

```bash
python run.py
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
streamlit run ui/app.py
```

UI:

```text
http://localhost:8501
```

---

## Current Challenges Solved

During implementation:

- Python environment compatibility issues
- LangChain import migrations
- PDF parsing issues
- Chroma persistence updates
- Git large file cleanup
- Virtual environment exclusion

---

## Future Improvements

- Drag-and-drop PDF upload
- Conversation memory
- Source citations
- Multiple document support
- Authentication
- MLflow integration
- Monitoring dashboard
- Docker deployment
- Kubernetes deployment
- CI/CD pipeline improvements

---

## Author

Nishitha

AI / ML Engineer | Python | RAG | FastAPI | MLOps