from cryptography.fernet import Fernet
import os

with open("../chave.key", "rb") as chave:
    key = chave.read()

with open("../Entry.json", "rb") as arquivo:
    conteudo = arquivo.read()
conteudo_decripted = Fernet(key).decrypt(conteudo)
with open("../Entry.json", "wb") as arquivo:
    arquivo.write(conteudo_decripted)