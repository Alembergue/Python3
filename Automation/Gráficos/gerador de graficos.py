import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, Button, filedialog
from openpyxl import Workbook

def carregar_planilha():
    # Abre um diálogo para selecionar a planilha
    file_path = filedialog.askopenfilename(title="Selecionar Planilha", filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        processar_planilha(file_path)

def processar_planilha(file_path):
    # Lê a planilha
    df = pd.read_excel(file_path)

    # Cria um relatório simples
    relatorio = df.describe()

    # Cria um gráfico (exemplo: gráfico de barras do valor médio de cada coluna)
    plt.figure(figsize=(10, 6))
    relatorio.loc['mean'].plot(kind='bar')
    plt.title('Média dos Valores')
    plt.ylabel('Valores Médios')
    plt.xticks(rotation=45)
    
    # Salva o gráfico
    plt.savefig('grafico.png')
    plt.close()

    # Cria um novo arquivo Excel para o relatório
    wb = Workbook()
    ws = wb.active
    ws.title = "Relatório"

    # Adiciona o resumo ao relatório
    for r_idx, row in enumerate(relatorio.iterrows(), 1):
        for c_idx, value in enumerate(row[1], 1):
            ws.cell(row=r_idx, column=c_idx, value=value)

    # Adiciona o gráfico
    ws.add_image('grafico.png', 'E5')

    # Salva o relatório
    wb.save('relatorio.xlsx')

    print("Relatório gerado com sucesso: relatorio.xlsx")

def criar_interface():
    root = Tk()
    root.title("Gerador de Relatório Excel")

    btn_carregar = Button(root, text="Carregar Planilha", command=carregar_planilha)
    btn_carregar.pack(pady=20)

    root.geometry("300x200")
    root.mainloop()

if __name__ == "__main__":
    criar_interface()
