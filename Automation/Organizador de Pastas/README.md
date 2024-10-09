
# BIBLIOTECAS NECESSÁRIAS:

pip install pandas

pip install pywin32

pip install openpyxl

# Criar o arquivo .exe a partir do ambiente virtual para que fique mais compacto

pyintaller --onefile nomedoarquivo.py

pyintaller --onefile -w [se o usuario necessita de interação com telas] nomedoarquivo.py