import PyPDF2, pathlib

path1 = pathlib.Path.cwd()/"newsletter.pdf"
path2 = pathlib.Path.cwd()/"newsletter_protected.pdf"

pdf_reader = PyPDF2.PdfReader(path1)

pdf_writer = PyPDF2.PdfWriter()

pdf_writer.append_pages_from_reader(pdf_reader)

pdf_writer.encrypt(user_password="SuperSecret", owner_password="ReallySuperSecret") // <- set up your user and owner passwords here

with path2.open(mode="wb") as file:
    pdf_writer.write(file)
