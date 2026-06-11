from fastapi import FastAPI
from ai_engine import generate_response
from prompts import project_planning_prompt
from cost_engine import estimate_cost, suggest_price, profit_percentage

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Construction AI running"}


@app.post("/generate-plan")
def generate_plan(data: dict):
    prompt = project_planning_prompt(
        plot=data["plot"],
        facing=data["facing"],
        budget=data["budget"],
        location=data["location"]
    )

    ai_output = generate_response(prompt)

    return {"plan": ai_output}


@app.post("/cost-analysis")
def cost_analysis(data: dict):
    area = data["area_sqft"]

    cost = estimate_cost(area)
    selling_price = suggest_price(cost)
    profit = profit_percentage(cost, selling_price)

    return {
        "cost": cost,
        "selling_price": selling_price,
        "profit_percent": profit
    }
