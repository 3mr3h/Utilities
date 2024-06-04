# pip install re
# pip install python-docx
import re
from docx import Document  # Correct import statement

def extract_text_from_docx(docx_path):
    try:
        document = Document(docx_path)  # Open the document
    except Exception as e:
        print(f"Error loading document: {e}")
        return ""
    
    full_text = []
    for para in document.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def find_acronyms(text):
    # This regex will match acronyms which are in uppercase and are 2-10 characters long
    acronyms = re.findall(r'\b[A-Z]{2,10}\b', text)
    set_acronyms = set(acronyms)
    sorted_acronyms = sorted(set_acronyms)
    return (sorted_acronyms)

def save_acronyms_to_txt(acronyms, output_path):
    try:
        with open(output_path, 'w') as f:
            for acronym in acronyms:
                f.write(f"{acronym}\n")
        print(f"Acronyms saved to {output_path}")
    except Exception as e:
        print(f"Error saving acronyms to file: {e}")

def main(docx_path, output_path):
    text = extract_text_from_docx(docx_path)
    if not text:
        print("No text extracted from document.")
        return
    
    acronyms = find_acronyms(text)
    if not acronyms:
        print("No acronyms found.")
        return
    
    print("Acronyms found:")
    for acronym in acronyms:
        print(acronym)
    save_acronyms_to_txt(acronyms, output_path)

# Example usage
docx_path = r'G:\My Drive\0.All\0.Academic\0.METU\1.THESIS WORK\PHD_IS\2.Thesis\060324\9.ThesisDraft.docx'
output_path = r'G:\My Drive\0.All\0.Academic\0.METU\1.THESIS WORK\PHD_IS\2.Thesis\060324\acronyms.txt'
main(docx_path, output_path)