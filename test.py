from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from StringIO import StringIO

#register font
pdfmetrics.registerFont(TTFont('fonta', 'always forever.ttf'))

imgTemp = StringIO()
imgDoc = canvas.Canvas(imgTemp)

imgPath = 'signature.png'
imgDoc.drawImage(imgPath, 260, 100, 160, 40)
imgDoc.setFont('fonta', 30)
imgDoc.drawString(260, 60, 'moveha')
imgDoc.save()

page = PdfFileReader(file('input.pdf', 'rb')).getPage(0)
overlay = PdfFileReader(StringIO(imgTemp.getvalue())).getPage(0)
page.mergePage(overlay)
output = PdfFileWriter()
output.addPage(page)
output.write(file('output.pdf', 'w'))
