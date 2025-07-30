# vector_store.py

from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get context from FAISS vector store
def get_context(query, index_path="faiss_index"):
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(index_path, embeddings)
    docs = db.similarity_search(query, k=3)
    return [doc.page_content for doc in docs]
