import fitz  # PyMuPDF
import re
import pandas as pd

# Function to extract text from the PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

# Function to parse the extracted text and return structured data
def parse_formulary(text):
    drugs = []
    # Regex pattern to match drug name, admin instructions, and indications
    pattern = r"(?P<drug_name>[\w\s]+)(?P<adm>Adm:.*?)(?P<indications>Indications:.*?)\n"
    
    matches = re.finditer(pattern, text, re.DOTALL)
    
    for match in matches:
        drug_name = match.group("drug_name").strip()
        adm = match.group("adm").strip().replace("Adm:", "").strip()
        indications = match.group("indications").strip().replace("Indications:", "").strip()
        drugs.append({"Drug Name": drug_name, "Adm": adm, "Indications": indications})
    
    return drugs

# Function to save the extracted data to CSV
def save_to_csv(drugs_data, file_name):
    df = pd.DataFrame(drugs_data)
    df.to_csv(file_name, index=False)
    print(f"Data saved to {file_name}")

# Main function to extract and save data
def main():
    pdf_path = 'formulary.pdf'  # Replace with the actual path to your PDF file
    pdf_text = extract_text_from_pdf(pdf_path)
    drugs_data = parse_formulary(pdf_text)
    save_to_csv(drugs_data, "formulary.csv")

if __name__ == "__main__":
    main()
