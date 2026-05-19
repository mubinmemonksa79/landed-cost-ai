import streamlit as st

st.title("AI Import Landed Cost Calculator (Dammam)")

st.write("Estimate total import cost from pickup to delivery in Saudi Arabia")

product_value = st.number_input("Product Value (USD)", min_value=0.0, value=1000.0)
weight = st.number_input("Weight (KG)", min_value=0.0, value=100.0)
cbm = st.number_input("Volume (CBM)", min_value=0.0, value=1.0)

mode = st.selectbox("Shipping Mode", ["Sea", "Air"])
origin = st.selectbox("Origin", ["China", "India", "UAE", "Turkey", "USA"])

if mode == "Sea":
    freight_per_cbm = 80 if origin == "China" else 120
    freight_cost = cbm * freight_per_cbm
else:
    freight_per_kg = 4 if origin == "China" else 6
    freight_cost = weight * freight_per_kg

duty_rate = 0.05
vat_rate = 0.15

customs_duty = product_value * duty_rate
vat = (product_value + freight_cost + customs_duty) * vat_rate

landed_cost = product_value + freight_cost + customs_duty + vat

st.subheader("Cost Breakdown")

st.write(f"Freight Cost: ${freight_cost:,.2f}")
st.write(f"Customs Duty (5%): ${customs_duty:,.2f}")
st.write(f"VAT (15%): ${vat:,.2f}")

st.subheader("TOTAL LANDED COST")
st.success(f"${landed_cost:,.2f}")
