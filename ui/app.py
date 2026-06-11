import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🏗️ Jeevan Build Tech AI")

plot = st.text_input("Plot Size (e.g., 25x35)")
facing = st.selectbox("Facing", ["North", "East", "South", "West"])
budget = st.number_input("Budget (Lakhs)")
location = st.text_input("Location", value="Coimbatore")

if st.button("Generate Plan"):
    res = requests.post(
        f"{API_URL}/generate-plan",
        json={
            "plot": plot,
            "facing": facing,
            "budget": budget,
            "location": location
        }
    )

    st.subheader("📐 Plan Output")
    st.write(res.json()["plan"])


st.subheader("💰 Cost Estimation")

area = st.number_input("Built-up Area (sqft)")

if st.button("Calculate Cost"):
    res = requests.post(
        f"{API_URL}/cost-analysis",
        json={"area_sqft": area}
    )

    data = res.json()

    st.write(f"Cost: ₹{data['cost']}")
    st.write(f"Selling Price: ₹{data['selling_price']}")
    st.write(f"Profit: {round(data['profit_percent'],2)}%")
