from src.ingestion.pdf_loader import load_pdf
from src.preprocessing.text_chunker import chunk_data
from src.embeddings.embedding_model import load_embedding
from src.vectorstore.chroma_store import create_vector_db
from src.retrieval.retriever import get_retriever
from src.llm.llm_engine import load_llm

def build_pipeline(path):

    docs=load_pdf(path)

    chunks=chunk_data(docs)

    embedding=load_embedding()

    db=create_vector_db(chunks,embedding)

    retriever=get_retriever(db)

    llm=load_llm()

    return retriever,llm