import streamlit as st
import pandas as pd
import plotly.express as px

# Function to calculate carbon emissions for individuals
def calculate_individual_emissions(data, country):
    total_emissions = 0
    for category, value in data.items():
        total_emissions += value * EMISSION_FACTORS_INDIVIDUAL[country][category]
    return total_emissions

# Function to calculate carbon emissions for industries
def calculate_industry_emissions(data, country):
    total_emissions = 0
    for category, value in data.items():
        total_emissions += value * ADDITIONAL_EMISSION_FACTORS_INDUSTRY[country][category]
    return total_emissions

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS_INDIVIDUAL = {
    "India": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal
        "Waste": 0.1,  # kgCO2/kg
        "Home Energy": 0.5,  # kgCO2/kWh
    }
}

ADDITIONAL_EMISSION_FACTORS_INDUSTRY = {
    "India": {
        "Manufacturing": 1.0,  # kgCO2/unit
        "Construction": 2.5,  # kgCO2/unit
        "Chemical Processing": 3.0,  # kgCO2/unit
        "Public Transport": 0.08,  # kgCO2/passenger km
        "Recycling Rate": 0.2,  # kgCO2/kg
        "Emissions Trading": 0.5,  # kgCO2/kg
        "Carbon Offsetting": -0.7,  # kgCO2/kg
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Carbon Calculator")

# Streamlit app code
st.title("Carbon Calculator App ⚠️")

# User inputs
st.sidebar.subheader("User Inputs")
user_type = st.sidebar.radio("Are you an individual or an industry?", ("Individual", "Industry"))
data_source = st.sidebar.radio("How would you like to input data?", ("Manual", "Sensor"))

if user_type == "Individual":
    st.sidebar.subheader("Individual Inputs")
    country_individual = st.sidebar.selectbox("Your Country", ["India"])
    distance = st.sidebar.slider("Daily Commute Distance (km)", 0.0, 100.0, 0.0)
    electricity = st.sidebar.slider("Monthly Electricity Consumption (kWh)", 0.0, 1000.0, 0.0)
    diet = st.sidebar.slider("Number of Meals per Day", 0, 10, 0)
    waste = st.sidebar.slider("Weekly Waste Generated (kg)", 0.0, 100.0, 0.0)
    home_energy = st.sidebar.slider("Home Energy Usage (kWh)", 0.0, 1000.0, 0.0)

    data_individual = {
        "Transportation": distance,
        "Electricity": electricity,
        "Diet": diet,
        "Waste": waste,
        "Home Energy": home_energy
    }

    if data_source == "Manual":
        total_emissions_individual = calculate_individual_emissions(data_individual, country_individual)
        st.write(f"Total Carbon Emissions (Individual): {total_emissions_individual} kgCO2")

        # Display emissions breakdown in a bar chart
        st.subheader("Carbon Emissions Breakdown (Individual)")
        df_individual = pd.DataFrame(data_individual.items(), columns=["Category", "Value"])
        fig_individual = px.bar(df_individual, x="Category", y="Value", title="Carbon Emissions Breakdown (Individual)", labels={"Value": "Quantity"})
        st.plotly_chart(fig_individual)

        # Suggestions for reducing carbon footprint
        st.subheader("Suggestions for Reducing Carbon Footprint (Individual)")
        if distance > 50:
            st.write("Consider using public transportation or carpooling to reduce emissions from commuting.")
        if electricity > 500:
            st.write("Try to reduce electricity consumption by turning off lights and appliances when not in use.")
        if diet > 3:
            st.write("Reducing meat consumption and adopting a more plant-based diet can help lower carbon emissions associated with food production.")
        if waste > 20:
            st.write("Implementing waste reduction strategies such as recycling, composting, and reducing single-use items can reduce carbon emissions from waste disposal.")
        if home_energy > 600:
            st.write("Improving home energy efficiency can significantly reduce carbon emissions. Consider insulating your home or installing energy-efficient appliances.")

    else:
        st.write("Sensor data input is not available for individuals.")

else:
    st.sidebar.subheader("Industry Inputs")
    country_industry = st.sidebar.selectbox("Your Country", ["India"])
    manufacturing = st.sidebar.slider("Manufacturing Output (units)", 0.0, 1000.0, 0.0)
    construction = st.sidebar.slider("Construction Output (units)", 0.0, 1000.0, 0.0)
    chemical_processing = st.sidebar.slider("Chemical Processing Output (units)", 0.0, 1000.0, 0.0)
    public_transport = st.sidebar.slider("Public Transport Usage (km)", 0.0, 1000.0, 0.0)
    recycling = st.sidebar.slider("Recycling Rate (kg)", 0.0, 1000.0, 0.0)
    emissions_trading = st.sidebar.slider("Emissions Trading (kg)", 0.0, 1000.0, 0.0)
    carbon_offsetting = st.sidebar.slider("Carbon Offsetting (kg)", 0.0, 1000.0, 0.0)

    data_industry = {
        "Manufacturing": manufacturing,
        "Construction": construction,
        "Chemical Processing": chemical_processing,
        "Public Transport": public_transport,
        "Recycling Rate": recycling,
        "Emissions Trading": emissions_trading,
        "Carbon Offsetting": carbon_offsetting
    }

    if data_source == "Manual":
        total_emissions_industry = calculate_industry_emissions(data_industry, country_industry)
        st.write(f"Total Carbon Emissions (Industry): {total_emissions_industry} kgCO2")

        # Display emissions breakdown in a bar chart
        st.subheader("Carbon Emissions Breakdown (Industry)")
        df_industry = pd.DataFrame(data_industry.items(), columns=["Category", "Value"])
        fig_industry = px.bar(df_industry, x="Category", y="Value", title="Carbon Emissions Breakdown (Industry)", labels={"Value": "Quantity"})
        st.plotly_chart(fig_industry)

        # Suggestions for reducing carbon footprint
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

    else:
        st.write("Sensor data input is not available for industries.")
