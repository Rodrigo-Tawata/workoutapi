# 🏋️‍♂️ WorkoutAPI

API RESTful para gerenciamento de centros de treinamento, atletas e categorias, desenvolvida com FastAPI, SQLAlchemy Async e PostgreSQL.

---

## 📌 Tecnologias Utilizadas

- **FastAPI** — Framework moderno para APIs assíncronas.
- **SQLAlchemy Async** — ORM assíncrono para interação com o banco de dados.
- **PostgreSQL** — Sistema de gerenciamento de banco de dados relacional.
- **Alembic** — Ferramenta para migrações de banco de dados.
- **FastAPI Pagination** — Biblioteca para paginação de resultados.
- **Pydantic** — Validação de dados e serialização.

---

## 🚀 Como Rodar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/Rodrigo-Tawata/workoutapi.git
cd workoutapi
```
### 2. Criar e Ativar o Ambiente Virtual
```
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### 3. Instalar as Dependências
```
pip install -r requirements.txt
```
### 4. Configurar o Banco de Dados
- Banco de Dados: PostgreSQL
- Usuário: workout
- Senha: workout
- Banco: workout
### 5. Aplicar as Migrações
```
alembic upgrade head
```
### 6. Usando com Docker
```
docker-compose up --build
```

### 7. Rodar o Servidor
```
uvicorn workout_api.main:app --reload
```

## 📚 Endpoints
### 🏋️‍♂️ Centros de Treinamento
- GET /centros_treinamento/ — Retorna todos os centros de treinamento.
- GET /centros_treinamento/{id} — Retorna um centro de treinamento pelo ID.
- POST /centros_treinamento/ — Cria um novo centro de treinamento.

### 🏃‍♂ Atletas
- GET /atletas/ — Retorna todos os atletas, com suporte a filtros por nome e cpf.
- GET /atletas/{id} — Retorna um atleta pelo ID.
- POST /atletas/ — Cria um novo atleta.
- PUT /atletas/{id} — Atualiza um atleta existente.
- DELETE /atletas/{id} — Deleta um atleta pelo ID.

### 📦 Categorias
- GET /categorias/ — Retorna todas as categorias.
- GET /categorias/{id} — Retorna uma categoria pelo ID.
- POST /categorias/ — Cria uma nova categoria.
