from pickle import FALSE, TRUE
from time import sleep
from turtle import ht
import pyautogui
import pyperclip
import os 
import subprocess
import time
import re
import codecs
pyautogui.PAUSE = 1 # Define 1 segundo de pausa entre um comando e outro do pyautogui



# Abre qualquer programa que esteja no windows (Forma Simples)
def openProgram(programName, isOpen):
    if( isOpen ):
        pyautogui.hotkey('Alt','Tab')
    else:
        pyautogui.press('win')
        pyautogui.write(programName)
        pyautogui.press('enter')

# Abre qualquer programa que esteja no windows e que seja previamente declarado (Forma complexa)
def openProgramFromSystem():
    program = os.path.join('C:\\','Program Files (x86)', 'Microsoft','Edge','Application','msedge.exe')     # Localizar o .exe do programa
    os.system('taskkill /im msedge.exe')    # Opcional: Encerrar possivel processo que ja esteja rodando
    subprocess.call([CHROME, '--kiosk'])    # Executar a chamada

# Copia e cola o link de forma correta na base de pesquisa
def copyPast():
    pyperclip.copy("https://www.youtube.com/playlist?list=PLtKC7DBHMLR6nA31a6BR-Cw730qnk1hZo") 
    pyautogui.hotkey('ctrl','v')
    pyautogui.press("enter")
    time.sleep(5)   # Tempo de espera para a pagina web carregar 

# Salvar HTML da pagina na aba de dowload 
def saveHTMLfromYoutube():
    pyautogui.rightClick(1427,195)
    pyautogui.click(1511,295)
    pyautogui.write("page")
    for i in range(3): 
        pyautogui.press('Tab')
    pyautogui.press('enter')
    
    '''
    # Funciona quando o download vai por padrao pra area de trabalho
    time.sleep(0.5)
    for i in range(9): 
        pyautogui.press('Tab')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('Tab')
    pyautogui.press('down')
    for i in range(4): 
        pyautogui.press('Tab')
    pyautogui.press('enter')
    '''

# Abre o arquivo HTML e salva ele em uma variavel 
def getLinks():
    arquivo = codecs.open("page.html", "r", "utf-8")
    html = arquivo.read()    
    return html
    

# Filtra em todo HTML passado, os links das musicas 
def saveLinks(html):
    index = save = controle = 0
    links = []
    while controle < len(html):
        index = html.find('https://www.youtube.com/watch', index)
        save = index
        newLink = html[index]
        while save < len(html):
            if html[save] != '"':
                newLink += html[save]
                save += 1
            else:
                index = save
                break
        print(index)
    print(links)


def getManualData(execute):
    if execute:
        openProgram("Chrome", 1)
        pyautogui.hotkey("ctrl", "t")   # Abrir nova guia do google chrome
        copyPast()
        saveHTMLfromYoutube() # Executar apenas uma vez

# 1. Entrar no local  onde se encontra os dados da empresa (Link do drive os dados são atualizados diariamente)
def start():
    #getManualData(FALSE)
    saveLinks(getLinks())

    
    
start()  

# 2. Navegar no local e encontrar o arquivo desejado
# 3. Fazer o download da base de vendas
# 4. Importar a base de vendas para o Python
# 5. Calcular o faturamento e quantidade de produtos vendidos. 
# 6. Enviar o e-mail para diretoria 