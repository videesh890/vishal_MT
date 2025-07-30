# features/feature_4_what_if_simulation.py

def simulate_tariff_change(base_price: float, old_rate: float, new_rate: float):
    old_tariff = base_price * old_rate
    new_tariff = base_price * new_rate
    diff = new_tariff - old_tariff
    return {
        "Old Tariff": round(old_tariff, 2),
        "New Tariff": round(new_tariff, 2),
        "Difference": round(diff, 2),
        "Total Landed Cost with New Tariff": round(base_price + new_tariff, 2)
    }
