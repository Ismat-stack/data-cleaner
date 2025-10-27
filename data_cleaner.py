import streamlit as st
import pandas as pd

st.title("🧹 Data Cleaner / Preprocessor")

uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

# Convert DataFrame to CSV
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("📄 Original Data:")
    st.dataframe(df.head())

    # Handle missing values
    st.subheader("Handle Missing Values")
    st.write("🔍 Missing Values:")
    st.write(df.isnull().sum())

    method = st.selectbox(
        "Choose method to handle missing values:",
        ["None", "Drop rows", "Fill with Mean", "Fill with Median", "Custom Value"]
    )

    if method == "Drop rows":
        df = df.dropna()

    elif method in ["Fill with Mean", "Fill with Median"]:
        num_cols = df.select_dtypes(include='number').columns
        for col in num_cols:
            if method == "Fill with Mean":
                df[col] = df[col].fillna(df[col].mean())
            else:
                df[col] = df[col].fillna(df[col].median())

    elif method == "Custom Value":
        value = st.text_input("Enter custom value to fill:")
        if value:
            df = df.fillna(value)

    # Remove Duplicates
    st.subheader("Remove Duplicate Rows")
    if st.checkbox("Drop duplicates"):
        df = df.drop_duplicates()

    # Normalize numerical data
    st.subheader("Normalize Numerical Columns")
    if st.checkbox("Apply Min-Max Scaling"):
        num_cols = df.select_dtypes(include='number').columns
        df[num_cols] = (df[num_cols] - df[num_cols].min()) / (df[num_cols].max() - df[num_cols].min())

    # Show and download cleaned data
    st.subheader("📥 Download Cleaned Data")
    st.write("📊 Cleaned Data Preview:")
    st.dataframe(df.head())

    csv_data = convert_df(df)

    st.download_button(
        label="Download Cleaned CSV",
        data=csv_data,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
