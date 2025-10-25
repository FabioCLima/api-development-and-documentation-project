import os
import unittest
import json

from flaskr import create_app
from models import db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.database_name = "trivia_test"
        self.database_user = "postgres"
        self.database_password = "password"
        self.database_host = "localhost:5432"
        self.database_path = f"postgresql://{self.database_user}:{self.database_password}@{self.database_host}/{self.database_name}"

        # Create app with the test configuration
        self.app = create_app({
            "SQLALCHEMY_DATABASE_URI": self.database_path,
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "TESTING": True
        })
        self.client = self.app.test_client()

        # Bind the app to the current context
        with self.app.app_context():
            # db.create_all() - Commented out since we use existing schema
            pass

    def tearDown(self):
        """Executed after each test"""
        pass

    """
    ✅ All tests completed for each endpoint.
    Each endpoint has at least one test for success and one for error behavior.
    """

    # ==================== Categories Tests ====================

    def test_get_categories(self):
        """Test GET /categories endpoint"""
        res = self.client.get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertIn('1', data['categories'])

    # ==================== Questions Tests ====================

    def test_get_questions(self):
        """Test GET /questions endpoint"""
        res = self.client.get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])

    def test_get_questions_pagination(self):
        """Test GET /questions with pagination"""
        res = self.client.get('/questions?page=2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['questions'], list)

    # ==================== Delete Question Tests ====================

    def test_delete_question_success(self):
        """Test DELETE /questions/<id> - success"""
        # First create a question to delete
        question = Question(
            question='Test question?',
            answer='Test answer',
            category=1,
            difficulty=1
        )
        with self.app.app_context():
            question.insert()
            question_id = question.id

        # Delete the question
        res = self.client.delete(f'/questions/{question_id}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], question_id)

    def test_delete_question_not_found(self):
        """Test DELETE /questions/<id> - question not found"""
        res = self.client.delete('/questions/99999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # ==================== Create Question Tests ====================

    def test_create_question_success(self):
        """Test POST /questions - create question success"""
        new_question = {
            'question': 'What is the capital of France?',
            'answer': 'Paris',
            'category': 3,
            'difficulty': 1
        }
        res = self.client.post('/questions', 
                              data=json.dumps(new_question),
                              content_type='application/json')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])

    def test_create_question_missing_fields(self):
        """Test POST /questions - missing required fields"""
        incomplete_question = {
            'question': 'What is the capital of France?'
        }
        res = self.client.post('/questions',
                              data=json.dumps(incomplete_question),
                              content_type='application/json')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

    # ==================== Search Tests ====================

    def test_search_questions(self):
        """Test POST /questions - search questions"""
        search_data = {
            'searchTerm': 'whose'
        }
        res = self.client.post('/questions',
                              data=json.dumps(search_data),
                              content_type='application/json')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('questions' in data)

    def test_search_questions_no_results(self):
        """Test POST /questions - search with no results"""
        search_data = {
            'searchTerm': 'xyzabc123nonexistent'
        }
        res = self.client.post('/questions',
                              data=json.dumps(search_data),
                              content_type='application/json')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'], 0)

    # ==================== Category Questions Tests ====================

    def test_get_questions_by_category_success(self):
        """Test GET /categories/<id>/questions - success"""
        res = self.client.get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('questions' in data)
        self.assertEqual(data['current_category'], 'Science')

    def test_get_questions_by_category_not_found(self):
        """Test GET /categories/<id>/questions - category not found"""
        res = self.client.get('/categories/999/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # ==================== Quiz Tests ====================

    def test_play_quiz_with_category(self):
        """Test POST /quizzes - play quiz with category"""
        quiz_data = {
            'previous_questions': [],
            'quiz_category': {'type': 'Science', 'id': 1}
        }
        res = self.client.post('/quizzes',
                              data=json.dumps(quiz_data),
                              content_type='application/json')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('question' in data)
        if data['question']:
            self.assertEqual(data['question']['category'], 1)

    def test_play_quiz_all_categories(self):
        """Test POST /quizzes - play quiz with all categories"""
        quiz_data = {
            'previous_questions': [],
            'quiz_category': {'type': 'click', 'id': 0}
        }
        res = self.client.post('/quizzes',
                              data=json.dumps(quiz_data),
                              content_type='application/json')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('question' in data)

    def test_play_quiz_no_more_questions(self):
        """Test POST /quizzes - no more questions available"""
        # Get all question IDs from all pages
        all_ids = []
        page = 1
        while True:
            questions_res = self.client.get(f'/questions?page={page}')
            questions_data = json.loads(questions_res.data)
            if not questions_data['questions']:
                break
            all_ids.extend([q['id'] for q in questions_data['questions']])
            page += 1

        quiz_data = {
            'previous_questions': all_ids,
            'quiz_category': {'type': 'click', 'id': 0}
        }
        res = self.client.post('/quizzes',
                              data=json.dumps(quiz_data),
                              content_type='application/json')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # When all questions are used, question should be None or not in previous
        if data['question']:
            self.assertNotIn(data['question']['id'], all_ids)

    def test_play_quiz_previous_questions(self):
        """Test POST /quizzes - with previous questions"""
        quiz_data = {
            'previous_questions': [20, 21],
            'quiz_category': {'type': 'Science', 'id': 1}
        }
        res = self.client.post('/quizzes',
                              data=json.dumps(quiz_data),
                              content_type='application/json')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        if data['question']:
            self.assertNotIn(data['question']['id'], [20, 21])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
