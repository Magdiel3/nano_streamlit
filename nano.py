import streamlit as st
import pandas as pd
from os.path import basename

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
    - [X] Load a dataset
    - [ ] Display raw data
    - [ ] Do some basic data exploration
    - [ ] Add some basic pre-processing or cleanup
    - [ ] Add some basic interactive visualizations
    - [ ] Outline some non-scientific conclusions
""")

# DATASET LOADING

dataset_name = "./datasets/CoffeeAndCodeLT2018---CoffeeAndCodeLT2018.csv"

st.write(f"""
         ### Dataset loading

         This section may be not very useful from the user perspective, but it is an essential step.
         The dataset `{basename(dataset_name)}` is loaded with the following code:
         ```python
         import pandas as pd

         dataset_name = "{dataset_name}"
         df = pd.read_csv(dataset_name, encoding="utf-8")
         ```
         """)

dataset_name = "./datasets/CoffeeAndCodeLT2018---CoffeeAndCodeLT2018.csv"
df = pd.read_csv(dataset_name, encoding="utf-8")

