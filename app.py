import streamlit as st
import pandas as pd

# Load your data (replace 'your_formulary_file.csv' with your actual file name)
def load_data():
    # Replace with your actual file path or URL on GitHub
    df = pd.read_csv('your_formulary_file.csv')  # Example for CSV file
    return df

# Display drug details
def display_drug_info(drug_name, df):
    drug_info = df[df['Drug Name'].str.contains(drug_name, case=False, na=False)]
    if not drug_info.empty:
        for index, row in drug_info.iterrows():
            st.subheader(f"Drug: {row['Drug Name']}")
            st.write(f"**Indications**: {row['Indications']}")
            st.write(f"**Administration**: {row['Adm']}")
    else:
        st.error("No matching drug found!")

# Main function
def main():
    # Title and description
    st.title("Drug Administration Guide")
    st.markdown("Search for a drug to get key information about its administration and indications.")
    
    # Load data
    df = load_data()
    
    # Drug search input
    drug_name = st.text_input("Enter Drug Name:")

    if drug_name:
        display_drug_info(drug_name, df)

if __name__ == "__main__":
    main()
