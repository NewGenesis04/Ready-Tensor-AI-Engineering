from RAG_APP.processing.embeddings import chroma_db

def get_retriever():
    """
    Returns a retriever object from the Chroma vector store.
    """
    return chroma_db.as_retriever(search_kwargs={"k": 2})
