import pandas as pd
import streamlit as st

# Load the dataset
df = pd.read_csv("car_data.csv")

# Sidebar
st.sidebar.header("Filter options")

# Car name text input
car_name = st.sidebar.text_input("Car Name")

# Transmission type multiselect
transmission = st.sidebar.multiselect("Transmission", options=["Manual", "Automatic"], default=["Manual", "Automatic"])

# Selling price slider
selling_price = st.sidebar.slider("Selling Price", 0, 20, (0, 20))

# Year slider
year = st.sidebar.slider("Year", 2000, 2024, (2000, 2024))

# Button to filter data
if st.sidebar.button("Submit"):
    # Filter the dataframe
    filtered_df = df[
        (df['Selling_Price'].between(selling_price[0], selling_price[1])) &
        (df['Year'].between(year[0], year[1])) &
        (df['Transmission'].isin(transmission))
    ]
    
    if car_name:
        filtered_df = filtered_df[filtered_df['Car_Name'].str.contains(car_name, case=False, na=False)]
    
    st.dataframe(filtered_df)
else:
    # Show original data if no filters are selected
    st.dataframe(df)
