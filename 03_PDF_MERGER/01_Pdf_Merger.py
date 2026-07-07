from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []             # Initially the list is kept empty.

n = int(input("How many pdfs you want to merge? \n"))       # User enters the number of PDFs to merge, we get an Idea of how many PDFs to append.

for i in range (0, n):    
    name = input(f"Enter the name of PDF {i + 1}: ")
    pdfs.append(name)         # Example : User wants to merge 2 pdfs therefore, ['A.pdf', 'B.pdf'] goes into the list, pdfs [ ] at line 5.

for pdf in pdfs:
    merger.append(pdf)

merger.write("New_Merged.pdf")
merger.close()