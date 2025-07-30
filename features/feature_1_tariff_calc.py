# features/feature_1_tariff_calc.py

import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

load_dotenv()

embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

docs = [
    Document(page_content="Tariff rate 5% on cotton shirts."),
    Document(page_content="Medical gloves have a 3% import tariff."),
]
db = FAISS.from_documents(docs, embedding)

def calculate_landed_cost(price: float, rate: float):
    tariff = price * rate
    mpf = price * 0.02  # Merchandise Processing Fee (2%)
    total = price + tariff + mpf
    return {
        "Base Price": round(price, 2),
        "Tariff": round(tariff, 2),
        "MPF (2%)": round(mpf, 2),
        "Total Landed Cost": round(total, 2),
    }
