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
    - [X] Do some basic data exploration
    - [X] Add some basic pre-processing or cleanup
    - [X] Add some basic interactive visualizations
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

# BASIC DATA CLEANUP
st.write("""
         ### Basic Data Cleanup
         In this section, we will drop the rows with missing values. This can be done using the
         following code:
            ```python
            df = df.dropna()
            st.write("#### Data after dropping missing values")
            st.dataframe(df.head())
            ```
         """)
df = df.dropna()
st.write("#### Data after dropping missing values")
st.write(f"""
         As tou can see, at least in the very first 5 rows we had an entry with missing values, so
         it was dropped and no longer appears in the head of the dataset. Now we reaim with only
            {len(df)} rows and {len(df.columns)} columns.
         """)
st.dataframe(df.head())

# NON STREAMLIT CODE
print("This is something that will be executed either when this script is run directly with"
      "python, or when it is launched with stramlit")
rows = len(df)
print(f"Total rows in the dataset: {rows}")
print(df.columns.tolist())

# INTERACTIVE DATA VISUALIZATION
st.write("""
         ### Interactive Data Visualization
         For this demo, we can choose to visualize the distribution of the non-numeric columns by
         selecting one from the dropdown below. This can be done using the following code:
            ```python
            st.write("#### Interactive Data Visualization")
            selected_column = st.selectbox("Select a column to visualize", df.select_dtypes(include=['object']).columns)
            st.bar_chart(data=df[selected_column].value_counts(), use_container_width=True)
            ```
         """)
st.write("#### Interactive Data Visualization")
selected_column = st.selectbox("Select a column to visualize", df.select_dtypes(include=['object']).columns)
st.bar_chart(data=df[selected_column].value_counts(), use_container_width=True)

st.write(f"""
         But lets not stop here! We can select with a slider the range of coffe cups per day and
         from that filtered dataset, we can visualize the distribution of the selected column in
         the dropdown menu. This can be done using the following code:
            ```python
            min_cups, max_cups = st.slider(
                "Select the range of coffee cups per day",
                0, int(df['CoffeeCupsPerDay'].min()), (0, int(df['CoffeeCupsPerDay'].max()))
            )
            filtered_df = df[
                (df['CoffeeCupsPerDay'] >= min_cups) & (df['CoffeeCupsPerDay'] <= max_cups)
            ]
            selected_column = st.selectbox(
                "Select a column to visualize",
                filtered_df.columns
            )
            st.bar_chart(
                data=filtered_df[selected_column].value_counts(),
                use_container_width=True
            )
            ```
         """)
min_cups, max_cups = st.slider(
    "Select the range of coffee cups per day",
    0, int(df['CoffeeCupsPerDay'].min()), (0, int(df['CoffeeCupsPerDay'].max()))
)
filtered_df = df[
    (df['CoffeeCupsPerDay'] >= min_cups) & (df['CoffeeCupsPerDay'] <= max_cups)
]
selected_column = st.selectbox(
    "Select a column to visualize",
    filtered_df.columns
)
st.bar_chart(
    data=filtered_df[selected_column].value_counts(),
    use_container_width=True
)
