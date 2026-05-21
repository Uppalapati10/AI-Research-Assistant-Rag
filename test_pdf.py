from pypdf import PdfReader

reader = PdfReader("data/raw/sample_pdfs/sample.pdf")

print("Pages:", len(reader.pages))