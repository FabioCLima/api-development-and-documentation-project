# Guia de Testes da API - Trivia API

Este documento contém exemplos de como testar todos os endpoints da API usando `curl`.

## Pré-requisitos

Certifique-se de que o servidor está rodando:

```bash
cd backend
flask run --reload
```

O servidor estará disponível em `http://127.0.0.1:5000`

## Endpoints

### 1. GET /categories

Lista todas as categorias disponíveis.

```bash
curl http://127.0.0.1:5000/categories
```

**Resposta esperada:**
```json
{
  "success": true,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```

### 2. GET /questions

Lista todas as perguntas com paginação (10 por página).

```bash
curl http://127.0.0.1:5000/questions
```

Para obter uma página específica:

```bash
curl "http://127.0.0.1:5000/questions?page=2"
```

**Resposta esperada:**
```json
{
  "success": true,
  "questions": [...],
  "total_questions": 19,
  "categories": {...},
  "current_category": null
}
```

### 3. POST /questions

Cria uma nova pergunta.

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

**Resposta esperada:**
```json
{
  "success": true,
  "created": 24
}
```

### 4. POST /questions (Busca)

Busca perguntas por termo.

```bash
curl -X POST http://127.0.0.1:5000/questions \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerm": "painting"
  }'
```

**Resposta esperada:**
```json
{
  "success": true,
  "questions": [...],
  "total_questions": 2,
  "current_category": null
}
```

### 5. DELETE /questions/<question_id>

Remove uma pergunta.

```bash
curl -X DELETE http://127.0.0.1:5000/questions/5
```

**Resposta esperada:**
```json
{
  "success": true,
  "deleted": 5
}
```

### 6. GET /categories/<category_id>/questions

Lista perguntas de uma categoria específica.

```bash
curl http://127.0.0.1:5000/categories/1/questions
```

**Resposta esperada:**
```json
{
  "success": true,
  "questions": [...],
  "total_questions": 3,
  "current_category": "Science"
}
```

### 7. POST /quizzes

Obtém uma pergunta aleatória para o quiz.

```bash
curl -X POST http://127.0.0.1:5000/quizzes \
  -H "Content-Type: application/json" \
  -d '{
    "previous_questions": [20, 21],
    "quiz_category": {"type": "Science", "id": 1}
  }'
```

Para todas as categorias:

```bash
curl -X POST http://127.0.0.1:5000/quizzes \
  -H "Content-Type: application/json" \
  -d '{
    "previous_questions": [5, 9],
    "quiz_category": {"type": "click", "id": 0}
  }'
```

**Resposta esperada:**
```json
{
  "success": true,
  "question": {
    "id": 22,
    "question": "Hematology is a branch of medicine involving the study of what?",
    "answer": "Blood",
    "category": 1,
    "difficulty": 4
  }
}
```

## Testando Erros

### 404 Not Found

```bash
curl http://127.0.0.1:5000/questions/9999
```

**Resposta esperada:**
```json
{
  "success": false,
  "error": 404,
  "message": "Resource not found"
}
```

### 422 Unprocessable Entity

```bash
curl -X POST http://127.0.0.1:5000/questions \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Test question without required fields"
  }'
```

**Resposta esperada:**
```json
{
  "success": false,
  "error": 400,
  "message": "Bad request"
}
```

## Testes Automatizados

Execute os testes unitários:

```bash
cd backend
python test_flaskr.py
```

## Formatação de Resposta

Para melhor legibilidade, você pode usar `jq`:

```bash
curl http://127.0.0.1:5000/categories | jq
```

Ou salve em um arquivo:

```bash
curl http://127.0.0.1:5000/questions > questions.json
```
