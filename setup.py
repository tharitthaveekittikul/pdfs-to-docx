from setuptools import setup, find_packages

setup(
    name="pdfs-to-docx",
    version="0.1",
    packages=find_packages(),
    install_requires=["python-docx>=0.8.11", "PyMuPDF>=1.23.4", "PyMuPDFb>=1.23.3"],
    author="Tharit Thaveekittikul",
    author_email="tharit.thaveekittikul@gmail.com",
)
