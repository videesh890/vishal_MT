# features/feature_3_material_suggestions.py

import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

load_dotenv()

embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

docs = [
    Document(page_content="100% Cotton → Suggest: 80% Cotton, 20% Polyester | Save $0.12 | Quality: High"),
    Document(page_content="100% Nitrile → Suggest: 70% Nitrile, 30% Latex | Save $0.08 | Quality: Moderate"),
]
db = FAISS.from_documents(docs, embedding)

def suggest_material_alternatives(material: str):
    results = db.similarity_search(material, k=1)
    if not results:
        return []
    parts = results[0].page_content.split("→ Suggest: ")[1].split(" | ")
    return [(parts[0], parts[1].replace("Save ", ""), parts[2].replace("Quality: ", ""))]
