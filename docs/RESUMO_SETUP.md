# Resumo do Setup do Ambiente - Trivia API Backend

## ✅ O que já foi configurado

1. **Projeto inicializado com `uv`** - Dependências gerenciadas via `pyproject.toml`
2. **Ambiente virtual criado** em `.venv/` com Python 3.12
3. **Dependências instaladas** (Flask, SQLAlchemy, psycopg2, etc.)
4. **Configuração do Flask** - Arquivo `.flaskenv` criado
5. **API Flask implementada** - Todos os endpoints criados e funcionais
6. **CORS configurado** - Aplicação pronta para se conectar com o frontend

## 📋 Próximos passos necessários

### 1. Instalar e configurar PostgreSQL

```bash
# Instalar PostgreSQL
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

# Iniciar o serviço
sudo service postgresql start
```

### 2. Criar e popular o banco de dados

```bash
# Criar o database
createdb trivia

# Popular o database
cd backend
psql trivia < trivia.psql
```

### 3. Executar o servidor Flask

```bash
# Da raiz do projeto
source .venv/bin/activate  # Ativar ambiente virtual
cd backend
flask run --reload
```

O servidor estará disponível em: **http://127.0.0.1:5000**

## 🛠️ Arquivos importantes

- `pyproject.toml` - Configuração do projeto e dependências
- `backend/flaskr/__init__.py` - Aplicação Flask principal
- `backend/models.py` - Modelos do banco de dados
- `backend/test_flaskr.py` - Testes unitários
- `backend/.flaskenv` - Variáveis de ambiente do Flask

## 🧪 Executar testes

```bash
# Criar database de teste
dropdb trivia_test 2>/dev/null || true
createdb trivia_test
psql trivia_test < backend/trivia.psql

# Executar testes
cd backend
python test_flaskr.py
```

## 📝 Documentação adicional

- Ver `backend/SETUP.md` para guia completo em inglês
- Ver `backend/README.md` para documentação original do projeto
- Ver `backend/TEST_API.md` para exemplos de testes com curl

## 🧪 Testar a API

Antes de executar o frontend, teste a API com curl:

```bash
# Listar categorias
curl http://127.0.0.1:5000/categories

# Listar perguntas
curl http://127.0.0.1:5000/questions

# Criar uma pergunta
curl -X POST http://127.0.0.1:5000/questions \
  -H "Content-Type: application/json" \
  -d '{"question": "Test?", "answer": "Yes", "category": 1, "difficulty": 1}'
```

Ver `backend/TEST_API.md` para mais exemplos.

## 🔧 Troubleshooting

### PostgreSQL não conecta

Verifique se está rodando:
```bash
sudo service postgresql status
```

### Problemas com dependências

Reinstalar:
```bash
uv sync
```

### Resetar banco de dados

```bash
dropdb trivia
createdb trivia
psql trivia < backend/trivia.psql
```
