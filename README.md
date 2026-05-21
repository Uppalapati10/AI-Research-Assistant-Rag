# AI Research Assistant (RAG)

An AI-powered Research Assistant that allows users to upload PDF documents and ask natural language questions about their content.

The project uses Retrieval-Augmented Generation (RAG) to retrieve relevant document context before generating responses.

## Features

- PDF ingestion
- Text chunking
- Embedding generation
- Chroma vector database
- Semantic retrieval
- Question answering
- FastAPI backend
- Streamlit frontend
- Docker support
- Jenkins CI/CD structure
- Kubernetes deployment templates

## Architecture

PDF Upload
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
Vector Database
↓
Retriever
↓
LLM
↓
API
↓
UI

## Tech Stack

### AI/ML
- LangChain
- Sentence Transformers
- OpenAI
- ChromaDB

### Backend
- FastAPI

### Frontend
- Streamlit

### MLOps

- Docker
- Jenkins
- Kubernetes

## Folder Structure

```text
ai-research-assistant-rag/

├── data/
├── notebooks/
├── src/
├── tests/
├── ui/
├── Dockerfile
├── Jenkinsfile
├── requirements.txt