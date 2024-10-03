#  pip install pdf2docx ->conver pdf file into word file
#  pip install docx2pdf ->conver word file into pdf file

from pdf2docx import Converter

old_pdf="Pinkush.pdf"
new_docx="new_word.docx"

obj=Converter(old_pdf)
obj.convert(new_docx)
obj.close

from docx2pdf import convert
convert("new_word.docx","newpdf.pdf")