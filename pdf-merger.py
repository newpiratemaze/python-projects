import pathlib,PyPDF2

path1 = pathlib.Path.cwd()/"merge1.pdf"
path2 = pathlib.Path.cwd()/"merge2.pdf"
path3 = pathlib.Path.cwd()/"merge3.pdf"
path = pathlib.Path.cwd()/"concatenated.pdf"
path4 = pathlib.Path.cwd()/"merged.pdf"


pdf_merger = PyPDF2.PdfMerger()

pdf_merger.append(path1)
pdf_merger.append(path2)

with path.open(mode="wb") as file:
    pdf_merger.write(file)

pdf_merger2 = PyPDF2.PdfMerger()

pdf_merger2.append(path)

pdf_merger2.merge(1,path3)

with path4.open(mode="wb") as file:
    pdf_merger2.write(file)
