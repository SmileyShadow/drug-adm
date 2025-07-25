import streamlit as st
import pandas as pd

# Function to load data from CSV
def load_data():
    df = pd.read_csv('formulary.csv')
    return df

# Function to display drug details
def display_drug_info(search_term, df):
    # Search by either Generic Drug Name, Brand Name, or P/P (Pack/Presentation)
    drug_info = df[df['Drug Name'].str.contains(search_term, case=False, na=False) | 
                   df['P/P'].str.contains(search_term, case=False, na=False)]
    
    if not drug_info.empty:
        for index, row in drug_info.iterrows():
            st.subheader(f"Drug Name: {row['Drug Name']}")
            st.write(f"**P/P**: {row['P/P']}")
            st.write(f"**Adm**: {row['Adm']}")
            st.write(f"**Category**: {row['Category']}")
            st.write(f"**Indications**: {row['Indications']}")
    else:
        st.error("No matching drug found!")

# Main function for Streamlit app
def main():
    # Title of the app
    st.title("Drug Administration Guide")
    st.markdown("Search for a drug by **Generic Name**, **Brand Name**, or **P/P (Pack/Presentation)** to get key information about its administration, category, and indications.")
    
    # Load the CSV data
    df = load_data()
    
    # Search input for drug name or P/P
    search_term = st.text_input("Enter Generic Drug Name, Brand Name, or P/P (Pack/Presentation):")
    
    if search_term:
        display_drug_info(search_term, df)

if __name__ == "__main__":
    main()
