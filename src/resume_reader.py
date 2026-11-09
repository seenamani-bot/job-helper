# resume_reader.py - gets the plain text out of a resume file.
# Everything here runs on your computer. Nothing is sent anywhere.

from pathlib import Path

from docx import Document   # reads Word files
from pypdf import PdfReader  # reads PDF files


def read_pdf(path):
    # Open the PDF and join the text of every page.
    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages)


def read_docx(path):
    # Open the Word file and collect the text line by line.
    document = Document(path)
    lines = []

    # Normal paragraphs.
    for paragraph in document.paragraphs:
        lines.append(paragraph.text)

    # Text inside tables (some resumes use tables for layout).
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                lines.append(cell.text)

    return "\n".join(lines)


def read_resume(path):
    # Pick the right reader based on the file ending.
    suffix = Path(path).suffix.lower()
    if suffix == ".pdf":
        return read_pdf(path)
    if suffix == ".docx":
        return read_docx(path)
    raise ValueError("Please use a .pdf or .docx file.")
