import pathlib,PyPDF2, copy

path = pathlib.Path.cwd()/"half_and_half.pdf"
path2 = pathlib.Path.cwd()/"half_and_half2.pdf"


pdf_reader = PyPDF2.PdfReader(path)

pdf_writer = PyPDF2.PdfWriter()

first_page = pdf_reader.pages[0]
left_side = copy.deepcopy(first_page)
right_side = copy.deepcopy(first_page)

current_coords = left_side.mediabox.upper_right

new_coords = (current_coords[0]/2, current_coords[1])

left_side.mediabox.upper_right = new_coords
right_side.mediabox.upper_left = new_coords


pdf_writer.add_page(left_side)
pdf_writer.add_page(right_side)

with path2.open(mode="wb") as file:
    pdf_writer.write(file)
