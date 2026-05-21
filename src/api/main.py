from fastapi import FastAPI
from pathlib import Path
from src.api.schemas import QueryRequest
from src.pipeline.rag_pipeline import build_pipeline

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

PDF_PATH = BASE_DIR / "data" / "raw" / "sample_pdfs" / "sample.pdf"

retriever, llm = build_pipeline(str(PDF_PATH))


@app.get("/")
def health():
    return {"status":"API running"}


@app.post("/ask")
def ask_question(request: QueryRequest):

    docs = retriever.invoke(request.question)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt=f"""
You are a research assistant.

Use only the context below.

Context:
{context}

Question:
{request.question}

Answer:
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }
