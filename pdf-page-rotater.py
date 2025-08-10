import pathlib,PyPDF2

path = pathlib.Path.cwd()/"ugly.pdf"
path2 = pathlib.Path.cwd()/"ugly2.pdf"

pdf_reader = PyPDF2.PdfReader(path)
pdf_writer = PyPDF2.PdfWriter()

for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    rotate = page["/Rotate"]
    page.rotate(-1*int(rotate))
    pdf_writer.add_page(page)

with path2.open(mode="wb") as file:
    pdf_writer.write(file)
