

import pikepdf

old_pdf=pikepdf.Pdf.open("Pinkush.pdf")

# print(old_pdf.pages)

for i in old_pdf.pages:
    i.Rotate=90
    old_pdf.save("new_rotate90.pdf")