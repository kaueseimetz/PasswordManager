import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import json
from dictionary import *
from main import *
from log import *

with open('chave.key', 'rb') as key:
    chave = key.read()

fernet = Fernet(chave)

with open('Entry.json') as arquivo:
    conteudo = arquivo.read()

#password_decrypt = fernet.decrypt(conteudo)

#json_pass = json.loads(password_decrypt)

json_pass = json.loads(fernet.decrypt(conteudo))

#variáveis
userName = json_pass["loguin"][0]["user"]
userPass = json_pass["loguin"][0]["pass"]

backgroundColor = "#5CA6CD"

#JANELA CONFIG

janela = tk.Tk() # Cria uma janela
lPrint("Janela criada")

janela.config(bg=backgroundColor)

janela.iconbitmap('icons/key.ico')

janela.title("login") # Define o título da janela

largura_janela = 400
altura_janela = 150

# Obtém a largura e altura da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcula o deslocamento x e y para centralizar a janela na tela
x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2

# Define a geometria da janela com base na largura e altura especificadas e no deslocamento x e y
janela.geometry("{}x{}+{}+{}".format(largura_janela, altura_janela, x, y))

janela.resizable(False, False) # Define a janela como não redimensionavel

#JANELA LAYOUT

lName = tk.Label(janela, text="Nome:", bg=backgroundColor)
lName.pack()

name = tk.Entry(janela, width=25, font=('Arial', 14), fg='black', bg='white', insertbackground='black')
name.pack()

lPass = tk.Label(janela, text="Senha:", bg=backgroundColor)
lPass.pack()

password = tk.Entry(janela, width=25, font=('Arial', 14)) #OBS: colocar em formato de *
password.config(show="*")
password.pack()

def getData():
    iName = name.get()
    iPass = password.get()
    iEnter = f"Nome: '{iName}' Senha: '{iPass}'"
    lPrint(f"Nome inserido: '{iName}'")
    lPrint(f"Senha inserida: '{iPass.translate(str.maketrans(chars,'*' * len(chars)))}'")


    if iName == userName and iPass == userPass:
        lPrint("Entrando...")
        print("Entrando...")
        janela.destroy()
        Main()
    else:
        messagebox.showerror(message="Senha incorreta")
        print("Dandos incorretos")
        lPrint(f"Os dados ({iEnter}) Estão incorretos")
botao = tk.Button(janela, text="Entrar", command=getData, padx=60)
botao.pack(pady=15)

janela.mainloop() # Inicia o loop de eventos da janela