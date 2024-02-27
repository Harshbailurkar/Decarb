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

# Sample additional industry-specific factors
ADDITIONAL_EMISSION_FACTORS_INDUSTRY = {
    "India": {
        "Chemical Processing": 3.0,  # kgCO2/unit (example value)
        "Construction": 2.5,  # kgCO2/unit (example value)
        "Manufacturing": 1.0,  # kgCO2/unit (example value)
        "Agriculture": 0.7,  # kgCO2/kg (example value)
        "Logging": 0.9,  # kgCO2/kg (example value)
        "Public Transport": 0.08,  # kgCO2/passenger km (example value)
        "Recycling Rate": 0.2,  # kgCO2/kg (example value)
        "Renewable Energy": -0.3,  # Negative value for carbon credits from renewable energy
        "Emissions Trading": 0.5,  # Example value for emissions trading
        "Carbon Offsetting": -0.7,  # Example value for carbon offsetting
        "Custom Factor 1": 1.2,  # Example custom emission factor 1
        "Custom Factor 2": 0.9,  # Example custom emission factor 2
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Carbon Calculator")

# Streamlit app code
st.title("Carbon Calculator App ⚠️")

# User selects whether they are an individual or industry and how data should be inputted
user_type = st.radio("Are you an individual or an industry?", ("Individual", "Industry"))

data_source = st.radio("How would you like to input data?", ("Manual", "Sensor"))

if user_type == "Individual":
    # Individual inputs
    st.subheader("🌍 Your Country (Individual)")
    country_individual = st.selectbox("Select", ["India"], key="country_individual_selectbox")

    if data_source == "Manual":
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

            # Suggestions based on individual inputs
            st.subheader("Suggestions for Reducing Carbon Footprint (Individual)")

            if distance > 50:
                st.write("Consider using public transportation or carpooling to reduce emissions from commuting.")

            if electricity > 500:
                st.write("Try to reduce electricity consumption by turning off lights and appliances when not in use.")

            if home_energy > 600:
                st.write("Improving home energy efficiency can significantly reduce carbon emissions. Consider insulating your home or installing energy-efficient appliances.")

            if meals > 3:
                st.write("Reducing meat consumption and adopting a more plant-based diet can help lower carbon emissions associated with food production.")

            if waste > 20:
                st.write("Implementing waste reduction strategies such as recycling, composting, and reducing single-use items can reduce carbon emissions from waste disposal.")

else:  # For industries
    # Industry inputs
    st.subheader("🌍 Your Country (Industry)")
    country_industry = st.selectbox("Select", ["India"], key="country_industry_selectbox")

    if data_source == "Manual":
        st.subheader("🏭 Manufacturing Output (units)")
        manufacturing = st.slider("Manufacturing", 0.0, 1000.0, key="manufacturing_input")

        st.subheader("🏗️ Construction Output (units)")
        construction = st.slider("Construction", 0.0, 1000.0, key="construction_input")

        st.subheader("⚗️ Chemical Processing Output (units)")
        chemical_processing = st.slider("Chemical Processing", 0.0, 1000.0, key="chemical_processing_input")

        st.subheader("🚆 Public Transport Usage (in km)")
        public_transport = st.slider("Public Transport", 0.0, 1000.0, key="public_transport_input")

        st.subheader("🍽️ Recycling Rate (kg)")
        recycling = st.slider("Recycling", 0.0, 1000.0, key="recycling_input")

        st.subheader("💰 Emissions Trading (kg)")
        emissions_trading = st.slider("Emissions Trading", 0.0, 1000.0, key="emissions_trading_input")

        st.subheader("🌱 Carbon Offsetting (kg)")
        carbon_offsetting = st.slider("Carbon Offsetting", 0.0, 1000.0, key="carbon_offsetting_input")

        # Calculate carbon emissions only if inputs are provided
        emissions_industry = {}

        if manufacturing > 0:
            emissions_industry["Manufacturing"] = ADDITIONAL_EMISSION_FACTORS_INDUSTRY[country_industry]["Manufacturing"] * manufacturing

        if construction > 0:
            emissions_industry["Construction"] = ADDITIONAL_EMISSION_FACTORS_INDUSTRY[country_industry]["Construction"] * construction

        if chemical_processing > 0:
            emissions_industry["Chemical Processing"] = ADDITIONAL_EMISSION_FACTORS_INDUSTRY[country_industry]["Chemical Processing"] * chemical_processing

        if public_transport > 0:
            emissions_industry["Public Transport"] = ADDITIONAL_EMISSION_FACTORS_INDUSTRY[country_industry]["Public Transport"] * public_transport

        if recycling > 0:
            emissions_industry["Recycling"] = ADDITIONAL_EMISSION_FACTORS_INDUSTRY[country_industry]["Recycling Rate"] * recycling

        if emissions_trading > 0:
            emissions_industry["Emissions Trading"] = ADDITIONAL_EMISSION_FACTORS_INDUSTRY[country_industry]["Emissions Trading"] * emissions_trading

        if carbon_offsetting > 0:
            emissions_industry["Carbon Offsetting"] = ADDITIONAL_EMISSION_FACTORS_INDUSTRY[country_industry]["Carbon Offsetting"] * carbon_offsetting

        # Convert emissions to tonnes and round off to 2 decimal points
        total_emissions_industry = round(sum(emissions_industry.values()) / 1000, 2)

        # Calculate total emissions for industries
        if st.button("Calculate Carbon Emission Score (Industry)"):
            # Display results
            st.header("Results (Industry)")

            st.subheader("Carbon Emissions by Category (Industry)")
            for category, emission in emissions_industry.items():
                st.info(f"{category}: {emission} tonnes CO2 per year")

            st.subheader("Total Carbon Emission Score (Industry)")
            st.success(f"🌍 Your total carbon emission score (Industry) is: {total_emissions_industry} tonnes CO2 per year")

            # Suggestions based on individual inputs
            st.subheader("Suggestions for Reducing Carbon Footprint (Industry)")

            if manufacturing > 500:
                st.write("Improving energy efficiency in manufacturing processes can significantly reduce carbon emissions. Consider upgrading equipment and optimizing processes.")

            if construction > 400:
                st.write("Using sustainable building materials and construction techniques can lower carbon emissions associated with construction projects.")

            if chemical_processing > 300:
                st.write("Implementing cleaner production technologies and optimizing chemical processes can reduce carbon emissions from chemical processing.")

            if public_transport > 200:
                st.write("Encouraging the use of public transportation among employees and investing in green transportation options can help reduce carbon emissions from commuting.")

            if recycling > 100:
                st.write("Expanding recycling programs and increasing the use of recycled materials can lower carbon emissions associated with waste management.")

            if emissions_trading > 50:
                st.write("Participating in emissions trading schemes can provide opportunities to offset carbon emissions by investing in carbon reduction projects.")

            if carbon_offsetting > 20:
                st.write("Supporting carbon offsetting initiatives such as reforestation and renewable energy projects can help offset carbon emissions.")
