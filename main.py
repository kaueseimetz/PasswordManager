import tkinter as tk
from cryptography.fernet import Fernet
import json

##Váriaveis

background = "#5CA6CD"

#with open('chave.key', 'rb') as key:
#    chave = key.read()
#
#fernet = Fernet(chave)
#
#with open('Entry.json') as arquivo:
#    conteudo = arquivo.read()
with open('dados.json', 'r', encoding='utf-8') as json_file:
    dados = json.load(json_file)
#
#dados = json.loads(fernet.decrypt(conteudo))

class Main:

    ##Inicio do Programa

    def __init__(self):
        jMain = tk.Tk()
        jMain.config(bg=background)
        jMain.iconbitmap('icons/key.ico')
        largura_janela = 800
        altura_janela = 400

        # Obtém a largura e altura da tela
        largura_tela = jMain.winfo_screenwidth()
        altura_tela = jMain.winfo_screenheight()

        # Calcula o deslocamento x e y para centralizar a janela na tela
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2

        # Define a geometria da janela com base na largura e altura especificadas e no deslocamento x e y
        jMain.geometry("{}x{}+{}+{}".format(largura_janela, altura_janela, x, y))
        # define a janela como iredimensionavel
        jMain.resizable(False, False)
        jMain.title("Senhas")

        ## LAYOUT ##

        mTitle = tk.Label(jMain, text="Suas senhas salvas", bg=background, font=("Arial", 24), fg="#000")
        mTitle.pack()

        nSenha = tk.Button(jMain, text="Nova Senha", fg="#000", width=25)
        nSenha.pack(pady=15)

        for chave, valor in dados.items():
            if chave == "loguin":
                continue
            aUser = tk.Label(jMain, text=f"{chave}: {valor}", bg=background)
            aUser.pack()

        Frame = tk.Frame(jMain)
        Frame.config()
        for cad, valores in dados.items():
            print(f"Cad: {cad}")
            fUser = tk.Label(Frame, text=f"Cad: {cad}", bg="white")
            fUser.pack()
            for chave, valor in valores.items():
                print(f"{chave}: {valor}")
                fPass = tk.Label(Frame, text=f"{chave}: {valor}", bg="white")
                fPass.pack(pady=7.5)
            print()  # pula uma linha após cada usuário


        jMain.mainloop()