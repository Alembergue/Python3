# se = if:
# se não se  = elif : PODE USAR VARIOS ELIF DENTRO DE IF
# se não se  = elif :
# se não = else :

# Desafio 36 emprestimo
print('-=-'*10)
print(' -=-'*2,'BANCO CENTRAL',' -=-'*2)
print('-=-'*10)
import time
casa =     float(input('Qual o valor do imovel? R$'))
salario =  float(input('Qual  a sua renda mensal? R$'))
parcela =  int(input('Em quantos anos?'))
print('Analisando...')
time.sleep(3)
#cores = {'vermelho':'\033[1;31m','verde':'\033[1;32m',
 #        'fim':'\033[m'}
pmensal = casa/(parcela*12)
sal30 = (salario*30)/100

if pmensal > sal30 :
    print('Para pagar a casa de R${:.2f} em {} anos a prestação será de {} \033[1;31mEmpréstimo NEGADO!\033[m'.format(casa,parcela,pmensal))

elif pmensal == sal30 or pmensal < sal30:
    print('Para pagar a casa de R$ {:.2f} a prestação será de R${:.2f} mensais por {} anos.\033[1;32mEmpréstimo APROVADO!\033[m'.format(casa,pmensal,parcela))
    print('Obrigado por escolher o nosso banco,volte sempre!')
print('Tenha um bom dia!')

#37 CALCULADORA CONVERTIDORA
numero = int(input('Digite uma número inteiro:'))

print('Escolha uma das bases de conversão:\n[1] converter para BINÁRIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL')

opção = int(input('Sua opção?'))

if opção == 1 :
      print('{} convertido para BINÁRIO é igual a {}'.format(numero,bin(numero)[2:]))

elif opção == 2 :
      print('{} convertido para OCTAL é igual a {}'.format(numero,oct(numero)[2:]))

elif opção == 3 :
      print('{} convertido para HEXADECIMAL é igual a {}'.format(numero,hex(numero)[2:]))

else :
      print('Opção inválida')


#38 QUEM É MAIOR
a =int(input('Digite um numero :'))
b =int(input('Digite outro numero :'))
if a > b :
    print('O numero {} é MAIOR que o número {}'.format(a,b))
elif a < b :
    print('O numero {} é MAIOR que o número {}'.format(b,a))
else:
    print('Não exite valor maior!os números são IGUAIS!')

#39 ALISTAMENTO
from datetime import date
atual=date.today().year
sexo =str(input('Qual o seu sexo?')).upper().lower()

if sexo == 'feminimo' or sexo == 'mulher':
    print('Você não precisa fazer alistamento militar!')

ano = int(input('Em que ano você nasceu?'))

idade = atual - ano
alistar = 18
alistar1 = atual - (idade-alistar)
alistar2 = atual + (alistar-idade)
anos1 = idade - alistar
anos2 = alistar - idade

if idade > alistar :
    print('Você ainda não se alistou?,já passou \033[1:31m{}\033[m anos,seu alistamento foi em {}'.format(anos1,alistar1))

elif idade == alistar:
    print('Você esta na idade de se alistar!\033[31mcorra para o quartel!\033[m')

elif idade > 5 and idade <= 17:
   print('Quem nasceu em {} tem {} anos em 2022.\nAinda faltam {} anos para você se alistar!\nSeu alistamento será em {}'.format(ano,idade,anos2,alistar2))

else:
    print('\033[1:31mVOCÊ AINDA É UM PIRRALHO!!!,O QUE QUERES AQUI!!! ¬¬\033[m')

#40 MEDIA

nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))

media = (nota1 + nota2)/2

if media < 5:
    print('Sua media foi {:.1f},\033[1;31mREPROVADO!!\033[m'.format(media))

elif media >=5 and media <= 6.99 :
    print('Sua media foi {:.1f},\033[1;33mRECUPERAÇÃO!!\033[m'.format(media))

elif media == 10 :
    print('Parabéns!! sua media foi {:.1f}'.format(media))
else:
    print('Sua media foi {:.1f},\033[1;32mAPROVADO!!\033[m'.format(media))

#41 NATAÇÃO
import time
from datetime import date

print('-=-'*20)
print('-=-'*6,'CONFEDERAÇÃO DE NATAÇÃO','-=-'*5)
print('-=-'*20)

nasceu = int(input('Qual o ano de nascimento?'))
print('PROCESSANDO...')
time.sleep(3)

atual = date.today().year
idade =  atual - nasceu

if idade  <= 9 :
    print('Você tem {} anos,sua categoria é a \033[1;32mMIRIM\033[m'.format(idade))

elif idade > 9 and idade <= 14 :
    print('Você tem {} anos,sua categoria é a \033[1;34mINFANTIL\033[m'.format(idade))

elif idade > 14 and idade <=19 :
    print('Você tem {} anos,sua categoria é a \033[1;33mJUNIOR\033[m'.format(idade))

elif idade > 19 and idade <=25:
    print('Você tem {} anos,sua categoria é a \033[1;36mSÊNIOR\033[m'.format(idade))

else:
    print('Você tem {} anos,sua categoria é a \033[1;35mMASTER\033[m'.format(idade))


#42 TRIANGULOS
lado1 = int(input('Comprimento 1 :'))
lado2 = int(input('Comprimento 2 :'))
lado3 = int(input('Comprimento 3 :'))

tr1 = lado2 + lado3
tr2 = lado1 + lado3
tr3 = lado1 + lado2

