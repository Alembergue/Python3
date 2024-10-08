# Envio do e-mail com o relatório em anexo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from fpdf import FPDF
import datetime

def coletar_dados():
    empresa = input("Empresa: ")
    local = input("Local: ")
    data = datetime.datetime.now().strftime("%d/%m/%Y")
    topicos_treinamento = input("Tópicos do treinamento: ")

    participantes = []
    while True:
        participante = input("Nome do participante (ou 'sair' para encerrar): ")
        if participante.lower() == 'sair':
            break
        assinatura = input(f"Assinatura {participante}: ")
        data_assinatura = input(f"Data  {participante}: ")
        participantes.append({
            "nome": participante,
            "assinatura": assinatura,
            "data_assinatura": data_assinatura
        })

    instrutor = input("Nome do Instrutor: ")
    assinatura_instrutor = input("Assinatura do Instrutor: ")
    testemunha = input("Nome da Testemunha/Observador: ")
    assinatura_testemunha = input("Assinatura da Testemunha/Observador: ")

    dados = {
        "empresa": empresa,
        "local": local,
        "data": data,
        "topicos_treinamento": topicos_treinamento,
        "participantes": participantes,
        "instrutor": instrutor,
        "assinatura_instrutor": assinatura_instrutor,
        "testemunha": testemunha,
        "assinatura_testemunha": assinatura_testemunha
    }
    return dados

# Geração do relatório em PDF padronizado com tabelas e bordas
def gerar_pdf(dados):
    pdf = FPDF()
    pdf.add_page()

    # Título principal
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(190, 10, txt="+ Perfomance - Análise Estratégica", ln=True, align="C", border=1)
    pdf.cell(190, 10, txt="Registro de Treinamentos (Grupo)", ln=True, align="C", border=1)
    pdf.ln(10)

    # Dados gerais: Empresa, Local e Data
    pdf.set_font("Arial", size=10)
    pdf.cell(130, 8, txt=f"Empresa: {dados['empresa']}", border=1)
    pdf.cell(60, 8, txt=f"Data: {dados['data']}", border=1, ln=True)
    pdf.cell(190, 8, txt=f"Local: {dados['local']}", border=1, ln=True)
    pdf.ln(5)

    # Tópicos e Comentários
    pdf.cell(190, 8, txt="Tópicos do Treinamento:", border=1, ln=True)
    pdf.multi_cell(190, 8, dados['topicos_treinamento'], border=1)

    # Lista de Participantes com Assinaturas
    pdf.cell(63, 8, txt="Nome do Participante", border=1, align='C')
    pdf.cell(63, 8, txt="Assinatura", border=1, align='C')
    pdf.cell(64, 8, txt="Data da Assinatura", border=1, align='C', ln=True)

    for p in dados['participantes']:
        pdf.cell(63, 8, txt=p['nome'], border=1)
        pdf.cell(63, 8, txt=p['assinatura'], border=1)
        pdf.cell(64, 8, txt=p['data_assinatura'], border=1, ln=True)

    pdf.ln(5)

    # Assinaturas: Instrutor e Testemunha
    pdf.cell(95, 8, txt=f"Instrutor: {dados['instrutor']}", border=1)
    pdf.cell(95, 8, txt=f"Assinatura: {dados['assinatura_instrutor']}", border=1, ln=True)
    pdf.cell(95, 8, txt=f"Testemunha: {dados['testemunha']}", border=1)
    pdf.cell(95, 8, txt=f"Assinatura: {dados['assinatura_testemunha']}", border=1, ln=True)

    # Nome do arquivo com a data
    nome_arquivo = f"registro_treinamento_{dados['data'].replace('/', '-')}.pdf"
    pdf.output(nome_arquivo)
    return nome_arquivo

# Envio do e-mail com o relatório em anexo
def enviar_email(arquivo_pdf, destinatario):
    remetente = "xxxxx@yahoo.com.br"
    senha = "ajkzyvevcotgvhzc"

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = "Relatório Diário de Obras"

    corpo_email = "Segue em anexo o relatório diário das atividades de obras."
    msg.attach(MIMEText(corpo_email, 'plain'))

    with open(arquivo_pdf, "rb") as attachment:
        part = MIMEApplication(attachment.read(), _subtype="pdf")
        part.add_header('Content-Disposition', 'attachment', filename=arquivo_pdf)
        msg.attach(part)

    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.starttls()
    server.login(remetente, senha)
    text = msg.as_string()
    server.sendmail(remetente, destinatario, text)
    server.quit()

# Exemplo de execução
dados_diarios = coletar_dados()
arquivo_pdf = gerar_pdf(dados_diarios)
enviar_email(arquivo_pdf, "xxxxx@yahoo.com.br")
enviar_email(arquivo_pdf, "xxxxx@hotmail.com")

print("Relatório diário gerado e enviado com sucesso!")