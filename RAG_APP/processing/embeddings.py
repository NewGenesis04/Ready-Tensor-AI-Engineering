from pathlib import Path
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from RAG_APP.processing.doc_processor import load_docs, split_docs
import os
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

CHROMA_PATH = str(Path(__file__).parent.parent / "chroma_db")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")    

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004",
                                          google_api_key=GOOGLE_API_KEY,
                                          task_type="retrieval_document")

DOCUMENTS = load_docs(folder_path = Path(__file__).parent.parent / "documents")
CHUNKS = split_docs(DOCUMENTS)

chroma_db = Chroma.from_documents(
    documents=CHUNKS, 
    embedding=embeddings, 
    persist_directory=CHROMA_PATH, 
    collection_name="chromadb_collection"
)

chroma_db.persist()

def query_db(query: str):
    """
    Queries the Chroma database with the provided query string.
    Returns the results from the database.
    """
    try:
        retriever = chroma_db.as_retriever(search_kwargs={"k": 2})
        results = retriever.invoke(query)
        return results
    except Exception as e:
        print(f"Error querying database: {e}")
        return []
