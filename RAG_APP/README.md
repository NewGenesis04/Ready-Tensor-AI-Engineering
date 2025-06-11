# RAG Chatbot

**RAG Chatbot** is a modular Retrieval-Augmented Generation (RAG) application that combines document search with generative AI to answer user questions based on your own knowledge base. 

---

## Features

- **Document Ingestion:** Upload and process PDF, DOCX, and TXT files.
- **Vector Search:** Uses ChromaDB for fast semantic retrieval of relevant document chunks.
- **LLM Integration:** Answers are generated using Google Generative AI models, grounded in your documents.
- **User Interface:** Includes a Streamlit web UI for interactive chat and document management.

---

## Requirements

- **Python Version:**  
  Python 3.10 or higher is recommended.

- **Operating System:**  
  - Windows, macOS, or Linux (tested on Windows 10/11 and Ubuntu 22.04)
  - Streamlit and all dependencies are cross-platform.

- **Dependencies:**  
  - All required Python packages are listed in `requirements.txt`.  
  - Key dependencies include:
    - streamlit
    - langchain
    - langchain-google-genai
    - chromadb
    - tenacity

- **API Keys:**  
  - You must provide a valid Google Generative AI API key in a `.env` file.

- **Hardware:**  
  - No GPU required. Standard CPU and at least 4GB RAM recommended for smooth operation.

---

**Note:**  
For best results, use a modern version of Python and keep your dependencies up to date.  
If you encounter issues on your OS, please open an issue or pull request.

---

## How to Run
1. **Clone the repository:**
    ```
    git clone --filter=blob:none --no-checkout https://github.com/NewGenesis04/Ready-Tensor-AI-Engineering.git
    cd Ready-Tensor-AI-Engineering

    git sparse-checkout init --cone
    git sparse-checkout set RAG_APP
    ```


2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Set up your environment:**
- Create a `.env` file in the `RAG_APP` directory with your Google API key:
    ```
    GOOGLE_API_KEY=your_google_api_key_here
    ```
4. **Run the Streamlit app:**
    ```
    streamlit run app.py
    ```
5. **Use the app:**
- Upload your US history documents.
- Ask questions in the chat interface.
- Get answers with sources cited from your documents.

---

## Project Structure

- `ui/` – Streamlit frontend and components
- `core/` – RAG logic, prompt templates, and services
- `processing/` – Document loading, splitting, and embedding
- `documents/` – Your source documents can be uploaded here directly or via the UI.
- `chroma_db/` – Vector database (auto-generated)
- `requirements.txt` – Python dependencies

---

## Credits

Developed by Ogie Omorose, Anish Khatiwada, and Alpha Lencho.

---

**Note:** This app is for educational and research purposes. For production use, review security and privacy best practices.