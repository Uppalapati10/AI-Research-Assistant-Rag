from langchain_community.vectorstores import Chroma

def create_vector_db(chunks,embedding):

    db=Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="vector_db"
    )

    db.persist()

    return db