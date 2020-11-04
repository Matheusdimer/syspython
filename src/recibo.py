from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import os
from sys import platform

def gerarRecibo(arquivo, itens, total, title=None, cabecalho=None):
    nLinhas = len(itens)
    height = 200 + 15 * nLinhas
    width = 290
    pdf = canvas.Canvas(f"{arquivo}.pdf", pagesize=[width, height])
    pdf.setFontSize(size=8)
    pdf.setFillColor(HexColor("#eef2bb"))
    path = pdf.beginPath()
    path.moveTo(0, 0)
    path.lineTo(0, height)
    path.lineTo(width, height)
    path.lineTo(width, 0)
    #this creates a rectangle the size of the sheet
    pdf.drawPath(path,True,True)

    pdf.setFillColor(HexColor("#1c1c1c"))
    if cabecalho:
        pdf.drawString(10, height-30, f"Nome: {cabecalho[0]}")
        pdf.drawString(10, height-45, f"CPF : {cabecalho[1]}")
        pdf.drawString(10, height-60, f"Data: {cabecalho[2]}")
    
    y = height - 100
    pdf.drawString(95, y, "RECIBO DE PAGAMENTO")
    
    y -= 20
    pdf.drawString(10, y, "COD")
    pdf.drawString(40, y, "DESCRIÇÃO")
    pdf.drawString(140, y, "UNID.")
    pdf.drawString(190, y, "QUANT")
    pdf.drawString(230, y, "TOTAL")
    
    for linha in itens:
        y -= 15
        pdf.drawString(10, y, linha[0])
        pdf.drawString(40, y, linha[1])
        pdf.drawString(140, y, f"R$ {linha[2]:.2f}".replace(".", ","))
        pdf.drawString(190, y, str(linha[3]))
        pdf.drawString(230, y, f"R$ {linha[4]:.2f}".replace(".", ","))
    
    y -= 20
    pdf.drawString(190, y, "TOTAL:")
    pdf.drawString(230, y, f"R$ {total:.2f}".replace(".", ","))

    y -= 30
    pdf.setFontSize(size=6)
    pdf.drawString(90, y, "Empresa fictícia de comércio de produtos")

    if title:
        pdf.setTitle(title)
    pdf.save()
    os.replace(f"./{arquivo}.pdf", f"./recibos/{arquivo}.pdf")
    if platform == "linux":
        os.system(f"xdg-open ./recibos/{arquivo}.pdf")
    else: 
        os.system(f"start ./recibos/{arquivo}.pdf")
"""
lista = [
    ["0005", "Cola Tenaz", 2.90, "10", 5000.00],
    ["0005", "Cola Tenaz", 45.60, "10", 29.00],
    ["0005", "Cola Tenaz", 12.90, "10", 29.00],
    ["0005", "Cola Tenaz", 24.89, "10", 29.00],
    ["0005", "Cola Tenaz", 32.50, "10", 29.00]
]

gerarRecibo("pdfTeste", lista, 5500.96,cabecalho=["Matheus de Lima Dimer", "052.012.110-46", "30/10/2020"])
"""
