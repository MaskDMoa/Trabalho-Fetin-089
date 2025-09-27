# Subindo o ambiente Wazuh com Docker

Este diretório contém os arquivos necessários para subir um ambiente Wazuh usando Docker no Windows.

## Requisitos
- Docker Desktop instalado no Windows
- Git Bash, PowerShell ou outro terminal compatível

## Como subir
```bash
cd docker
docker-compose up -d
```

## Comandos para colocar o monitor.py
Comandos wazuh

cd wazuh-docker/single-node

docker-compose up -d

docker ps

docker exec -it single-node-wazuh.manager-1 bash

dnf install nano
dnf install pip
pip install flask
pip install request

nano monitor.py

Colar o codigo pronto.

python3 monitor.py

