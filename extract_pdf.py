import fitz  # PyMuPDF
import re
import pandas as pd
import os

# Function to extract text from the PDF
def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text("text")
        return text
    except Exception as e:
        print(f"Error while reading PDF: {e}")
        return None

# Function to parse the extracted text and return structured data
def parse_formulary(text):
    drugs = []
    
    # Updated regex pattern to capture Drug Name, P/P, Admin instructions, Category, Indications
    pattern = r"(?P<drug_name>[A-Za-z\s]+(?:\s(?:\(\w+\))?)?)\s*(?:\([^\)]+\))?\s*P/P:\s*(?P<pp>.*?)\s*Adm:\s*(?P<adm>.*?)(?=\nCategory:)(?P<category>.*?)\nIndications:\s*(?P<indications>.*?)\n"

    matches = re.finditer(pattern, text, re.DOTALL)
    
    for match in matches:
        drug_name = match.group("drug_name").strip()
        pp = match.group("pp").strip()
        adm = match.group("adm").strip()
        category = match.group("category").strip()
        indications = match.group("indications").strip()
        
        drugs.append({
            "Drug Name": drug_name,
            "P/P": pp,
            "Adm": adm,
            "Category": category,
            "Indications": indications
        })
    
    return drugs

# Function to save the extracted data to CSV
def save_to_csv(drugs_data, file_name):
    df = pd.DataFrame(drugs_data)
    df.to_csv(file_name, index=False)
    print(f"Data saved to {file_name}")

# Main function to extract and save data
def main():
    # Check if the Formulary.pdf exists in the current directory
    pdf_path = './Formulary.pdf'  # Assuming the PDF file is in the current directory

    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' does not exist.")
        return

    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)
    
    if pdf_text:
        # Parse the text and get structured data
        drugs_data = parse_formulary(pdf_text)
        
        if drugs_data:
            # Save the parsed data to CSV
            save_to_csv(drugs_data, "formulary.csv")
        else:
            print("No data parsed from the PDF.")
    else:
        print("Failed to extract text from the PDF.")

if __name__ == "__main__":
    main()
