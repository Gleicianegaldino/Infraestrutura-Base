# Relatório Técnico: Orquestração de IA com n8n para Análise de Dados

O objetivo desse projeto é desenvolver uma Prova de Conceito (PoC) de um sistema de Business Intelligence, no qual o n8n centraliza a orquestração da migração de dados de planilhas para um banco de dados e atua como motor de uma aplicação de IA conversacional, permitindo que o usuário faça perguntas em linguagem natural e receba respostas precisas baseadas nos dados.

Ao clonar ou fazer o fork deste repositório, você encontrará a seguinte estrutura de arquivos:
```powershell
.
├── assets
├── postgres_data
├── docker-compose.yml
├── Dockerfile
├── main.py
└── requirements.txt
```


### Acessando a pasta do projeto pelo terminal
Para rodar o projeto, você precisa primeiro abrir um terminal ou PowerShell dentro da pasta que contém o arquivo `docker-compose.yml`. 

#### Existem duas formas fáceis de fazer isso:
- **Usando o comando cd**:  
No terminal, digite o comando `cd` (que significa "mudar diretório") seguido do caminho da pasta e pressione Enter.
Por exemplo: `cd C:\Users\SeuUsuario\Desktop\Projetos\Infraestrutura-Base`

- **Direto do Visual Studio Code**:  
Se você já usa o VS Code, pode abrir o terminal diretamente na pasta do projeto. O terminal já abrirá no local certo, pronto para ser usado.
    No menu superior, vá em `Terminal > New Terminal`.

### Como rodar o projeto
Primeiro deve abrir o docker desktop e acessar a conta cadastrada; o próximo passo é acessar a pasta do projeto (explicado anteriormente), chamada `Infraestrutura-Base`, que contém o arquivo `docker-compose.yml`, abrir um terminal e executar o comando `docker-compose up -d`. O docker-compose.yml está configurado para iniciar a API, o banco de dados e o n8n de uma vez, e eles continuarão rodando em segundo plano.

O comando `docker-compose up`: vai ler o arquivo `docker-compose.yml` e iniciar todos os serviços definidos nele:
  - Construindo a imagem da API; 
  - Baixar a imagem do banco de dados e do n8n;
  - Iniciar todos os containers. 
  
  A flag `-d` significa "detach", o que faz com que os containers rodem em segundo plano, permitindo o uso continuo do terminal. 
  
  Ou seja:
1. Abrir o Docker Desktop e acessar a conta cadastrada.
2. Acessar a pasta do projeto `Infraestrutura-Base`.
3. Executar o comando: `docker-compose up -d`

No terminal aparecerá algo assim:
```powershell
[+] Running 3/3
 ✔ Container postgres_cont       Running                                    0.0s 
 ✔ Container api_container       Running                                    0.0s 
 ✔ Container n8n_container       Running                                    0.0s             
```

#### Verificando o status dos containers
Para verificar o status dos containers execute o comando: `docker ps`, a saída mostrará os containers `api_container`, `postgres_container` e `n8n_container` listados e com o status `Up`.

No terminal aparecerá algo assim:
```powershell
CONTAINER ID   IMAGE                     COMMAND                  CREATED      STATUS          PORTS                                         NAMES
5042780ea0cf   infraestrutura-base-api   "uvicorn main:app --…"   2 days ago   Up 11 minutes   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   api_container
e58460cd6514   n8nio/n8n                 "tini -- /docker-ent…"   2 days ago   Up 11 minutes   0.0.0.0:5678->5678/tcp, [::]:5678->5678/tcp   n8n_container
6be4eeab5c5e   postgres:15               "docker-entrypoint.s…"   2 days ago   Up 11 minutes   0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp   postgres_container      
```

### Acessando os Serviços:
- **API**: estará disponível na porta `8000`. Pode testá-la acessando `http://localhost:8000` no seu navegador. A resposta deve ser:

  `{
    "status": "API está funcionando!"
  }`

- **n8n**: A instância do n8n estará disponível na porta `5678`. Acesse `http://localhost:5678` no seu navegador e faça login com as credenciais padrão: usuário `admingle` e senha `admingle123`.

- **PostgreSQL**: O banco de dados está na porta `5432`. Ele só é acessível pelos outros containers. Para interagir com ele, você pode usar uma ferramenta de banco de dados ou entrar no container com `docker exec -it postgres_container psql -U admingle -d meubanco`.

