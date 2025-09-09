import json
import time

# Caminho do arquivo de alertas do Wazuh
LOG_FILE = "/var/ossec/logs/alerts/alerts.json"

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

# Função para monitorar o arquivo em tempo real
def monitorar_alertas():
    print(" Monitorando alertas em tempo real... (Ctrl+C para parar)")
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            f.seek(0, 2)  # Vai para o final do arquivo
            while True:
                line = f.readline()
                if line:
                    try:
                        alerta = json.loads(line.strip())
                        rule = alerta.get("rule", {})
                        nivel = rule.get("level", -1)
                        classificacao = classificar_alerta(nivel)

                        ip = alerta.get("srcip") or alerta.get("agent", {}).get("ip", "N/A")
                        descricao = rule.get("description", "Sem descrição")

                        print(f"→ IP: {ip}")
                        print(f"→ Nível: {nivel} ({classificacao})")
                        print(f"→ Descrição: {descricao}")
                        print('-' * 50)

                    except json.JSONDecodeError:
                        print("⚠️ Linha inválida (ignorada).")
                else:
                    time.sleep(1)  # Evita 100% CPU quando não tem nada novo
    except KeyboardInterrupt:
        print("\n Monitoramento encerrado.")

if __name__ == "__main__":
    monitorar_alertas()
