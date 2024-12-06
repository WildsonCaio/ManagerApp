# Sistema de Gestão de Projetos, Tarefas, Times e Equipes

## **Descrição da Aplicação**

Este sistema é uma solução para gerenciamento de projetos, tarefas, equipes e clientes. Ele permite que empresas acompanhem o progresso de suas iniciativas, organizem times e monitorem tarefas. Com foco em produtividade e organização, a aplicação oferece:

- **Gestão de Projetos**: Criação, monitoramento e atualização do status dos projetos.
- **Gestão de Tarefas**: Organização das tarefas dentro de cada projeto, com atribuição de status e descrição.
- **Gestão de Equipes**: Formação de times para colaborar em projetos específicos.

---

## **Tecnologias Utilizadas**

- **Backend**: Django 5.1.3
- **Banco de Dados**: PostgreSQL
- **Containerização**: Docker e Docker Compose
- **Linguagem de Programação**: Python 3.10
- **Frontend**: Vue.js

---

## **Pré-requisitos**

Certifique-se de ter os seguintes softwares instalados no seu ambiente:

1. **Docker**: [Baixe aqui](https://docs.docker.com/get-docker/)
2. **Docker Compose**: Geralmente incluído no Docker Desktop.


## **Passos para Instalação**

1. Clonar o Repositório
Clone este repositório para o seu ambiente local:
```
        git clone https://github.com/seu-usuario/sistema-gestao-projetos.git
        cd sistema-gestao-projetos
```

2. Clonar o Repositório
Inicie os serviços usando o Docker Compose:
```
        docker compose up --build
```
Isso irá:

- **Construir as imagens do Docker.**
- **Configurar o banco de dados PostgreSQL.**
- **Subir o backend Django e frontend Vue.**

## **Executar Scripts de População** ##
Após os containers estarem em execução, execute o script para popular o banco de dados com informações iniciais (clientes, projetos, equipes e tarefas):
1. Acesse o container do backend:
```
        docker exec -it django-backend bash
```

2. Execute o script de população do banco:
```
        python /app/populate_database.py
```

3. Execute os testes do backend:
```
        pytest
```

## **Estrutura dos Modelos**

A aplicação possui os seguintes modelos:

### **Client**
- **user**: Um usuário do sistema vinculado ao cliente.
- **phone**: Telefone do cliente.

### **Team**
- **name**: Nome do time.
- **users**: Usuários vinculados ao time.

### **Project**
- **name**: Nome do projeto.
- **client**: Cliente associado ao projeto.
- **team**: Time responsável pelo projeto.
- **status**: Status do projeto (PENDENTE, EM EXECUÇÃO, COMPLETO).
- **start_date**: Data de início do projeto.
- **end_date**: Data de término do projeto.

### **Task**
- **name**: Nome da tarefa.
- **description**: Descrição detalhada da tarefa.
- **project**: Projeto ao qual a tarefa pertence.
- **status**: Status da tarefa (PENDENTE, EM EXECUÇÃO, COMPLETA).
- **created_at**: Data e hora de criação.

---

