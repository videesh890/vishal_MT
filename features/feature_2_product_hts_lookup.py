# features/feature_2_product_hts_lookup.py

import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

load_dotenv()

embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

docs = [
    Document(page_content="McKesson nitrile gloves: HTS 4015.19.0510"),
    Document(page_content="Cotton shirt: HTS 6109.10.0012"),
]
db = FAISS.from_documents(docs, embedding)

def get_product_hts_info(product: str, company: str = ""):
    query = f"{company} {product}"
    results = db.similarity_search(query, k=1)
    return {
        "product": product,
        "company": company,
        "hts_code": results[0].page_content if results else "Not found"
    }
