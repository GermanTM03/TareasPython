import PyPDF2
import requests
from io import BytesIO

url = "https://uploads-ssl.webflow.com/61f81854791665a201a9c4b6/6267170a273ffa33b0064b4f_Examen-Python.pdf"
response = requests.get(url)
pdf_data = BytesIO(response.content)
pdf_reader = PyPDF2.PdfReader(pdf_data)
num_pages = len(pdf_reader.pages)

for page_num in range(num_pages):
    page = pdf_reader.pages[page_num]
    page_text = page.extract_text()
    print(page_text)
