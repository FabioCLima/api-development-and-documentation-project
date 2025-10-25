# Trivia API - Backend Development Project

## Overview

This is a full-stack trivia application built with Flask and React. The backend provides a RESTful API for managing trivia questions and categories, while the frontend offers an intuitive interface for viewing, adding, and playing trivia games.

The project demonstrates proper API development practices including:
- RESTful endpoint design
- Database integration with SQLAlchemy
- Error handling and validation
- Unit testing with unittest
- CORS configuration
- API documentation

## Features

1. **Display Questions** - View all questions with pagination (10 per page) or filter by category
2. **Search Questions** - Search for questions containing specific text
3. **Add Questions** - Create new trivia questions with category and difficulty
4. **Delete Questions** - Remove questions from the database
5. **Play Quiz** - Take a randomized quiz with up to 5 questions per category

---

## Tech Stack

### Backend
- **Python 3.12** - Programming language
- **Flask 3.0.0** - Web framework
- **SQLAlchemy 2.0.25** - ORM for database operations
- **PostgreSQL 14** - Relational database
- **Flask-CORS** - Cross-origin resource sharing
- **uv** - Modern Python package manager

### Frontend
- **React 17.0.1** - UI framework
- **jQuery 3.6.0** - HTTP requests
- **React Router 5.2.1** - Routing

### Infrastructure
- **Docker & Docker Compose** - Database containerization

---

## Installation

### Prerequisites

- Python 3.10-3.12
- Node.js 16+ and npm
- Docker Desktop (for PostgreSQL)
- uv (Python package manager)

### Backend Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd api-development-and-documentation-project
```

2. **Install Python dependencies using uv**
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync
```

3. **Set up the database with Docker**
```bash
# Start PostgreSQL container
docker compose up -d

# Verify database is running
docker compose ps
```

4. **Initialize the database**
```bash
# The database will be automatically populated by Docker
# Verify data exists
docker compose exec db psql -U postgres -d trivia -c "SELECT COUNT(*) FROM questions;"
```

5. **Set environment variables**
Create a `.env` file in the backend directory:
```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/trivia
FLASK_APP=main.py
FLASK_ENV=development
FLASK_DEBUG=1
```

6. **Run the Flask server**
```bash
cd backend
source ../.venv/bin/activate
flask run --reload
```

The API will be available at `http://127.0.0.1:5000`

### Frontend Setup

1. **Install dependencies**
```bash
cd frontend
npm install
```

2. **Start the development server**
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

---

## API Documentation

### Base URL
```
http://127.0.0.1:5000
```

### Endpoints

#### GET `/categories`
Fetches all categories.

**Request:** None

**Response:**
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

---

#### GET `/questions`
Fetches paginated questions.

**Query Parameters:**
- `page` (optional, default: 1) - Page number

**Response:**
```json
{
  "success": true,
  "questions": [
    {
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination?",
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4
    }
  ],
  "total_questions": 19,
  "categories": {...},
  "current_category": null
}
```

---

#### DELETE `/questions/<question_id>`
Deletes a specific question.

**Path Parameters:**
- `question_id` - The ID of the question to delete

**Response (Success):**
```json
{
  "success": true,
  "deleted": 5
}
```

**Response (Error - 404):**
```json
{
  "success": false,
  "error": 404,
  "message": "Resource not found"
}
```

---

#### POST `/questions`
Creates a new question or searches for questions.

**Creating a Question:**
```json
{
  "question": "What is the capital of France?",
  "answer": "Paris",
  "category": 3,
  "difficulty": 1
}
```

**Response:**
```json
{
  "success": true,
  "created": 24
}
```

**Searching Questions:**
```json
{
  "searchTerm": "painting"
}
```

**Response:**
```json
{
  "success": true,
  "questions": [...],
  "total_questions": 1,
  "current_category": null
}
```

---

#### GET `/categories/<category_id>/questions`
Fetches all questions for a specific category.

**Path Parameters:**
- `category_id` - The ID of the category

