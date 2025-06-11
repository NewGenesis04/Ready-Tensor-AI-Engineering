# RAG_APP/core/config.py

from pathlib import Path
from dotenv import load_dotenv
import os

# Load .env file from root
# env_path = Path(__file__).parent.parent / ".env"
load_dotenv()

# ENV VARS
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# Ensure GOOGLE_API_KEY is set
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")

# Paths
BASE_DIR = Path(__file__).parent.parent
DOCUMENTS_PATH = BASE_DIR / "documents"
CHROMA_PATH = BASE_DIR / "chroma_db"

# Vectorstore
CHROMA_COLLECTION_NAME = "chromadb_collection"
