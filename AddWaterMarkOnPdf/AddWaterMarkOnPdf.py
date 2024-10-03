# pip install pikepdf

from pikepdf import Pdf,Page,Rectangle

old_pdf=Pdf.open("Pinkush.pdf")
old_pdf1=Pdf.open("m1.pdf")

des_page=Page(old_pdf.pages[0])
sor_page=Page(old_pdf1.pages[0])

des_page.add_overlay(sor_page,Rectangle(0,0,500,500))

old_pdf.save("new_pdf.pdf")