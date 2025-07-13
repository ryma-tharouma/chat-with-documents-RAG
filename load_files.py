""" This module provides functions to load various document types such as PDF, PowerPoint, and Word documents."""

from langchain_community.document_loaders import PDFMinerLoader
from langchain_community.document_loaders import UnstructuredPowerPointLoader
from langchain_community.document_loaders import UnstructuredWordDocumentLoader


def load_pdf(file_path):
    """Load a PDF file using PDFMinerLoader."""
    loader =PDFMinerLoader(file_path)
    return loader.load()

def load_pptx(file_path):
    """Load a PowerPoint file using UnstructuredPowerPointLoader."""
    loader = UnstructuredPowerPointLoader(file_path)
    return loader.load()

def load_docx(file_path):
    """Load a Word document using UnstructuredWordDocumentLoader."""
    loader = UnstructuredWordDocumentLoader(file_path)
    return loader.load()

def get_docs(files_dir):
    """Load documents from a directory."""
    docs = []
    for file_path in files_dir:
        file_path.lower()
        if file_path.endswith('.pdf'):
            docs.extend(load_pdf(file_path))
        elif file_path.endswith('.pptx'):
            docs.extend(load_pptx(file_path))
        elif file_path.endswith('.docx'):
            docs.extend(load_docx(file_path))
    return docs





