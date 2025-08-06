from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []

n = int(input("no of pdfs to merge?: \n"))
for i in range(0,n):
    name = input(f"enter the name of pdf {i + 1} : ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()