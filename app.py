import streamlit as st

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.1,  # kgCO2/kg
        "Home Energy": 0.5,  # kgCO2/kWh (example value)
        "Public Transport": 0.08,  # kgCO2/passenger km (example value)
        "Recycling Rate": 0.2,  # kgCO2/kg (example value)
        "Renewable Energy": -0.3,  # Negative value for carbon credits from renewable energy
        "Vegetarian Diet": -0.5,  # Negative value for carbon credits from vegetarian diet
        "Manufacturing": 1.0,  # kgCO2/unit (example value)
        "Construction": 2.5,  # kgCO2/unit (example value)
        "Chemical Processing": 3.0,  # kgCO2/unit (example value)
        "Agriculture": 0.7,  # kgCO2/kg (example value)
        "Logging": 0.9,  # kgCO2/kg (example value)
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")

# Streamlit app code
st.title("Personal Carbon Calculator App ⚠️")

# User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select", ["India"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 Daily commute distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

    st.subheader("🏠 Home Energy Usage (in kWh)")
    home_energy = st.slider("Home Energy", 0.0, 1000.0, key="home_energy_input")

    st.subheader("🏭 Manufacturing Output (units)")
    manufacturing = st.slider("Manufacturing", 0.0, 1000.0, key="manufacturing_input")

with col2:
    st.subheader("🍽️ Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("🍽️ Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")

    st.subheader("🚜 Agriculture Output (kg)")
    agriculture = st.slider("Agriculture", 0.0, 1000.0, key="agriculture_input")

    st.subheader("🌳 Logging Output (kg)")
    logging = st.slider("Logging", 0.0, 1000.0, key="logging_input")

# Calculate carbon emissions only if inputs are provided
emissions = {}

if distance > 0:
    emissions["Transportation"] = EMISSION_FACTORS[country]["Transportation"] * distance

if electricity > 0:
    emissions["Electricity"] = EMISSION_FACTORS[country]["Electricity"] * electricity

if home_energy > 0:
    emissions["Home Energy"] = EMISSION_FACTORS[country]["Home Energy"] * home_energy

if manufacturing > 0:
    emissions["Manufacturing"] = EMISSION_FACTORS[country]["Manufacturing"] * manufacturing

if meals > 0:
    emissions["Diet"] = EMISSION_FACTORS[country]["Diet"] * meals

if waste > 0:
    emissions["Waste"] = EMISSION_FACTORS[country]["Waste"] * waste

if agriculture > 0:
    emissions["Agriculture"] = EMISSION_FACTORS[country]["Agriculture"] * agriculture

if logging > 0:
    emissions["Logging"] = EMISSION_FACTORS[country]["Logging"] * logging

# Convert emissions to tonnes and round off to 2 decimal points
total_emissions = round(sum(emissions.values()) / 1000, 2)

# Calculate total emissions
if st.button("Calculate Carbon Emission Score"):

    # Display results
    st.header("Results")

    st.subheader("Carbon Emissions by Category")
    for category, emission in emissions.items():
        st.info(f"{category}: {emission} tonnes CO2 per year")

    st.subheader("Total Carbon Emission Score")
    st.success(f"🌍 Your total carbon emission score is: {total_emissions} tonnes CO2 per year")
