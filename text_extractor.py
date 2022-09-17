import PyPDF2

Pdf_file=open("Sample.pdf","rb")
Pdf_reader=PyPDF2.PdfFileReader(Pdf_file)
Text=Pdf_reader.getPage(0).extract_text()
print(Text)