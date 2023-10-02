from modules import fitz, Pt, Document
from constants import FONT_DEFAULT, FONT_SIZE


def extract_text_from_pdf(pdf_path, amount_of_pages=-1):
    with fitz.open(pdf_path) as pdf_document:
        # Validate amount_of_pages parameter
        if amount_of_pages < -1 or amount_of_pages > len(pdf_document):
            raise ValueError("Invalid amount_of_pages value")

        # If amount_of_pages is -1, extract text from all pages
        pages_to_extract = (
            range(len(pdf_document))
            if amount_of_pages == -1
            else range(amount_of_pages)
        )

        # every blocks
        text = ""
        for page_number in pages_to_extract:
            page = pdf_document[page_number]
            # Get text blocks and add a newline character after each block
            blocks = page.get_text("blocks")
            for block in blocks:
                block_text = block[4]  # block[4] contains the text in the block

                # Check if block_text is not an image metadata
                if not block_text.startswith("<image:"):
                    text += block_text + "\n"

        # every lines
        # text = ""
        # for page_number in pages_to_extract:
        #     page = pdf_document[page_number]
        #     # Get text lines and add a newline character after each line
        #     lines = page.get_text("text").splitlines()
        #     for line in lines:
        #         text += line + "\n"
    return text


def write_text_to_docx(text, docx_path):
    document = Document()
    document.add_paragraph(text)
    document.save(docx_path)


###############################################################################


def convert_pdf_to_docx(pdf_path, docx_path, amount_of_pages=-1):
    # Extract text from pdf
    with fitz.open(pdf_path) as pdf_document:
        # Validate amount_of_pages parameter
        if amount_of_pages < -1 or amount_of_pages > len(pdf_document):
            raise ValueError("Invalid amount_of_pages value")

        # If amount_of_pages is -1, extract text from all pages
        pages_to_extract = (
            range(len(pdf_document))
            if amount_of_pages == -1
            else range(amount_of_pages)
        )

        # every blocks
        text = ""
        for page_number in pages_to_extract:
            page = pdf_document[page_number]
            # Get text blocks and add a newline character after each block
            blocks = page.get_text("blocks")
            for block in blocks:
                block_text = block[4]  # block[4] contains the text in the block

                # Check if block_text is not an image metadata
                if not block_text.startswith("<image:"):
                    text += block_text + "\n"

    # Write text to DOCX
    document = Document()
    paragraph = document.add_paragraph(text)

    # run object from the paragraph
    run = paragraph.runs[0]
    run.font.name = FONT_DEFAULT
    run.font.size = Pt(FONT_SIZE)

    # Save DOCX
    document.save(docx_path)


###############################################################################
