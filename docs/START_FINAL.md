# 🚀 Guia de Início Rápido - Trivia API Full Stack

## ✅ Tudo Funcionando!

### Serviços Ativos:
- ✅ **Backend Flask:** http://127.0.0.1:5000
- ✅ **Frontend React:** http://localhost:3000  
- ✅ **PostgreSQL (Docker):** Porta 5432

---

## 🎯 Como Acessar a Aplicação

### Opção 1: Navegador (Recomendado)
Abra seu navegador e acesse:
```
http://localhost:3000
```

### Opção 2: Verificar se está rodando
```bash
# Ver status de todos os serviços
lsof -i :5000  # Backend
lsof -i :3000  # Frontend
docker compose ps  # PostgreSQL
```

---

## 🎮 Funcionalidades Disponíveis

### 1. 📋 Ver Perguntas (List View)
- Visualize todas as perguntas
- Paginação (10 por página)
- Filtre por categoria
- Busque perguntas

### 2. ➕ Adicionar Perguntas (Add View)
- Crie novas perguntas trivia
- Defina categoria e dificuldade
- Question + Answer

### 3. 🎲 Jogar Quiz (Play View)
- Jogue até 5 perguntas
- Escolha uma categoria ou "All"
- Veja sua pontuação final

---

## 🧪 Testar API com curl

### 1. Listar Categorias
```bash
curl http://127.0.0.1:5000/categories
```

### 2. Listar Perguntas (página 1)
```bash
curl http://127.0.0.1:5000/questions?page=1
```

### 3. Buscar Perguntas
```bash
curl -X POST http://127.0.0.1:5000/questions \
  -H "Content-Type: application/json" \
  -d '{"searchTerm": "movie"}'
```

### 4. Criar Pergunta
```bash
curl -X POST http://127.0.0.1:5000/questions \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is the capital of France?",
    "answer": "Paris",
    "category": 3,
    "difficulty": 1
  }'
```

### 5. Jogar Quiz
```bash
curl -X POST http://127.0.0.1:5000/quizzes \
  -H "Content-Type: application/json" \
  -d '{
    "quiz_category": {"type": "Science", "id": 1},
    "previous_questions": []
  }'
```

---

## 📚 Documentação Completa

### Backend
- **API Docs:** `backend/README.md`
- **Testes:** `backend/test_flaskr.py`
- **Testes com curl:** `backend/TEST_API.md`
- **Setup:** `backend/SETUP.md`
- **Docker:** `DOCKER_SETUP.md`

### Frontend
- **Inicialização:** `INICIALIZAR_FRONTEND.md`
- **Componentes:** `frontend/src/components/`
- **Estilos:** `frontend/src/stylesheets/`

### Integração
- **Status Completo:** `INTEGRACAO_COMPLETA.md`
- **Resumo Setup:** `RESUMO_SETUP.md`
- **Verificação:** `VERIFICAR_AMBIENTE_LOCAL.md`

---

## 🔧 Troubleshooting

### Backend não responde
```bash
cd backend
source ../.venv/bin/activate
flask run --reload
```

### Frontend não carrega
```bash
cd frontend
npm start
```

### Database não conecta
```bash
docker compose up -d
```

### Ver logs do Backend
```bash
tail -f backend/flask_app.log
```

### Ver logs do Frontend
Verifique o terminal onde `npm start` está rodando.

---

## 🎓 Estrutura do Projeto

```
.
├── backend/
│   ├── flaskr/
│   │   └── __init__.py      # API endpoints
│   ├── models.py             # SQLAlchemy models
│   ├── test_flaskr.py        # Testes unitários
│   ├── trivia.psql          # Database schema
│   ├── requirements.txt      # Python dependencies
│   └── README.md            # API documentation
│
├── frontend/
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── stylesheets/      # CSS files
│   │   └── App.js           # Main app
│   ├── package.json         # npm dependencies
│   └── README.md
│
├── docker-compose.yml        # PostgreSQL container
└── README.md                 # Project overview
```

---

## 📊 Stack Tecnológica

### Backend
- **Python 3.12**
- **Flask 3.0.0**
- **SQLAlchemy 2.0.25**
- **PostgreSQL 14**
- **uv** (package manager)

### Frontend
- **React 17.0.1**
- **React Router 5.2.1**
- **jQuery 3.6.0**

### DevOps
- **Docker & Docker Compose**
- **Virtual Environment**
- **npm & pip**

---

## 🎉 Pronto para Usar!

A aplicação está completamente funcional e integrada.

### Próximos Passos (Opcional):
1. Customizar estilos CSS
2. Adicionar mais perguntas ao database
3. Modificar lógica do quiz
4. Adicionar novos endpoints
5. Deploy em produção

---

**Aproveite a aplicação Trivia! 🎲**
