# reversing copying deleting pages

#  pip install pikepdf

import pikepdf

old_pdf=pikepdf.Pdf.open("Pinkush report.pdf")

def reverse():
    old_pdf.pages.reverse()
    old_pdf.save("nr.pdf")

# reverse()
def PageIndexChange():
    old_pdf.pages[1]=old_pdf.pages[6]
    old_pdf.save("PageIndexChange.pdf")

PageIndexChange()

def deletePage():
    del old_pdf.pages[1:3]
    old_pdf.save("deltepage.pdf")

# deletePage()