from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class Report:
    def __init__(self, name, phoneNumber, address, reason, formatFile = "diet.pdf", reportFile = "report.pdf", font='Helvetica-Bold'):
        self.name = name
        self.phoneNumber = phoneNumber
        self.address = address
        self.reason = reason
        self.formatFile = formatFile
        self.reportFile = reportFile
        self.font = font
        self.startX = 50
        self.startY = 642

    def split(self, string, splitBy=17):
        if len(string) < splitBy:
            return [string]
        else:
            return [string[:splitBy]] + self.split(string[splitBy:], splitBy)


    def make(self):
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont(self.font, 20)
        can.drawString(self.startX, self.startY, self.name)
        self.startY-=47
        can.drawString(self.startX, self.startY, self.phoneNumber)
        self.startY-=50
        for i in self.split(self.address):
            can.drawString(self.startX, self.startY, i)
            self.startY-=25
        self.startY-=50
        can.setFont(self.font, 25)
        can.drawString(30, self.startY, self.reason)
        can.showPage()
        can.save()

        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        existing_pdf = PdfFileReader(open(self.formatFile, "rb"))
        output = PdfFileWriter()
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        page = existing_pdf.getPage(1)
        page.mergePage(new_pdf.getPage(1))
        output.addPage(page)

        outputStream = open(self.reportFile, "wb")
        output.write(outputStream)
        outputStream.close()

