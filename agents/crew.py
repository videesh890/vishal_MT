from crewai import Crew, Task, Agent
from agents.agents import hts_classifier, tariff_evaluator, material_analyzer

def run_tariff_analysis_scenario(query: str):
    task1 = Task(
        name="HTS Classification",
        description=f"Classify the HTS code and material for: {query}",
        agent=hts_classifier,
        expected_output="HTS code and material composition"
    )

    task2 = Task(
        name="Tariff Rate Evaluation",
        description=f"Evaluate tariff rate for: {query}",
        agent=tariff_evaluator,
        expected_output="Tariff rate with justification"
    )

    task3 = Task(
        name="Material Optimization",
        description=f"Suggest better material mix to reduce tariff: {query}",
        agent=material_analyzer,
        expected_output="New material composition and savings"
    )

    crew = Crew(
        agents=[hts_classifier, tariff_evaluator, material_analyzer],
        tasks=[task1, task2, task3],
        verbose=True
    )

    output = crew.kickoff()
    return output.final_outputs
