# ingest.py
import pandas as pd
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
# Load environment variables (for OpenAI API key)
load_dotenv()
def load_documents_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    documents = []
    for _, row in df.iterrows():
        content = f"""
        Product Name: {row.get('product_name')}
        Brand: {row.get('brand')}
        Material Composition: {row.get('material_composition')}
        HTS Code: {row.get('hts_code')}
        Tariff Rate: {row.get('tariff_rate')}
        Country: {row.get('country')}
        Base Price: {row.get('base_price')}
        """
        documents.append(Document(page_content=content.strip()))
    return documents
def build_faiss_index(documents, save_path="faiss_index"):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(documents, embeddings)
    db.save_local(save_path)
    print(f"✅ FAISS index created and saved to: {save_path}")

if __name__ == "__main__":
    dataset_path = "data/tariff_dataset_10k.csv"  # Make sure this file exists
    docs = load_documents_from_csv(dataset_path)
    build_faiss_index(docs)
