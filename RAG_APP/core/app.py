from fastapi import FastAPI
from pydantic import BaseModel
from core.generation import get_rag_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RAGRequest(BaseModel):
    user_id: str
    thread_id: str
    query: str

@app.post("/rag-response")
def rag_response(payload: RAGRequest):
    response = get_rag_response(
        user_id=payload.user_id,
        thread_id=payload.thread_id,
        query=payload.query
    )
    return response
