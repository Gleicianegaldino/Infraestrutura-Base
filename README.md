# Orquestração de IA com n8n para Análise de Dados  

Este projeto é uma **Prova de Conceito (PoC)** de um sistema de Business Intelligence utilizando **Docker, FastAPI, PostgreSQL e n8n**.  A solução centraliza a migração de dados de planilhas Google Sheets para um banco de dados, além de permitir consultas em **linguagem natural via IA**, respondendo com base nos dados armazenados.  

## Tecnologias:
- **FastAPI** → API principal;
- **PostgreSQL** → Banco de dados relacional;  
- **n8n** → Orquestração de workflows (ETL e IA);
- **Docker + Docker Compose** → Infraestrutura containerizada;
- **Postman** → Testes de API e entrada de "perguntas".

## Estrutura do Repositório:
.

├── assets

├── postgres_data

├── docker-compose.yml

├── Dockerfile

├── main.py

└── requirements.txt

## Como rodar o projeto: 

1. Abra o **Docker Desktop** e faça login.  
2. Acesse a pasta do projeto no terminal:  
   ```bash
   cd Infraestrutura-Base
3. Execute:
   ```bash
   docker-compose up -d

### Isso irá iniciar:
- API → http://localhost:8000
- n8n → http://localhost:5678
 (login: admingle / senha: admingle123)
- Postgres → porta 5432
  
-  Para verificar se está rodando:  
     ```bash
    docker ps

### Endpoints principais da API:
- GET / → status da API
- POST /eventos/ → cria evento
- GET /eventos/ → lista eventos
- GET /eventos/{nome_evento} → consulta evento
- PUT /eventos/{nome_evento} → atualiza evento
- DELETE /eventos/{nome_evento} → remove evento

### Fluxos criados no n8n:
- ETL (planilhas → banco + API): lê dados de 3 Google Sheets, padroniza colunas, remove duplicidades e insere no Postgres.
  <img width="1048" height="380" alt="Arquitetura-do-fluxo-etapa-2" src="https://github.com/user-attachments/assets/f942e088-de0e-487d-84ae-0f6a11f64863" />
  Arquivo JSON do: [Workflow Etapa 2](assets/Workflow-Etapa2.json)

- Consulta com IA: recebe pergunta em linguagem natural, identifica os filtros corretos, consulta a API e retorna uma resposta estruturada.
  <img width="1376" height="414" alt="Arquitetura-do-fluxo-etapa-3" src="https://github.com/user-attachments/assets/e3cf6c74-8516-4218-84ab-9eef8f8f87dc" />
 Arquivo JSON do:
[Workflow Etapa 3](assets/Workflow-Etapa3.json)

#### Relatório Técnico:
Em **assets** também encontra-se o [relatório técnico detalhado](assets/relatorio.md), descrevendo todo o processo de desenvolvimento.



### Desafios pessoais:
- Primeiro contato com n8n e OpenAI;
- Ajustes de JSON e padronização de dados;
- Integração entre múltiplos serviços em containers.
