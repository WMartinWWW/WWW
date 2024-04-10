{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6c59b39a-af7c-4d25-85b5-9eb04eddb4e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "\n",
    "# Load the dataset\n",
    "df = pd.read_csv(\"/Users/w./Desktop/DS549/Lab12/car_data.csv\")\n",
    "\n",
    "# Sidebar\n",
    "st.sidebar.header(\"Filter options\")\n",
    "\n",
    "# Car name text input\n",
    "car_name = st.sidebar.text_input(\"Car Name\")\n",
    "\n",
    "# Transmission type multiselect\n",
    "transmission = st.sidebar.multiselect(\"Transmission\", options=[\"Manual\", \"Automatic\"], default=[\"Manual\", \"Automatic\"])\n",
    "\n",
    "# Selling price slider\n",
    "selling_price = st.sidebar.slider(\"Selling Price\", 0, 20, (0, 20))\n",
    "\n",
    "# Year slider\n",
    "year = st.sidebar.slider(\"Year\", 2000, 2024, (2000, 2024))\n",
    "\n",
    "# Button to filter data\n",
    "if st.sidebar.button(\"Submit\"):\n",
    "    # Filter the dataframe\n",
    "    filtered_df = df[\n",
    "        (df['Selling_Price'].between(selling_price[0], selling_price[1])) &\n",
    "        (df['Year'].between(year[0], year[1])) &\n",
    "        (df['Transmission'].isin(transmission))\n",
    "    ]\n",
    "    \n",
    "    if car_name:\n",
    "        filtered_df = filtered_df[filtered_df['Car_Name'].str.contains(car_name, case=False, na=False)]\n",
    "    \n",
    "    st.dataframe(filtered_df)\n",
    "else:\n",
    "    # Show original data if no filters are selected\n",
    "    st.dataframe(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e095ae77-5560-4364-a5bf-16dbc10e6302",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
