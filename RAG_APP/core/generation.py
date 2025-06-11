# RAG_APP/core/generation.py
from RAG_APP.processing.embeddings import chroma_db
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from .config import GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

def get_rag_response(thread_id: str | None, query: str) -> dict:


    prompt = PromptTemplate.from_template("""
    Use the following context to answer the question.

    Context:
    {context}

    Question:
    {query}
    """)

    retriever = chroma_db.as_retriever(search_kwargs={"k": 2})
    parser = StrOutputParser()

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {
            "context": retriever | format_docs,
             "query": RunnablePassthrough()
    }      
        | prompt
        | llm
        | parser
    )

    answer = rag_chain.invoke({"query": query})

    sources = [doc.metadata.get("source", "Unknown") for doc in answer.get("source_documents", [])]
    return {
        "answer": answer,
        "sources": sources,
        "thread_id": thread_id
    }