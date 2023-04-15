import json

# abrir o arquivo JSON
with open('../dados.json', 'r', encoding='utf-8') as json_file:
    dados = json.load(json_file)

# percorrer o objeto Python e imprimir todos os valores
for cad, valores in dados.items():
    print(f"Cad: {cad}")
    for chave, valor in valores.items():
        print(f"{chave}: {valor}")
    print()  # pula uma linha após cada usuário