import PyPDF2
import requests

# URL of the paper's PDF (replace with actual URL)
pdf_url = 'https://arxiv.org/pdf/2301.09856.pdf'

# Download the PDF file
response = requests.get(pdf_url)
with open('paper.pdf', 'wb') as f:
    f.write(response.content)

# Open and read the PDF
with open('paper.pdf', 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    # Loop through pages and extract text
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()
        print(text)  # Or store the text for later processing
