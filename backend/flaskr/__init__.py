from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    if test_config is None:
        setup_db(app)
    else:
        database_path = test_config.get('SQLALCHEMY_DATABASE_URI')
        setup_db(app, database_path=database_path)

    # Set up CORS. Allow '*' for origins.
    CORS(app, resources={r"/*": {"origins": "*"}})

    """
    Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    """
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories', methods=['GET'])
    def get_categories():
        try:
            categories = Category.query.all()
            formatted_categories = {category.id: category.type for category in categories}
            
            return jsonify({
                'success': True,
                'categories': formatted_categories
            })
        except Exception as e:
            abort(422)

    """
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.
    """
    @app.route('/questions', methods=['GET'])
    def get_questions():
        try:
            page = request.args.get('page', 1, type=int)
            start = (page - 1) * QUESTIONS_PER_PAGE
            end = start + QUESTIONS_PER_PAGE

            questions = Question.query.order_by(Question.id).all()
            total_questions = len(questions)
            current_questions = [question.format() for question in questions[start:end]]

            categories = Category.query.all()
            formatted_categories = {category.id: category.type for category in categories}

            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': total_questions,
                'categories': formatted_categories,
                'current_category': None
            })
        except Exception as e:
            abort(422)

    """
    Create an endpoint to DELETE question using a question ID.
    """
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.get(question_id)
            
            if question is None:
                abort(404)
            
            question.delete()
            
            return jsonify({
                'success': True,
                'deleted': question_id
            })
        except Exception as e:
            if hasattr(e, 'code') and e.code == 404:
                abort(404)
            abort(422)

    """
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.
    """
    @app.route('/questions', methods=['POST'])
    def create_question():
        try:
            body = request.get_json()
            
            # Check if it's a search request FIRST
            search_term = body.get('searchTerm', None)
            if search_term:
                return search_questions(search_term)
            
            # Otherwise validate required fields for creating question
            question_text = body.get('question', None)
            answer = body.get('answer', None)
            category = body.get('category', None)
            difficulty = body.get('difficulty', None)
            
            # Validate required fields
            if not all([question_text, answer, category, difficulty]):
                abort(400)
            
            question = Question(
                question=question_text,
                answer=answer,
                category=category,
                difficulty=difficulty
            )
            question.insert()
            
            return jsonify({
                'success': True,
                'created': question.id
            })
        except Exception as e:
            if hasattr(e, 'code') and e.code == 400:
                abort(400)
            abort(422)

    """
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.
    """
    def search_questions(search_term):
        try:
            questions = Question.query.filter(
                Question.question.ilike(f'%{search_term}%')
            ).all()
            
            formatted_questions = [question.format() for question in questions]
            
            return jsonify({
                'success': True,
                'questions': formatted_questions,
                'total_questions': len(formatted_questions),
                'current_category': None
            })
        except Exception as e:
            abort(422)

    """
    Create a GET endpoint to get questions based on category.
    """
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_questions_by_category(category_id):
        try:
            category = Category.query.get(category_id)
            
            if category is None:
                abort(404)
            
            questions = Question.query.filter(Question.category == category_id).all()
            formatted_questions = [question.format() for question in questions]
            
            return jsonify({
                'success': True,
                'questions': formatted_questions,
                'total_questions': len(formatted_questions),
                'current_category': category.type
            })
        except Exception as e:
            if hasattr(e, 'code') and e.code == 404:
                abort(404)
            abort(422)

    """
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.
    """
    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        try:
            body = request.get_json()
            previous_questions = body.get('previous_questions', [])
            quiz_category = body.get('quiz_category', None)
            
            if quiz_category and quiz_category['id'] != 0:
                questions = Question.query.filter(
                    Question.category == quiz_category['id']
                ).filter(
                    Question.id.notin_(previous_questions)
                ).all()
            else:
                questions = Question.query.filter(
                    Question.id.notin_(previous_questions)
                ).all()
            
            if len(questions) == 0:
                return jsonify({
                    'success': True,
                    'question': None
                })
            
            random_question = random.choice(questions)
            
            return jsonify({
                'success': True,
                'question': random_question.format()
            })
        except Exception as e:
            abort(422)

    """
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable entity'
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal server error'
        }), 500

    return app