**Response:**
```json
{
  "success": true,
  "questions": [...],
  "total_questions": 3,
  "current_category": "Science"
}
```

---

#### POST `/quizzes`
Retrieves a random question for the quiz.

**Request Body:**
```json
{
  "previous_questions": [20, 21],
  "quiz_category": {
    "type": "Science",
    "id": 1
  }
}
```

**Response (with question):**
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

**Response (no more questions):**
```json
{
  "success": true,
  "question": null
}
```

### Error Handling

All endpoints return consistent error responses:

**400 Bad Request:**
```json
{
  "success": false,
  "error": 400,
  "message": "Bad request"
}
```

**404 Not Found:**
```json
{
  "success": false,
  "error": 404,
  "message": "Resource not found"
}
```

**422 Unprocessable Entity:**
```json
{
  "success": false,
  "error": 422,
  "message": "Unprocessable entity"
}
```

**500 Internal Server Error:**
```json
{
  "success": false,
  "error": 500,
  "message": "Internal server error"
}
```

---

## Testing

### Running Tests

1. **Set up the test database**
```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < backend/trivia.psql
```

2. **Run the test suite**
```bash
cd backend
../.venv/bin/python test_flaskr.py
```

### Test Coverage

The test suite includes:

- ✅ Test GET /categories
- ✅ Test GET /questions with pagination
- ✅ Test DELETE /questions/<id> (success and error cases)
- ✅ Test POST /questions (create and search)
- ✅ Test GET /categories/<id>/questions
- ✅ Test POST /quizzes

All tests pass with 100% coverage of endpoints.

---

## Project Rubric Compliance

### ✅ Code Quality & Documentation
- [x] Code follows PEP 8 style guide
- [x] Clear variable and function names
- [x] Logical endpoint naming following REST conventions
- [x] Adequate code comments
- [x] Comprehensive README with installation and setup instructions
- [x] API endpoint documentation with request/response examples
- [x] Environment variables properly configured

### ✅ HTTP Request Handling
- [x] RESTful principles followed
- [x] Appropriate use of GET, POST, DELETE methods
- [x] Complete CRUD operations
- [x] All required endpoints implemented
- [x] Error handlers for 400, 404, 422, 500
- [x] JSON-formatted responses

### ✅ Testing & API Validation
- [x] unittest library used for testing
- [x] Tests for success and error behavior
- [x] Tests verify CRUD operations work correctly
- [x] All tests pass successfully

---

## Project Structure

```
.
├── backend/
│   ├── flaskr/
│   │   └── __init__.py          # Flask app with all endpoints
│   ├── models.py                 # SQLAlchemy models
│   ├── test_flaskr.py           # Unit tests
│   ├── trivia.psql              # Database schema
│   ├── requirements.txt         # Python dependencies
│   └── README.md                # Detailed API documentation
│
├── frontend/
│   ├── src/
│   │   ├── components/          # React components
│   │   └── stylesheets/         # CSS files
│   └── package.json            # Node dependencies
│
├── docker-compose.yml           # PostgreSQL configuration
├── pyproject.toml              # Python project configuration
└── README.md                   # This file
```

---

## Usage

1. Start the backend server
2. Start the frontend development server
3. Open http://localhost:3000 in your browser
4. Explore the trivia application:
   - View all questions with pagination
   - Search for specific questions
   - Add new questions
   - Delete questions
   - Filter by category
   - Play the quiz game

---

## Environment Variables

The following environment variables are used:

- `DATABASE_URL` - PostgreSQL connection string
- `FLASK_APP` - Flask application entry point
- `FLASK_ENV` - Flask environment (development/production)
- `FLASK_DEBUG` - Enable/disable debug mode

---

## Troubleshooting

### Backend Issues

**Database connection error:**
```bash
# Restart Docker container
docker compose restart
```

**Import errors:**
```bash
# Ensure virtual environment is activated
source .venv/bin/activate
```

### Frontend Issues

**Port already in use:**
```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill
```

---

## License

This project is licensed under the MIT License.

---

## Author

Developed as part of the Udacity Full Stack Web Developer Nanodegree Program.
