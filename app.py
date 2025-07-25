import streamlit as st
import pandas as pd

# Load the data (formulary.csv) into the app
def load_data():
    df = pd.read_csv('formulary.csv')
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
    st.title("Drug Administration Guide")
    st.markdown("Search for a drug to get key information about its administration and indications.")
    
    df = load_data()  # Load the CSV file containing the drug data
    
    # Search functionality
    drug_name = st.text_input("Enter Drug Name:")
    
    if drug_name:
        display_drug_info(drug_name, df)

if __name__ == "__main__":
    main()
