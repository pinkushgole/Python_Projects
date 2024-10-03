# pip install pdf2image
# Poppler 24.07.0 : user read and write operation on pdf file

from pdf2image import convert_from_path
poppler_path=r'D:\Django\Python\PdfToImage\poppler-24.07.0\Library\bin'

images = convert_from_path('Pinkush.pdf', poppler_path=poppler_path)

# Save each page as a JPEG image
for i, image in enumerate(images):
    image.save(f"new_{i}.jpg", "JPEG")


