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
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

#Entrada dos Dados

# tipo da cda

resposta = confirm(text='', title='', buttons=['IPTU', 'TLFF', 'ISSQN', 'TAXA'])

#Valor Total da CDA

valorTotalDaCDA = prompt(text='VALOR TOTAL DA CDA', title='CDA', default='')
valorFormatado = valorTotalDaCDA.replace("[R$., ]" ,"")
time.sleep(1)

#Numero da CDA

numeroDaCda = prompt(text='NUMERO CDA', title='CDA', default='')
time.sleep(1)

#Data de Origem

dataDeOrigem = prompt(text='Data da Origem', title='CDA', default='')
time.sleep(1)

# Valor da Causa

valorDaCausa = prompt(text='Valor da CDA / CAUSA', title='CDA', default='')
time.sleep(1)

# Volta para o Site do EPROC e clica no meio da Tela

pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.click(x=1572, y=429)
time.sleep(1)

#Acessa o Campo de Ação que seleciona o Municipio

pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('s')
time.sleep(1)

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
time.sleep(1)

#acessa a aba de adicionar CDA
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

#Acessa o Campo do Numero da CDA
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
clipboard.copy(numeroDaCda)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# pula o numero administrativo

pyautogui.press('tab')
time.sleep(1)

# Marca o Tributo Fiscal como DIV.ATIVA-IPTU

pyautogui.press('tab')
time.sleep(1)
if resposta == 'IPTU':
    for x in range(0, 7):
        pyautogui.press('down')
elif resposta == 'TLFF':
    for x in range(0, 6):
        pyautogui.press('down')
elif resposta == 'ISSQN':
    for x in range(0, 9):
        pyautogui.press('down')
elif resposta == 'TAXA':
        pyautogui.press('end')
time.sleep(1)

# Acessa a Data de Origem

pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
clipboard.copy(dataDeOrigem)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Acessa o Campo de Status da CDA
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('end')

# Acessa o Campo de Valor da CDA

pyautogui.press('tab')
time.sleep(1)
clipboard.copy(valorDaCausa)
pyautogui.hotkey('ctrl', 'v')

# Inclui a CDA e salva

pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)


# Proxima Etapa

pyautogui.hotkey('alt', 'tab')
pyautogui.click(x=1572, y=429)
for x in range(0, 10):
    pyautogui.press('tab')

pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.click(x=1572, y=429)
time.sleep(1)
pyautogui.click('Impostos')
