from functions import extract_text_from_pdf, convert_pdf_to_docx
from constants import PDF_PATH, DOCX_PATH, PDF_FORMAT, DOCX_FORMAT, FILE_NAME


if __name__ == "__main__":
    pdf_path = PDF_PATH + FILE_NAME + PDF_FORMAT
    docx_path = DOCX_PATH + FILE_NAME + DOCX_FORMAT
    print(extract_text_from_pdf(pdf_path))
    convert_pdf_to_docx(pdf_path, docx_path)
