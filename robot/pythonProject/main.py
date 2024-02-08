import time

import clipboard
import pyautogui
from pymsgbox import prompt

pyautogui.hotkey('alt', 'tab')
time.sleep(0.5)
pyautogui.hotkey('alt', 'm')
time.sleep(0.5)
pyautogui.write('Peticao inicial')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

#Entrada dos Dados

#Valor Total da CDA
valorDaCDA = prompt(text='VALOR TOTAL DA CDA', title='CDA', default='R$')
valorFormatado = valorDaCDA.replace("[.,]" ,"")
time.sleep(1)

#Numero da CDA
numeroDaCda = prompt(text='NUMERO CDA', title='CDA', default='')
time.sleep(1)

#Data de Origem
dataDeOrigem = prompt(text='Data da Origem', title='CDA', default='')
# Entrada de dados Fim
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.click(x=1071, y=397)

time.sleep(1)
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
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('r')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
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
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('e')

for classeProcessual in range(0, 6):
    pyautogui.press('down')

pyautogui.press('enter')

time.sleep(3)

for toValorTotal in range(0, 3):
    pyautogui.press('tab')


#valor total da cda
clipboard.copy(valorFormatado)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)

pyautogui.press('enter')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
clipboard.copy(numeroDaCda)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('i')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
clipboard.copy(dataDeOrigem)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('end')