from crewai import Agent
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
hts_classifier = Agent(
    role="HTS Classification Expert",
    goal="Identify product, brand, country, material, and HTS code",
    backstory="Customs classification expert",
    llm=llm,
    return_as_function=True,
    verbose=True
)
tariff_calculator = Agent(
    role="Tariff Analyst",
    goal="Compute tariff rate and landed cost with justification",
    backstory="Trade compliance specialist",
    llm=llm,
    return_as_function=True,
    verbose=True
)
material_optimizer = Agent(
    role="Material Strategist",
    goal="Suggest alternative material composition to reduce tariffs",
    backstory="Materials and cost optimization expert",
    llm=llm,
    return_as_function=True,
    verbose=True
)

tariff_evaluator = Agent(
    role="Tariff Cost Evaluator",
    goal="Calculate total tariff cost and landed cost based on HTS and country of origin",
    backstory="Expert in tariff calculation and international trade cost analysis. Evaluates final landed cost using HTS code and MPF.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)
material_analyzer = Agent(
    role="Material Analyzer",
    goal="Analyze the material composition of products and suggest optimizations",
    backstory=(
        "You are a material science expert with deep knowledge of manufacturing materials. "
        "You assess current product compositions and recommend substitutes that maintain performance "
        "while potentially reducing tariffs or costs."
    ),
    verbose=True,
    allow_delegation=False,
    llm=ChatOpenAI(model="gpt-4", temperature=0.3),
)