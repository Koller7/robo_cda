import re

import pdfplumber
from PyPDF2 import PdfReader

with pdfplumber.open("C:/Users/gabriel.9161/Downloads/CDA/peticao.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text()


print(text)

valorTotal_re = re.compile(r'^\d{3} [A-Z].*')

for linha in text.split('\n'):
    if valorTotal_re.match(linha):
        print(linha)