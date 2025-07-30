# utils/helpers.py

import random

# A mock database to simulate product info and HTS classification
SYNTHETIC_HTS_DATABASE = {
    "nitrile gloves": {
        "brand": "McKesson",
        "origin": "Malaysia",
        "material": "100% Nitrile",
        "hts": "4015.19.0510",
        "tariff_rate": 0.03,
        "base_price": 1.00,
    },
    "cordless drill": {
        "brand": "Stanley Black & Decker",
        "origin": "China",
        "material": "60% Steel, 30% Plastic, 10% Electronics",
        "hts": "8467.21.0030",
        "tariff_rate": 0.017,
        "base_price": 50.00,
    }
}
# Simulated material alternatives (for optimization suggestions)
MATERIAL_ALTERNATIVES = {
    "steel": [("aluminum", 0.08, "95% strength")],
    "plastic": [("polypropylene", 0.03, "rigid"), ("HIPS", 0.0, "impact resistant")],
    "electronics": [("silver-plated", 0.1, "similar conductivity")],
}
def lookup_hts_from_description(description: str):
    for key in SYNTHETIC_HTS_DATABASE:
        if key in description.lower():
            return SYNTHETIC_HTS_DATABASE[key]
    return None
def calculate_tariff(base_price: float, rate: float):
    tariff = base_price * rate
    mpf = 0.02 if base_price > 0 else 0
    return {
        "tariff_per_unit": round(tariff, 2),
        "mpf": round(mpf, 2),
        "total_landed_cost": round(base_price + tariff + mpf, 2),
    }
def suggest_alternatives(material: str):
    suggestions = []
    for mat, alts in MATERIAL_ALTERNATIVES.items():
        if mat in material.lower():
            for alt in alts:
                suggestions.append((alt[0], f"${alt[1]:.2f}", alt[2]))
    return suggestions


def random_scenario_response():
    example = random.choice(list(SYNTHETIC_HTS_DATABASE.values()))
    cost = calculate_tariff(example["base_price"], example["tariff_rate"])
    return {
        "Product": example["hts"],
        "Brand": example["brand"],
        "Country of Origin": example["origin"],
        "Material": example["material"],
        "HTS Code": example["hts"],
        "Tariff Rate": f"{example['tariff_rate']*100:.1f}%",
        "Estimated Tariff": f"${cost['tariff_per_unit']}",
        "Total Landed Cost": f"${cost['total_landed_cost']}"
    }
