# RAG_APP/core/config.py

from pathlib import Path
from dotenv import load_dotenv
import os

# Load .env file from root
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# ENV VARS
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Paths
BASE_DIR = Path(__file__).parent.parent
DOCUMENTS_PATH = BASE_DIR / "documents"
CHROMA_PATH = BASE_DIR / "chroma_db"

# Vectorstore
CHROMA_COLLECTION_NAME = "chromadb_collection"
