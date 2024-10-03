# pip install pickpdf

import pikepdf

old_pdf=pikepdf.Pdf.open("Pinkush.Pdf")

no_extr=pikepdf.Permissions(extract=False)

old_pdf.save("lock.pdf",
             encryption=pikepdf.Encryption(user="12345",
                                           owner="wscube",
                                           allow=no_extr))