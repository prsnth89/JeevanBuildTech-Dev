def estimate_cost(area_sqft):
    cost_per_sqft = 2200  # adjust for Coimbatore
    return area_sqft * cost_per_sqft


def suggest_price(cost):
    return cost * 1.35  # 35% margin target


def profit_percentage(cost, selling_price):
    return ((selling_price - cost) / cost) * 100
