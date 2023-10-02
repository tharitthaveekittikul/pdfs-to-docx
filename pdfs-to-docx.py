from functions import extract_text_from_pdf, convert_pdf_to_docx
from constants import PDF_PATH, DOCX_PATH, PDF_FORMAT, DOCX_FORMAT
from modules import os, load_dotenv

if __name__ == "__main__":
    load_dotenv()
    file_name = os.getenv("FILE_NAME")
    pdf_path = PDF_PATH + file_name + PDF_FORMAT
    docx_path = DOCX_PATH + file_name + DOCX_FORMAT
    print(extract_text_from_pdf(pdf_path))
    convert_pdf_to_docx(pdf_path, docx_path)
