# Trabalho-Fetin-089: Automação de Respostas a Alertas do Wazuh

Este projeto monitora os alertas gerados pelo SIEM Wazuh em tempo real e executa respostas automáticas com base no tipo e nível do alerta.

## Funcionalidades
- Leitura do arquivo `alerts.json`
- Ações automáticas como bloqueio de IP
- Registro de incidentes

# Instalação do Wazuh com Docker

Este projeto utiliza a imagem oficial do Wazuh para criar um ambiente de SIEM local.

## Componentes
- wazuh/wazuh-manager
- wazuh/wazuh-indexer
- wazuh/wazuh-dashboard

## Guia oficial (referência)
- [Documentação Wazuh - Docker] (https://documentation.wazuh.com/current/deployment-options/docker/index.html)
- [Repositório oficial no Github] (https://github.com/wazuh/wazuh-docker)

## Etapas básicas
1. Instalar Docker Desktop
2. Clonar o repositório
3. Executar `docker-compose up -d`
4. Acessar o painel em `http://localhost`


