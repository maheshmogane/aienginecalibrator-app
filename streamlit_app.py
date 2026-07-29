
import streamlit as st

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="AI Engine Calibration Assistant",
    page_icon="🚜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# Custom CSS
# ----------------------------------------------------------

st.markdown("""
<style>

.main-header{
    font-size:40px;
    color:#1E88E5;
    text-align:center;
    font-weight:bold;
}

.sub-header{
    font-size:22px;
    text-align:center;
    color:gray;
}

.metric-box{
    background-color:#F8F9FA;
    padding:20px;
    border-radius:10px;
}

.footer{
    text-align:center;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

st.sidebar.title("🚜 AI Engine Calibration")

st.sidebar.markdown("---")

st.sidebar.success("Version 1.0")

st.sidebar.markdown("### Developed By")

st.sidebar.info("Mahesh D. Mogane")

st.sidebar.markdown("### University")

st.sidebar.write("BITS Pilani")

st.sidebar.markdown("---")

st.sidebar.markdown("## Modules")

st.sidebar.write("🏠 Home")

st.sidebar.write("📂 Upload Dataset")

st.sidebar.write("📊 Data Analysis")

st.sidebar.write("🤖 Train Models")

st.sidebar.write("📈 Compare Models")

st.sidebar.write("🔍 SHAP Explainability")

st.sidebar.write("🎯 Prediction")

st.sidebar.write("🧬 Genetic Algorithm")

st.sidebar.write("🐦 Particle Swarm Optimization")

st.sidebar.write("🧠 Bayesian Optimization")

st.sidebar.write("⚖ Optimizer Comparison")

st.sidebar.write("🗺 Calibration Map")

st.sidebar.write("📄 Generate Report")

# ----------------------------------------------------------
# Header
# ----------------------------------------------------------

st.markdown(
    '<p class="main-header">AI Engine Calibration Assistant</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-header">'
    'Application of Artificial Intelligence & Machine Learning '
    'for Performance and Emission Optimization'
    '</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# ----------------------------------------------------------
# Dashboard Metrics
# ----------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Machine Learning Models",
        "4"
    )

with col2:

    st.metric(
        "AI Optimizers",
        "3"
    )

with col3:

    st.metric(
        "Emission Targets",
        "5"
    )

with col4:

    st.metric(
        "Application Status",
        "Ready"
    )

st.markdown("---")

# ----------------------------------------------------------
# Project Overview
# ----------------------------------------------------------

st.header("📖 Project Overview")

st.write("""

This application provides an end-to-end Artificial Intelligence
solution for diesel engine calibration.

The software predicts engine emissions using Machine Learning
and automatically optimizes calibration parameters using
Artificial Intelligence algorithms.

""")

# ----------------------------------------------------------
# Features
# ----------------------------------------------------------

st.header("🚀 Features")

feature1, feature2 = st.columns(2)

with feature1:

    st.success("Machine Learning")

    st.write("""
    ✔ Random Forest

    ✔ Gradient Boosting

    ✔ XGBoost

    ✔ Artificial Neural Network
    """)

with feature2:

    st.success("Artificial Intelligence")

    st.write("""
    ✔ Genetic Algorithm

    ✔ Particle Swarm Optimization

    ✔ Bayesian Optimization

    ✔ Automatic Calibration Map
    """)

st.markdown("---")

# ----------------------------------------------------------
# Workflow
# ----------------------------------------------------------

st.header("⚙ Workflow")

st.info("""

Upload Dataset

↓

Data Cleaning

↓

Feature Engineering

↓

Train Machine Learning Models

↓

Compare Models

↓

Explain Predictions using SHAP

↓

Predict Emissions

↓

AI Optimization (GA / PSO / Bayesian)

↓

Generate Calibration Map

↓

Download Report

""")

st.markdown("---")

# ----------------------------------------------------------
# Expected Inputs
# ----------------------------------------------------------

st.header("📥 Input Parameters")

inputs = [

    "Engine Speed",

    "Load",

    "Fuel Flow",

    "Air Flow",

    "EGR",

    "SIT",

    "Nozzle Opening Pressure",

    "Ambient Temperature",

    "Ambient Pressure",

    "Relative Humidity"

]

st.table(inputs)

# ----------------------------------------------------------
# Expected Outputs
# ----------------------------------------------------------

st.header("📤 Predicted Outputs")

outputs = [

    "NOX",

    "Smoke",

    "Soot",

    "CO",

    "HC"

]

st.table(outputs)

st.markdown("---")

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------

st.markdown(
    "<p class='footer'>"
    "Developed for M.Tech Dissertation | "
    "BITS Pilani | AI & ML"
    "</p>",
    unsafe_allow_html=True
)
