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
    - [X] Display raw data
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

# DISPLAY RAW DATA

st.write(f"""
         ### Display raw data

         Here we can see how the data was imported with just loading it with the default settings.
         This following 5 top rows are displayed using the following code:
            ```python
            import streamlit as st
            st.write("#### Raw Data (header)")
            st.dataframe(df.head())
            ```
         #### Raw Data (header)
         """)

st.dataframe(df.head())

st.write(f"""
         > **NOTE:** Though we are displaying only 5 entries, the dataset contains {len(df)} rows
         and {len(df.columns)} columns. These columns are:
         """)
st.write(df.columns.tolist())

# DATA EXPLORATION

st.write("""
         ### Data Exploration
         Now that we know the amount of data we are going to use, we can start exploring it. Some
         of the basic statistics can be displayed using the following code:
            ```python
            st.write("#### Basic Statistics")
            st.dataframe(df.describe())
            ```
         > **NOTE:** The `describe()` method provides a summary of the statistics only for the 
            numeric columns in the dataset.
         """)
st.write("#### Basic Statistics")
st.dataframe(df.describe())

st.write("""
         It is also useful to check for missing values in the dataset. This can be done using the
         following code:
            ```python
            st.write("#### Missing Values")
            st.dataframe(df.isnull().sum())
            ```
         """)
st.write("#### Missing Values")
st.dataframe(df.isnull().sum())

st.write("#### Missing Values Visualization")
st.write("""
         But who likes to only see numbers? Let's visualize the missing values in a more. This can
         be achieved with the following code:
            ```python
            st.write("#### Missing Values Visualization")
            st.bar_chart(data=df.isnull().sum(), use_container_width=True)
            ```
         """)
st.bar_chart(data=df.isnull().sum(), use_container_width=True)

st.write(f"""
         Dropping rows with missing values is a common practice, but it is not always the best. For
         this demo, we will be dropping a total of {len(df[df.isnull().any(axis=1)])} rows with
         missing values. (This is only {len(df[df.isnull().any(axis=1)]) / len(df) * 100:.2f}% of
         the total dataset.)
         """)

