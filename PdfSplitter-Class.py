import pathlib, PyPDF2

class PdfSplitter():
    def __init__(self,filename):
        self.filename = filename
        self.path = pathlib.Path.cwd()/filename
        self.reader = PyPDF2.PdfReader(self.path)
        self.writer1 = PyPDF2.PdfWriter()
        self.writer2 = PyPDF2.PdfWriter()

    def split(self,breakpoint):
        pages1 = self.reader.pages[:breakpoint]
        pages2 = self.reader.pages[breakpoint:]

        for page in pages1:
            self.writer1.add_page(page)

        for page in pages2:
            self.writer2.add_page(page)

    def write(self,new_filename):
        with pathlib.Path(new_filename+"_1.pdf").open(mode="wb") as file:
            self.writer1.write(file)

        with pathlib.Path(new_filename+"_2.pdf").open(mode="wb") as file:
            self.writer2.write(file)


pdf_splitter = PdfSplitter("Pride_and_Prejudice.pdf")
pdf_splitter.split(135)
pdf_splitter.write("pride_split")
