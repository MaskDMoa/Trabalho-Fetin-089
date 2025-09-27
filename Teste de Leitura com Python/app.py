#programa usado para fazer os requests e lugar que os ips são banidos
#comando utilizado (Invoke-WebRequest -Method POST -Uri http://127.0.0.1:5000/login -Body "user=admin&password=errado")                                                                     
from flask import Flask, request, abort
import logging, os, json, threading, time

app = Flask(__name__)

# Caminho de log no Windows
log_dir = r"C:\Users\BigHi\teste\logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "app.log")
ban_file = os.path.join(log_dir, "banned_ips.json")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# Usuários e senhas de teste (use um banco/arquivo real em produção)
USERS = {
    "admin": "admin123",
    "teste": "teste123"
}

# Carrega banlist (persistente)
def load_banlist():
    try:
        with open(ban_file, "r") as f:
            return set(json.load(f))
    except Exception:
        return set()

def save_banlist(banned):
    with open(ban_file, "w") as f:
        json.dump(list(banned), f)

banned_ips = load_banlist()

# Bloqueia antes de qualquer request
@app.before_request
def block_banned():
    ip = request.remote_addr
    if ip in banned_ips:
        logging.warning("REJECTED request from banned IP %s to %s", ip, request.path)
        abort(403, "IP banido")

# Endpoint para banir IP (protegê-lo: token simples — troque por algo mais seguro em prod)
API_TOKEN = os.environ.get("BAN_API_TOKEN", "El_Psy_Congroo")

@app.route('/ban', methods=['POST'])
def ban_ip():
    token = request.headers.get("Authorization", "")
    if token != f"Bearer {API_TOKEN}":
        return "Unauthorized", 401

    data = request.get_json(force=True, silent=True) or {}
    ip = data.get("ip")
    duration = data.get("duration")  # opcional: segundos (não implementamos unban automático aqui)
    if not ip:
        return "Missing ip", 400

    banned_ips.add(ip)
    save_banlist(banned_ips)
    logging.warning("IP %s adicionado à banlist via API (duration=%s)", ip, duration)
    return "banned", 200

@app.route('/unban', methods=['POST'])
def unban_ip()::
    token = request.headers.get("Authorization", "")
    if token != f"Bearer {API_TOKEN}":
        return "Unauthorized", 401
    data = request.get_json(force=True, silent=True) or {}
    ip = data.get("ip")
    if not ip:
        return "Missing ip", 400
    if ip in banned_ips:
        banned_ips.remove(ip)
        save_banlist(banned_ips)
    return "unbanned", 200

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('password')
    ip = request.remote_addr

    if not user or not password:
        return "Faltou usuário ou senha", 400

    # Validação
    if user in USERS and USERS[user] == password:
        logging.info("LOGIN_SUCCES user=%s ip=%s", user, ip)
        return "Login ok"
    else:
        logging.warning("LOGIN_FAIL user=%s ip=%s", user, ip)
        return "Login falhou", 401

if __name__ == '__main__':
    # Rode em host Windows: app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000)

