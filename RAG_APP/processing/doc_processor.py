from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document
from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

folder_path = Path(__file__).parent.parent / "documents"

def load_docs(folder_path: str) -> List[Document]:
    """Loads documents from a specified folder and returns a list of Document objects.
    Supports PDF, DOCX, and TXT files."""
    try:
        if not os.path.exists(folder_path):
            print(f"Folder not found: {folder_path}")
            return []
        documents = []
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if filename.endswith('.pdf'):
                loader = PyPDFLoader(file_path)
            elif filename.endswith('.docx'):
                loader = Docx2txtLoader(file_path)
            elif filename.endswith('.txt'):
                loader = TextLoader(file_path, encoding='utf-8')
            else:
                print(f"Unsupported file type: {filename}")
                continue
            documents.extend(loader.load())
        return documents
    except Exception as e:
        print(f"Error loading documents: {e}")
        return []

def split_docs(documents, chunk_size=1000, chunk_overlap=200):
    """
    Splits documents into chunks for embedding.
    """
    try:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        return splitter.split_documents(documents)
    except Exception as e:
        print(f"Error splitting documents: {e}")
        return []
