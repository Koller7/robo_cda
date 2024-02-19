import time

import clipboard
import pyautogui
from pymsgbox import *


#volta para o navegador

pyautogui.hotkey('alt', 'tab')
time.sleep(0.5)

# faz a pesquisa no site do EPROC

pyautogui.hotkey('alt', 'm')
time.sleep(0.5)
pyautogui.write('Peticao inicial')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)

#Entrada dos Dados

# tipo da cda

resposta = confirm(text='', title='', buttons=['IPTU', 'TLLF', 'ISSQN'])


#Valor Total da CDA

valorTotalDaCDA = prompt(text='VALOR DA CAUSA', title='CDA', default='')
valorFormatado = valorTotalDaCDA.replace("[R$., ]" ,"")


#Numero da CDA

numeroDaCda = prompt(text='NUMERO CDA', title='CDA', default='')


#Data de Origem

dataDeOrigem = prompt(text='Data da Origem', title='CDA', default='')

# Valor da Causa

valorDaCausa = prompt(text='Valor da CDA', title='CDA', default='')


# Volta para o Site do EPROC e clica no meio da Tela

# pyautogui.hotkey('alt', 'tab')
time.sleep(0.5)
pyautogui.hotkey('alt', 'tab')
pyautogui.click(x=1572, y=429)
time.sleep(0.5)

#Acessa o Campo de Ação que seleciona o Municipio

pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('s')
time.sleep(0.5)

for municipio in range(0, 18):
    pyautogui.press('down')

pyautogui.press('enter')
time.sleep(0.5)

#Acessa o Campo do Rito

pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('r')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)

#Acessa o Campo da Área

pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('f')
time.sleep(0.5)
pyautogui.press('down')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)

#Acessa o Campo da Classe Processual
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('e')

for classeProcessual in range(0, 6):
    pyautogui.press('down')

pyautogui.press('enter')
time.sleep(3)

# Pula três campos abaixos desnecessarios e coloca o valor total da CDA

for toValorTotal in range(0, 3):
    pyautogui.press('tab')

clipboard.copy(valorFormatado)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

#acessa a aba de adicionar CDA
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)

#Acessa o Campo do Numero da CDA
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
clipboard.copy(numeroDaCda)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

# pula o numero administrativo

pyautogui.press('tab')
time.sleep(0.5)

# Marca o Tributo Fiscal como DIV.ATIVA-IPTU

pyautogui.press('tab')
time.sleep(0.5)
if resposta == 'IPTU':
    for x in range(0, 7):
        pyautogui.press('down')

elif resposta == 'TLLF':
    for x in range(0, 18):
        pyautogui.press('down')

elif resposta == 'ISSQN':
    for x in range(0, 9):
        pyautogui.press('down')
time.sleep(0.5)

# Acessa a Data de Origem

pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
clipboard.copy(dataDeOrigem)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

# Acessa o Campo de Status da CDA
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('end')

# Acessa o Campo de Valor da CDA

pyautogui.press('tab')
time.sleep(0.5)
clipboard.copy(valorDaCausa)
pyautogui.hotkey('ctrl', 'v')

# Inclui a CDA e salva

pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)


# Proxima Etapa

#pyautogui.hotkey('alt', 'tab') se forem duas telas
pyautogui.click(x=1572, y=429)
for x in range(0, 11):
    pyautogui.press('tab')
    time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)

# 2 / 5 Assuntos

#Acessa o Campo do Assunto
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
if resposta == 'IPTU':
    time.sleep(1)
    pyautogui.write('IPTU')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.moveTo(214, 478)
    time.sleep(1)
    pyautogui.click()
elif resposta == 'ISSQN':
    time.sleep(1)
    pyautogui.write('Imposto Sobre Servicos')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.moveTo(201, 478)
    time.sleep(1)
    pyautogui.click()

elif resposta == 'TLLF':
    time.sleep(1)
    pyautogui.write('Taxa de Licenciamento de Estabelecimento')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.moveTo(266, 499)
    time.sleep(1)
    pyautogui.click()

time.sleep(0.5)

# Inclui o Assunto
for x in range(0, 5):
    pyautogui.press('tab')
    time.sleep(0.5)
pyautogui.press('enter')
time.sleep(1)

# Avança 3 / 5 Parte Autora

pyautogui.moveTo(1773, 647)
time.sleep(1)
pyautogui.click()
time.sleep(1)

# Seleciona a Entidade

pyautogui.press('tab')
time.sleep(1)
pyautogui.press('down')

# faz a inclusão da entidade

pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

#vai para o prox campo

for x in range(0, 6):
    pyautogui.press('tab')
    time.sleep(0.5)
time.sleep(1)
pyautogui.press('enter')

# Tipo de pessoa

tipoDePessoa = confirm(text='Selecione o Tipo de Pessoa', title='', buttons=['PESSOA FISICA', 'PESSOA JURIDICA'])

if tipoDePessoa == 'PESSOA FISICA':
    cpf = prompt(text='Digite o CPF', title='CPF', default='')
    #pyautogui.hotkey('alt', 'tab') se for uma tela só tirar o comentario dessas duas linhas
    #pyautogui.hotkey('alt', 'tab') X
    clipboard.copy(cpf)
    time.sleep(0.5)
    pyautogui.click(327,305)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')

else:
    cnpj = prompt(text='Digite o CNPJ', title='CNPJ', default='')
    clipboard.copy(cnpj)
    time.sleep(0.5)
    pyautogui.click(327, 305)
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')

for x in range(0, 5):
    pyautogui.press('tab')
    time.sleep(0.5)
pyautogui.press('enter')

for x in range(0, 10):
    pyautogui.press('tab')
    time.sleep(0.5)

pyautogui.press('enter')

for x in range(0, 6):
    pyautogui.press('tab')
    time.sleep(0.5)
pyautogui.press('enter')

pyautogui.alert('PROCESSO CONCLUIDO')
