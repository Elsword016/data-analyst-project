import streamlit as st 
from multipage import MultiApp
from pages import insurance_data,insurance_model

app = MultiApp()

st.markdown("# Welcome to the Insurance Data App")

app.add_app("Insurance Data", insurance_data.app)
app.add_app("Model",insurance_model.app)

app.run()