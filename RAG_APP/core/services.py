import os
import json
from pathlib import Path
from RAG_APP.core.generation import get_rag_response
from RAG_APP.processing.embeddings import chroma_db, get_embeddings
from RAG_APP.processing.doc_processor import load_docs, split_docs

CHAT_HISTORY_DIR = Path(__file__).parent.parent / "ui" / "chat_histories"
UPLOADS_DIR = Path(__file__).parent.parent / "ui" / "uploads"
DOCUMENTS_DIR = Path(__file__).parent.parent / "documents"


def generate_answer(query, user_id, thread_id):
    """
    Generate an answer using the RAG pipeline.
    """
    return get_rag_response(user_id, thread_id, query)


def process_and_index_files(files, user_id):
    """
    Process and add new documents to the vector DB after upload.
    """
    user_upload_dir = UPLOADS_DIR / str(user_id)
    user_upload_dir.mkdir(parents=True, exist_ok=True)
    for file in files:
        file_path = user_upload_dir / file.name
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
    # Load and split new docs, then add to vector DB
    new_docs = load_docs(str(user_upload_dir))
    if new_docs:
        chunks = split_docs(new_docs)
        chroma_db.add_documents(chunks)
        chroma_db.persist()


def save_chat_history(session_id, history):
    CHAT_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    with open(CHAT_HISTORY_DIR / f"{session_id}.json", "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def load_chat_history(session_id):
    try:
        with open(CHAT_HISTORY_DIR / f"{session_id}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def list_threads():
    if not CHAT_HISTORY_DIR.exists():
        return []
    return [f.stem for f in CHAT_HISTORY_DIR.glob("*.json")]