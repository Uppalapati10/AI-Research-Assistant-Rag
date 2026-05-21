from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config.settings import *

def chunk_data(documents):

    splitter=RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks=splitter.split_documents(documents)

    return chunks