# features/feature_5_hts_lookup.py

import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

load_dotenv()

embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

docs = [
    Document(page_content="cotton shirt: HTS 6109.10.0012"),
    Document(page_content="nitrile gloves: HTS 4015.19.0510"),
    Document(page_content="drill machine: HTS 8467.21.0030"),
]
db = FAISS.from_documents(docs, embedding)

def suggest_hts_code(description: str):
    results = db.similarity_search(description, k=1)
    return {"Suggested HTS Code": results[0].page_content if results else "Not found"}
