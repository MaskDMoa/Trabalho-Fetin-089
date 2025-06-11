import json

# Abrindo e lendo o arquivo JSON
with open('Exemplos/alerta_exemplo.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# Acessando os dados
print("Timestamp:", dados["timestamp"])
print("IP de origem:", dados["srcip"])
print("Nível da regra:", dados["rule"]["level"])
print("Descrição da regra:", dados["rule"]["description"])