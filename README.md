# 🛡️ Trabalho Fetin 089 — Automação de Respostas a Alertas do Wazuh

Este projeto foi desenvolvido como parte do **Fetin 089**, com o objetivo principal de monitorar os alertas gerados pelo SIEM **Wazuh** em tempo real, executando respostas automatizadas e eficientes baseadas no nível e tipo de cada ameaça ou alerta reportado.

---

## 🎯 Sobre o Projeto
O foco central do projeto reside na segurança da informação proativa. Ele atua lendo o arquivo `alerts.json` em tempo real e orquestrando medidas de contenção para responder o mais depressa possível a possíveis invasões ou varreduras maliciosas.

### ⚙️ Requisitos
- **Docker** e **Docker Compose**
- Uma máquina capaz de rodar a stack local do Wazuh.

---

## 🚀 Como Rodar e Instalar

O ambiente depende da criação de um SIEM Wazuh local usando containeres.

1. **Instale o Docker Desktop:** Faça o download no [site oficial](https://www.docker.com/products/docker-desktop/).
2. Clone o repositório:
```bash
git clone https://github.com/MaskDMoa/Trabalho-Fetin-089.git
cd Trabalho-Fetin-089
```
3. Suba os containeres do Wazuh:
```bash
docker-compose up -d
```
4. Verifique o acesso ao painel através da interface gráfica (`http://localhost:5601/`).

---

## 📁 Estrutura do Projeto / Componentes Docker
O projeto utiliza a imagem oficial do Wazuh, desmembrada em:
| Componente / Pasta | Descrição |
|---|---|
| `wazuh-manager` | Responsável pelo gerenciamento de agentes e processamento lógico das regras de segurança. |
| `wazuh-indexer` | Banco de dados escalável para armazenamento e indexação de todos os logs e alertas recebidos. |
| `wazuh-dashboard` | Interface gráfica amigável para análise profunda e visualização dos dados do Indexer. |
| `Teste de Leitura com Python/` | Scripts locais para leitura do monitoramento `alerts.json`. |

---

## 🔧 Funcionalidades (Automação de Execução)
Quando o sistema e os painéis do Wazuh estiverem 100% operacionais, o script de automação associado irá realizar:
1. 📄 **Análise em Tempo Real:** Escaneamento ininterrupto do arquivo de log de alertas (`alerts.json`).
2. 🚫 **Ações Defensivas Automáticas:** Bloqueios ativos (como banimento de IP) caso se depare com alertas críticos predefinidos.
3. 📝 **Auditoria:** Registro formal de todas as medidas e incidentes contidos para análise pericial futura.

---

## 📚 Documentação Adicional
- [Documentação Wazuh - Docker](https://documentation.wazuh.com/current/deployment-options/docker/index.html)
- [Repositório Oficial no GitHub (Wazuh)](https://github.com/wazuh/wazuh)
