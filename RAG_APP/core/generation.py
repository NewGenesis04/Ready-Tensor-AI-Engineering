# RAG_APP/core/generation.py

from core.retrieval import get_retriever
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from core.config import GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_API_KEY
)

def system_response(thread_id: str, query: str) -> dict:
    retriever = get_retriever()
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    result = rag_chain.invoke({"query": query})

    sources = [doc.metadata.get("source", "Unknown") for doc in result.get("source_documents", [])]
    
    return {
        "answer": result["result"],
        "sources": sources
    }