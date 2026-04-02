
import streamlit as st
import pandas as pd

st.title("Sales Summary App")
st.subheader("Filter sales by category")

data = {
    "Product": ["Laptop", "Shirt", "Phone", "Shoes", "Watch"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Accessories"],
    "Sales": [50000, 2000, 30000, 4000, 7000]
}

df = pd.DataFrame(data)

category = st.sidebar.selectbox("Select Category", df["Category"].unique())

filtered_df = df[df["Category"] == category]

st.dataframe(filtered_df)
st.line_chart(filtered_df.set_index("Product")["Sales"])

