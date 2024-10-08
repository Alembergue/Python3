import PyPDF2
import os                                      

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if".pdf" in arquivo :
        merger.append(f"arquivos/{arquivo}")

merger.write ("PDF Final.pdf")