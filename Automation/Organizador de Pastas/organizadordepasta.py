import os                                                                         #  biblioteca
from tkinter.filedialog import askdirectory                                       #  Função da biblioteca para abrir pop up para escolher a pasta

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {                                                                       # lista de pastas que serão criadas após roda o código

    "imagens" : [".png",".jpg",".tif"],
    "planilhas" : [".xlsx"],
    "pdfs" : [".pdf"],
    "word" : [".docx"],
    "zipados" : [".zip"],

}


for arquivo in lista_arquivos :

    nome,extensao = os.path.splitext(f"{caminho}/{arquivo}")                     
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}",f"{caminho}/{pasta}/{arquivo}")