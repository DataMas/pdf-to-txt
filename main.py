import PyPDF2
import codecs

pdffileobj = open('test.pdf', 'rb')

pdfreader = PyPDF2.PdfFileReader(pdffileobj)

x = pdfreader.numPages
print(x)

pdffileobj = pdfreader.getPage(x-1)

text = pdffileobj.extractText()
print(text)

with open("results.txt", "w",  encoding='utf-8') as fh:
    fh.write(text)