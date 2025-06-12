import streamlit as st

# First, do some unessential modifications to the page
st.set_page_config(
    page_title="Nano Data Exploration Demo",
    page_icon=":bar_chart:",
)

# Start with some static data to present the project
st.write("""
    # ~Mini~ Nano Data Exploration Demo

    This is a simple demo of a data exploration app using Streamlit.

    ## Objectives
    - [ ] Load a dataset
    - [ ] Display raw data
    - [ ] Do some basic data exploration
    - [ ] Add some basic pre-processing or cleanup
    - [ ] Add some basic interactive visualizations
    - [ ] Outline some non-scientific conclusions
""")
