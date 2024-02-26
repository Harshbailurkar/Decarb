import streamlit as st

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS_INDIVIDUAL = {
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
    }
}

EMISSION_FACTORS_INDUSTRY = {
    "India": {
        "Manufacturing": 1.0,  # kgCO2/unit (example value)
        "Construction": 2.5,  # kgCO2/unit (example value)
        "Chemical Processing": 3.0,  # kgCO2/unit (example value)
        "Agriculture": 0.7,  # kgCO2/kg (example value)
        "Logging": 0.9,  # kgCO2/kg (example value)
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Carbon Calculator")

# Streamlit app code
st.title("Carbon Calculator App ⚠️")

# User selects whether they are an individual or industry
user_type = st.radio("Are you an individual or an industry?", ("Individual", "Industry"))

if user_type == "Individual":
    # Individual inputs
    st.subheader("🌍 Your Country (Individual)")
    country_individual = st.selectbox("Select", ["India"])

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚗 Daily commute distance (in km)")
        distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

        st.subheader("💡 Monthly electricity consumption (in kWh)")
        electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

        st.subheader("🏠 Home Energy Usage (in kWh)")
        home_energy = st.slider("Home Energy", 0.0, 1000.0, key="home_energy_input")

        st.subheader("🍽️ Number of meals per day")
        meals = st.number_input("Meals", 0, key="meals_input")

        st.subheader("🍽️ Waste generated per week (in kg)")
        waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    with col2:
        st.subheader("🚜 Agriculture Output (kg)")
        agriculture = st.slider("Agriculture", 0.0, 1000.0, key="agriculture_input")

        st.subheader("🌳 Logging Output (kg)")
        logging = st.slider("Logging", 0.0, 1000.0, key="logging_input")

    # Calculate carbon emissions only if inputs are provided
    emissions_individual = {}

    if distance > 0:
        emissions_individual["Transportation"] = EMISSION_FACTORS_INDIVIDUAL[country_individual]["Transportation"] * distance

    if electricity > 0:
        emissions_individual["Electricity"] = EMISSION_FACTORS_INDIVIDUAL[country_individual]["Electricity"] * electricity

    if home_energy > 0:
        emissions_individual["Home Energy"] = EMISSION_FACTORS_INDIVIDUAL[country_individual]["Home Energy"] * home_energy

    if meals > 0:
        emissions_individual["Diet"] = EMISSION_FACTORS_INDIVIDUAL[country_individual]["Diet"] * meals

    if waste > 0:
        emissions_individual["Waste"] = EMISSION_FACTORS_INDIVIDUAL[country_individual]["Waste"] * waste

    if agriculture > 0:
        emissions_individual["Agriculture"] = EMISSION_FACTORS_INDIVIDUAL[country_individual]["Agriculture"] * agriculture

    if logging > 0:
        emissions_individual["Logging"] = EMISSION_FACTORS_INDIVIDUAL[country_individual]["Logging"] * logging

    # Convert emissions to tonnes and round off to 2 decimal points
    total_emissions_individual = round(sum(emissions_individual.values()) / 1000, 2)

    # Calculate total emissions for individuals
    if st.button("Calculate Carbon Emission Score (Individual)"):
        # Display results
        st.header("Results (Individual)")

        st.subheader("Carbon Emissions by Category (Individual)")
        for category, emission in emissions_individual.items():
            st.info(f"{category}: {emission} tonnes CO2 per year")

        st.subheader("Total Carbon Emission Score (Individual)")
        st.success(f"🌍 Your total carbon emission score (Individual) is: {total_emissions_individual} tonnes CO2 per year")

else:  # For industries
    # Industry inputs
    st.subheader("🌍 Your Country (Industry)")
    country_industry = st.selectbox("Select", ["India"])

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏭 Manufacturing Output (units)")
        manufacturing = st.slider("Manufacturing", 0.0, 1000.0, key="manufacturing_input")

        st.subheader("🏗️ Construction Output (units)")
        construction = st.slider("Construction", 0.0, 1000.0, key="construction_input")

        st.subheader("⚗️ Chemical Processing Output (units)")
        chemical_processing = st.slider("Chemical Processing", 0.0, 1000.0, key="chemical_processing_input")

    with col2:
        st.subheader("🚆 Public Transport Usage (in km)")
        public_transport = st.slider("Public Transport", 0.0, 1000.0, key="public_transport_input")

    # Calculate carbon emissions only if inputs are provided
    emissions_industry = {}

    if manufacturing > 0:
        emissions_industry["Manufacturing"] = EMISSION_FACTORS_INDUSTRY[country_industry]["Manufacturing"] * manufacturing

    if construction > 0:
        emissions_industry["Construction"] = EMISSION_FACTORS_INDUSTRY[country_industry]["Construction"] * construction

    if chemical_processing > 0:
        emissions_industry["Chemical Processing"] = EMISSION_FACTORS_INDUSTRY[country_industry]["Chemical Processing"] * chemical_processing

    if public_transport > 0:
        emissions_industry["Public Transport"] = EMISSION_FACTORS_INDI
