# esse programa deve ser colocado dentro do container do wazuh manager
import json
import time
import requests
import re

# Caminho do arquivo de alertas do Wazuh
LOG_FILE = "/var/ossec/logs/alerts/alerts.json"

# Configura    o do Flask
FLASK_URL = "http://host.docker.internal:5000/ban"  # Flask rodando no Windows
API_TOKEN = "El_Psy_Congroo"         # mesmo token do Flask

# Fun    o de classifica    o
def classificar_alerta(nivel):
    if nivel == 0:
        return "Ignorado"
    elif 1 <= nivel <= 3:
        return "Informativo"
    elif 4 <= nivel <= 6:
        return "Baixa"
    elif 7 <= nivel <= 8:
        return "M  dia"
    elif 9 <= nivel <= 10:
        return "Alta"
    elif 11 <= nivel <= 13:
        return "Cr  tica"
    elif 14 <= nivel <= 15:
        return "Emergencial"
    else:
        return "N  vel inv  lido"

def enviar_ban(ip, descricao):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"ip": ip, "reason": descricao}}
    try:
        r = requests.post(FLASK_URL, json=payload, headers=headers, timeout=5)
        print(f"[+] Ban enviado para {ip} => {r.status_code} {r.text}")
    except Exception as e:
        print(f"[!] Erro ao enviar ban para {ip}: {e}")

# Fun    o para monitorar o arquivo em tempo real
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

                        descricao = rule.get("description", "Sem descri    o")
                        m = re.search(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", descricao)
                        ip = m.group(0) if m else None

                        print(f" IP: {ip}")
                        print(f" N  vel: {nivel} ({classificacao})")
                        print(f" Descri    o: {descricao}")
                        print('-' * 50)

                        # Se for brute force n  vel alto  ^f^r banir
                        if nivel >= 15 and "brute" in descricao.lower():
                            if ip:
                                enviar_ban(ip, descricao)

                    except json.JSONDecodeError:
                        print(" Linha inv  lida (ignorada).")
                else:
                    time.sleep(1)  # evita 100% CPU
    except KeyboardInterrupt:
        print("\n Monitoramento encerrado.")

if __name__ == "__main__":
    monitorar_alertas()
