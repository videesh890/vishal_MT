# api_server.py

from fastapi import FastAPI
from features import (
    feature_1_tariff_calc as f1,
    feature_2_product_hts_lookup as f2,
    feature_3_material_suggestions as f3,
    feature_4_what_if_simulation as f4,
    feature_5_hts_lookup as f5
)
from pydantic import BaseModel

app = FastAPI()


class TariffInput(BaseModel):
    price: float
    rate: float


@app.post("/tariff/calculate")
def calc_tariff(data: TariffInput):
    return f1.calculate_landed_cost(data.price, data.rate)


class ProductInput(BaseModel):
    product: str
    company: str = ""


@app.post("/hts/lookup")
def hts_lookup(data: ProductInput):
    return f2.get_product_hts_info(data.product, data.company)


class MaterialInput(BaseModel):
    material: str


@app.post("/material/suggest")
def material_suggest(data: MaterialInput):
    return f3.suggest_material_alternatives(data.material)


class WhatIfInput(BaseModel):
    base_price: float
    old_rate: float
    new_rate: float


@app.post("/tariff/whatif")
def whatif_simulation(data: WhatIfInput):
    return f4.simulate_tariff_change(data.base_price, data.old_rate, data.new_rate)


class HTSDescInput(BaseModel):
    description: str


@app.post("/hts/suggest")
def hts_from_description(data: HTSDescInput):
    return f5.suggest_hts_code(data.description)
