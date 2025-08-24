# Relatório

## Etapa 1: Infraestrutura Base (Docker, Python, Postgres)

### Obter a estrutura do projeto:
Ao clonar ou fazer o fork desse repositório, você encontrará a seguinte estrutura de arquivos:

/Infraestrutura-Base

├──/postgres_data

├── Dockerfile (Instruções para construir a imagem da API)

├── docker-compose.yml (Inicia a API, o banco de dados e o n8n)

├── main.py (Código da API em Python)

└── requirements.txt (Dependências do Python)

### Acessando a pasta do projeto pelo terminal:
Para rodar o projeto, você precisa primeiro abrir um terminal ou PowerShell dentro da pasta que contém o arquivo **docker-compose.yml**. 
Existem duas formas fáceis de fazer isso:

- **Usando o comando cd**:  
  No terminal, digite `cd` (que significa "mudar diretório") seguido do caminho da sua pasta e pressione Enter.  
  Exemplo:  
cd C:\Users\SeuUsuario\Desktop\Projetos\Infraestrutura-Base

- **Direto do Visual Studio Code**:  
Se você já usa o VS Code, pode abrir o terminal diretamente na pasta do projeto.  
No menu superior, vá em **Terminal → New Terminal**.  
O terminal já abrirá no local certo, pronto para você usar.

### Como rodar o projeto:
- Primeiro precisa abrir o **Docker Desktop** e acessar a conta cadastrada.  
- Depois, acessar a pasta do projeto chamada **Infraestrutura-Base** (que contém o arquivo docker-compose.yml).  
- Executar o comando: docker-compose up -d

Esse comando vai iniciar a API, o banco de dados e o n8n de uma vez, rodando em segundo plano.

### Como saber se deu certo:
Verifique o status dos contêineres com: docker ps

A saída mostrará os contêineres **api_container**, **postgres_container** e **n8n_container** com status **Up**.

### Acessando os Serviços:

- **API**:  
  Disponível na porta 8000 [http://localhost:8000](http://localhost:8000)  
  Retorno esperado:  
  ```json
  {"status": "API está funcionando!"}

- **n8n**:
    A sua instância do n8n estará disponível na porta 5678. Acesse http://localhost:5678 no seu navegador e faça login com as credenciais padrão: usuário admingle e senha admingle123.


- **PostgreSQL**:
    O banco de dados está na porta 5432. Ele só é acessível pelos outros contêineres. Para interagir com ele, você pode usar uma ferramenta de banco de dados ou entrar no contêiner com docker exec -it postgres_container psql -U admingle -d meubanco.