if tr1 > lado1 and tr2 > lado2 and tr3 > lado3 :
  print('É possível formar um triângulo,',end ='')

  if lado1 == lado2 == lado3 :
    print('Com as medidas {},{} e {},o triangulo formado é EQUILÁTERO'.format(lado1,lado2,lado3))

  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 :
     print('Com as medidas {},{} e {},o triangulo formado é ISÓCELES'.format(lado1,lado2,lado3))

  else:
     print('Com as medidas {},{} e {},o triangulo formado é ESCALENO'.format(lado1,lado2,lado3))

else:
 print('Não é possível formar um triangulo com estes valores')


#43 IMC
peso = float(input('Qual o seu peso ?(Kg)'))
altura = float(input('Qual a sua altura ?(Cm)'))

imc = peso / (altura*altura)

#ou imc = peso (altura**2)

if imc < 18.5 :
    print('Seu IMC é {:.1f},você esta abaixo do peso ideal'.format(imc))

elif imc >= 18.5 and imc < 25 :
    print('Seu IMC é {:.1f},\033[1;32mPARABÉNS!!você esta no peso ideal\033[m'.format(imc))

elif imc >= 25 and imc < 30 :
    print('Seu IMC é {:.1f},você esta com sobre peso'.format(imc))

elif imc >= 30 and imc < 40 :
    print('Seu IMC é {:.1f},você esta com \033[1;33mOBESIDADE\033[m'.format(imc))

else :
    print('Você esta com obesidade \033[1;31mMORBIDA!CUIDADO!!\033[m')

#44 LOJA
print('{:=^40}'.format('LOJAS BUDEGA'))
valor = float(input('Preço do produto:R$'))
pagamento = str(input('FORMAS DE PAGAMENTO:(Dinheiro,Cheque,Cartão)\nQual a forma de pagamento ?')).upper().lower().strip()

desconto10 = valor - (valor*10/100)
desconto5 = valor - (valor*5/100)
juros20 = valor + (valor*20/100)

if pagamento == 'Cartão' or pagamento == 'cartao':
    parcela = int(input('Em quantas vezes?'))
    if parcela == 1 :
      print('O produto fica com 5% de desconto,custara R${:.2f}'.format(desconto5))

    elif parcela == 2 :
      print('O produto custura R${:.2f}'.format(valor))


    elif parcela >= 3 :
      print('O produto ficara com juros de 20%,o valor final sera de R${:.2f}! '.format(juros20,parcela))

if pagamento == 'dinheiro' or pagamento == 'cheque':
    print('Você fica com 10% de desconto ,o produto custara R${:.2f} '.format(desconto10))

#44 FORMA 2
print('{:=^40}'.format('LOJAS BUDEGA'))

valor = float(input('Preço das compras:R$'))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3]2x no cartão\n[4]3x ou mais no cartão')
pagamento = int(input('Qual a forma de pagamento?'))

desconto10 = valor - (valor*10/100)
desconto5 = valor - (valor*5/100)
juros20 = valor + (valor*20/100)

if pagamento == 4 :

    parcela = int(input('Quantas parcelas'))
    parjuros20 = juros20 / parcela
    if parcela >= 3 :
        print('Sua compra de R${:.2f} será parcelada em {}x de R${:.2f}'.format(valor,parcela,parjuros20))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor,juros20))

if pagamento == 3:
    parcela2 = valor/2
    print('Sua compra de R${:.2f} será parcelada no cartão em 2x de {:.2f} sem juros com valor final de {:.2f}'.format(valor,parcela2,valor))

elif pagamento == 2 :
    print('Sua compra de R${:.2f} a vista no cartão terá um desconto de 5%\nO custo final será de R${:.2f}'.format(valor,desconto5))

elif pagamento == 1:
    print('Sua compra de R${:.2f} a vista no dinheiro/cheque terá um desconto de 10%\nO custo final será de R${:.2f}'.format(valor,desconto10))

else:
    total = valor
    print('Opçao invalida de pagamento.Selecione uma das opções mencionadas no menu')

#45 JOKENPÔ POR ALEMBERGUE
import random
import time

print('{:=^40}'.format('JOKENPÔ'))

print('OPÇÕES\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA')

itens = ('PEDRA','PAPEL','TESOURA')

jogador = int(input('Qual é sua jogada ?'))
maquina = random.randint(0,2)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!')

if   jogador == 0 and maquina == 1 :
      print('JOGADOR = {}\nMAQUINA = {}\nMAQUINA VENCEU!!'.format(itens[jogador],itens[maquina]))

elif jogador == 0 and maquina == 2 :
      print('JOGADOR = {}\nMAQUINA = {}\nJOGADOR VENCEU!'.format(itens[jogador],itens[maquina]))

elif jogador == 1 and maquina == 0 :
      print('JOGADOR = {}\nMAQUINA = {}\nJOGADOR VENCEU!!'.format(itens[jogador],itens[maquina]))

elif jogador == 1 and maquina == 2 :
      print('JOGADOR = {}\nMAQUINA = {}\nMAQUINA VENCEU!!'.format(itens[jogador],itens[maquina]))

elif jogador == 2 and maquina == 1 :
      print('JOGADOR = {}\nMAQUINA = {}\nJOGADOR VENCEU!!'.format(itens[jogador],itens[maquina]))

elif jogador == 2 and maquina == 0 :
      print('JOGADOR = {}\nMAQUINA = {}\nMAQUINA VENCEU!!'.format(itens[jogador],itens[maquina]))

elif jogador > 2 :
      print('Esta opção não é valida! tente uma das opções mencionadas nas instruções!')
else:
     print('JOGADOR = {}\nMAQUINA = {}\nEMPATAMOS!!'.format(itens[jogador],itens[maquina]))

#45 JOKENPO PELO CURSO
