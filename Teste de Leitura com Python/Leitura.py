import json
import os

# Função de classificação
def classificar_alerta(nivel):
    if nivel == 0:
        return "Ignorado"
    elif 1 <= nivel <= 3:
        return "Informativo"
    elif 4 <= nivel <= 6:
        return "Baixa"
    elif 7 <= nivel <= 8:
        return "Média"
    elif 9 <= nivel <= 10:
        return "Alta"
    elif 11 <= nivel <= 13:
        return "Crítica"
    elif 14 <= nivel <= 15:
        return "Emergencial"
    else:
        return "Nível inválido"

# Função para processar vários arquivos
def processar_alertas(pasta_json):
    for arquivo in os.listdir(pasta_json):
        if arquivo.endswith('.json'):
            caminho = os.path.join(pasta_json, arquivo)
            with open(caminho, 'r', encoding='utf-8') as f:
                try:
                    alerta = json.load(f)
                    nivel = alerta.get('rule', {}).get('level', -1)
                    classificacao = classificar_alerta(nivel)
                    print(f"Arquivo: {arquivo}")
                    print(f"→ IP: {alerta.get('srcip')}")
                    print(f"→ Nível: {nivel}")
                    print(f"→ Classificação: {classificacao}")
                    print(f"→ Descrição: {alerta.get('rule', {}).get('description')}")
                    print('-' * 40)
                except json.JSONDecodeError:
                    print(f"Erro ao ler {arquivo}: JSON inválido.")


# Lendo e classificando todos os arquivos da pasta
processar_alertas('Exemplos')
