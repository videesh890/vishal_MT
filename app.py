import streamlit as st
from features import (
    feature_1_tariff_calc as f1,
    feature_2_product_hts_lookup as f2,
    feature_3_material_suggestions as f3,
    feature_4_what_if_simulation as f4,
    feature_5_hts_lookup as f5
)
from agents.crew import run_tariff_analysis_scenario

# --- App UI ---
st.set_page_config(page_title="Tariff Chatbot", layout="wide")
st.title("Tariff Management Chatbot")

tabs = st.tabs([
    "Tariff Calc",
    "Product → HTS",
    "Material Suggestion",
    "What-If",
    "HTS Lookup",
    "Scenario Chatbot"
])

# --- Tab 0: Tariff Calculation ---
with tabs[0]:
    st.subheader("Tariff Impact Calculation")
    price = st.number_input("Enter Base Price ($)", 0.0)
    rate = st.number_input("Enter Tariff Rate (%)", 0.0)
    if st.button("Calculate Tariff"):
        result = f1.calculate_landed_cost(price, rate / 100)
        st.json(result)

# --- Tab 1: Product to HTS ---
with tabs[1]:
    st.subheader("Product HTS Classification")
    product = st.text_input("Product Name")
    company = st.text_input("Company Name (optional)")
    if st.button("Get HTS Code"):
        if product:
            st.json(f2.get_product_hts_info(product, company))
        else:
            st.warning("Please enter a product name.")

# --- Tab 2: Material Suggestions ---
with tabs[2]:
    st.subheader("Material Proportion Suggestions")
    material = st.text_input("Enter Material Composition")
    if st.button("Suggest Material Alternatives"):
        suggestions = f3.suggest_material_alternatives(material)
        if suggestions:
            for alt in suggestions:
                st.markdown(f"- Suggestion: {alt[0]} | Savings: {alt[1]} | Quality: {alt[2]}")
        else:
            st.warning("No suggestions found.")

# --- Tab 3: What-If Simulation ---
with tabs[3]:
    st.subheader("What-If Tariff Simulation")
    base = st.number_input("Base Price ($)", 0.0, key="base")
    old = st.number_input("Current Tariff Rate (%)", 0.0, key="old")
    new = st.number_input("New Tariff Rate (%)", 0.0, key="new")
    if st.button("Simulate New Tariff"):
        st.json(f4.simulate_tariff_change(base, old / 100, new / 100))

# --- Tab 4: HTS Lookup from Description ---
with tabs[4]:
    st.subheader("HTS Code Suggestion from Description")
    desc = st.text_input("Describe the Product")
    if st.button("Suggest HTS Codes"):
        st.json(f5.suggest_hts_code(desc))

# --- Tab 5: Scenario-Based Chatbot ---
with tabs[5]:
    st.subheader("Scenario-Based Chatbot")
    scenario_query = st.text_area("Enter your scenario or question", height=150)
    if st.button("Run Chatbot"):
        if scenario_query:
            with st.spinner("Running agents..."):
                result = run_tariff_analysis_scenario(scenario_query)
                st.markdown(result)
        else:
            st.warning("Please enter a scenario.")
