# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

## API Documentation

### Endpoint Documentation

#### GET `/categories`

Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category.

- **Request Arguments:** None
- **Returns:** An object with keys `success` and `categories`, that contains an object of `id: category_string` key:value pairs.

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

Fetches a paginated list of questions.

- **Request Arguments:** 
  - `page` (optional, default: 1) - Page number for pagination
- **Returns:** An object with keys `success`, `questions`, `total_questions`, `categories`, and `current_category`.

```json
{
  "success": true,
  "questions": [
    {
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4
    }
  ],
  "total_questions": 19,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null
}
```

---

#### DELETE `/questions/<question_id>`

Deletes a question by ID.

- **Request Arguments:** 
  - `question_id` (path parameter) - The ID of the question to delete
- **Returns:** An object with keys `success` and `deleted`.

Success Response:
```json
{
  "success": true,
  "deleted": 5
}
```

Error Response (404):
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
- **Request Body:** 
  ```json
  {
    "question": "What is the capital of France?",
    "answer": "Paris",
    "category": 3,
    "difficulty": 1
  }
  ```
- **Returns:** An object with keys `success` and `created`.

```json
{
  "success": true,
  "created": 24
}
```

**Searching Questions:**
- **Request Body:** 
  ```json
  {
    "searchTerm": "painting"
  }
  ```
- **Returns:** An object with keys `success`, `questions`, `total_questions`, and `current_category`.

```json
{
  "success": true,
  "questions": [
    {
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?",
      "answer": "One",
      "category": 2,
      "difficulty": 4
    }
  ],
  "total_questions": 1,
  "current_category": null
}
```

Error Response (400):
```json
{
  "success": false,
  "error": 400,
  "message": "Bad request"
}
```

---

#### GET `/categories/<category_id>/questions`

Fetches all questions for a specific category.

- **Request Arguments:** 
  - `category_id` (path parameter) - The ID of the category
- **Returns:** An object with keys `success`, `questions`, `total_questions`, and `current_category`.

Success Response:
```json
{
  "success": true,
  "questions": [
    {
      "id": 20,
      "question": "What is the heaviest organ in the human body?",
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4
    }
  ],
  "total_questions": 3,
  "current_category": "Science"
}
```

Error Response (404):
```json
{
  "success": false,
  "error": 404,
  "message": "Resource not found"
}
```

---

#### POST `/quizzes`

Retrieves a random question for the quiz game.

- **Request Body:** 
  ```json
  {
    "previous_questions": [20, 21],
    "quiz_category": {
      "type": "Science",
      "id": 1
    }
  }
  ```
  - `previous_questions` (array) - List of question IDs already shown
  - `quiz_category` (object) - Category object with `type` and `id`. Use `{"type": "click", "id": 0}` for all categories
- **Returns:** An object with keys `success` and `question`.

Success Response:
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

No More Questions:
```json
{
  "success": true,
  "question": null
}
```

---

### Error Handling

The API returns standard error responses:

#### 400 Bad Request
```json
{
  "success": false,
  "error": 400,
  "message": "Bad request"
}
```

#### 404 Not Found
```json
{
  "success": false,
  "error": 404,
  "message": "Resource not found"
}
```

#### 422 Unprocessable Entity
```json
{
  "success": false,
  "error": 422,
  "message": "Unprocessable entity"
}
```

#### 500 Internal Server Error
```json
{
  "success": false,
  "error": 500,
  "message": "Internal server error"
}
```

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
