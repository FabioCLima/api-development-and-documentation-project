# Project Enhancement Suggestions

This document outlines three enhancement suggestions to make the Trivia API project stand out. Each enhancement is optional and can be implemented independently or in combination.

---

## 🎯 Enhancement Overview

### 1. ✅ Easy: Add Rating Field to Questions
**Difficulty:** Easy  
**Impact:** Medium  
**Files to Modify:** 5-7 files

### 2. 🔥 Intensive: Add Users and Track Scores
**Difficulty:** Intensive  
**Impact:** High  
**Files to Modify:** 10+ files

### 3. 📝 Medium: Add New Category Creation
**Difficulty:** Medium  
**Impact:** Low-Medium  
**Files to Modify:** 4-6 files

---

## 1. 📊 Add Rating Field to Questions

### Overview
Add an additional `rating` field to questions that allows users to rate questions (e.g., 1-5 stars).

### Implementation Steps

#### Step 1: Update Database Model
**File:** `backend/models.py`

```python
class Question(db.Model):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    category = Column(String, nullable=False)
    difficulty = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=True, default=0)  # Add this

    def __init__(self, question, answer, category, difficulty, rating=0):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty
        self.rating = rating  # Add this

    def format(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'category': self.category,
            'difficulty': self.difficulty,
            'rating': self.rating  # Add this
        }
```

#### Step 2: Create Database Migration
**File:** Create `backend/migrations/add_rating.py` (optional, or use SQL)

```sql
ALTER TABLE questions ADD COLUMN rating INTEGER DEFAULT 0;
```

Or run directly:
```bash
docker compose exec db psql -U postgres -d trivia -c "ALTER TABLE questions ADD COLUMN rating INTEGER DEFAULT 0;"
```

#### Step 3: Update API Endpoints
**File:** `backend/flaskr/__init__.py`

Update the POST /questions endpoint to accept rating:

```python
@app.route('/questions', methods=['POST'])
def create_question():
    try:
        body = request.get_json()
        
        if 'searchTerm' in body:
            # Search logic...
            pass
        else:
            # Extract data including rating
            question = body.get('question')
            answer = body.get('answer')
            category = body.get('category')
            difficulty = body.get('difficulty')
            rating = body.get('rating', 0)  # Add this, default to 0
            
            if not all([question, answer, category, difficulty]):
                abort(400)
            
            new_question = Question(
                question=question,
                answer=answer,
                category=category,
                difficulty=difficulty,
                rating=rating  # Add this
            )
            
            new_question.insert()
            
            return jsonify({
                'success': True,
                'created': new_question.id
            })
    except Exception as e:
        abort(422)
```

#### Step 4: Update Frontend Form
**File:** `frontend/src/components/FormView.js`

```jsx
render() {
    return (
        <div id='add-form'>
            <h2>Add a New Trivia Question</h2>
            <form className='form-view' id='add-question-form' onSubmit={this.submitQuestion}>
                {/* Existing fields... */}
                
                {/* Add Rating Field */}
                <label>
                    Rating
                    <select name='rating' onChange={this.handleChange}>
                        <option value='0'>Not Rated</option>
                        <option value='1'>1 Star</option>
                        <option value='2'>2 Stars</option>
                        <option value='3'>3 Stars</option>
                        <option value='4'>4 Stars</option>
                        <option value='5'>5 Stars</option>
                    </select>
                </label>
                
                <input type='submit' className='button' value='Submit' />
            </form>
        </div>
    );
}
```

#### Step 5: Update Question Display
**File:** `frontend/src/components/Question.js`

```jsx
render() {
    const { question, answer, category, difficulty, rating } = this.props;
    return (
        <div className='Question-holder'>
            <div className='Question'>{question}</div>
            <div className='Question-status'>
                {/* Add rating display */}
                {rating > 0 && (
                    <div className='rating'>
                        {'⭐'.repeat(rating)} ({rating}/5)
                    </div>
                )}
                {/* Other fields... */}
            </div>
        </div>
    );
}
```

#### Step 6: Update Tests
**File:** `backend/test_flaskr.py`

```python
def test_create_question_with_rating(self):
    """Test POST /questions - create question with rating"""
    new_question = {
        'question': 'Test question?',
        'answer': 'Test answer',
        'category': 3,
        'difficulty': 1,
        'rating': 4
    }
    res = self.client.post('/questions', 
                          data=json.dumps(new_question),
                          content_type='application/json')
    data = json.loads(res.data)
    
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
```

### Files to Modify
1. `backend/models.py` - Add rating field
2. `backend/flaskr/__init__.py` - Update create endpoint
3. `frontend/src/components/FormView.js` - Add rating input
4. `frontend/src/components/Question.js` - Display rating
5. `backend/test_flaskr.py` - Add rating tests
6. Database migration SQL file

---

## 2. 👥 Add Users and Track Scores (INTENSIVE)

### Overview
Add user authentication and track individual game scores.

### Implementation Steps

#### Step 1: Create User Model
**File:** `backend/models.py`

```python
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def format(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

class Score(db.Model):
    __tablename__ = 'scores'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, db.ForeignKey('users.id'), nullable=False)
    score = Column(Integer, nullable=False)
    category = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __init__(self, user_id, score, category=None):
        self.user_id = user_id
        self.score = score
        self.category = category
    
    def format(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'score': self.score,
            'category': self.category,
            'created_at': self.created_at.isoformat()
        }
```

#### Step 2: Create Database Migration
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE scores (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    score INTEGER NOT NULL,
    category INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_scores_user_id ON scores(user_id);
CREATE INDEX idx_scores_score ON scores(score DESC);
```

#### Step 3: Add User Endpoints
**File:** `backend/flaskr/__init__.py`

```python
@app.route('/users', methods=['POST'])
def create_user():
    try:
        body = request.get_json()
        username = body.get('username')
        email = body.get('email')
        
        if not username or not email:
            abort(400)
        
        # Check if user exists
        existing_user = User.query.filter(
            db.or_(User.username == username, User.email == email)
        ).first()
        
        if existing_user:
            abort(422)
        
        user = User(username=username, email=email)
        user.insert()
        
        return jsonify({
            'success': True,
            'user': user.format()
        })
    except Exception as e:
        abort(422)

@app.route('/users/<int:user_id>/scores', methods=['POST'])
def create_score(user_id):
    try:
        body = request.get_json()
        score = body.get('score')
        category = body.get('category')
        
        if score is None:
            abort(400)
        
        new_score = Score(user_id=user_id, score=score, category=category)
        new_score.insert()
        
        return jsonify({
            'success': True,
            'score': new_score.format()
        })
    except Exception as e:
        abort(422)

@app.route('/users/<int:user_id>/scores', methods=['GET'])
def get_user_scores(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            abort(404)
        
        scores = Score.query.filter(Score.user_id == user_id).order_by(Score.score.desc()).all()
        formatted_scores = [score.format() for score in scores]
        
        return jsonify({
            'success': True,
            'scores': formatted_scores,
            'total_scores': len(formatted_scores)
        })
    except Exception as e:
        abort(422)

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    try:
        limit = request.args.get('limit', 10, type=int)
        
        # Get top scores with user information
        top_scores = db.session.query(
            Score, User
        ).join(
            User, Score.user_id == User.id
        ).order_by(
            Score.score.desc()
        ).limit(limit).all()
        
        leaderboard = [{
            'username': user.username,
            'score': score.score,
            'category': score.category,
            'date': score.created_at.isoformat()
        } for score, user in top_scores]
        
        return jsonify({
            'success': True,
            'leaderboard': leaderboard
        })
    except Exception as e:
        abort(422)
```

#### Step 4: Update Quiz Endpoint to Track Scores
**File:** `backend/flaskr/__init__.py`

Modify POST /quizzes to optionally accept user_id and track final score:

```python
@app.route('/quizzes', methods=['POST'])
def play_quiz():
    try:
        body = request.get_json()
        previous_questions = body.get('previous_questions', [])
        quiz_category = body.get('quiz_category', None)
        user_id = body.get('user_id', None)  # Add this
        final_score = body.get('final_score', None)  # Add this
        
        # If final_score is provided, save it
        if final_score is not None and user_id:
            score = Score(
                user_id=user_id,
                score=final_score,
                category=quiz_category['id'] if quiz_category and quiz_category['id'] != 0 else None
            )
            score.insert()
        
        # Rest of quiz logic...
```

#### Step 5: Add Frontend User Management
**New File:** `frontend/src/components/UserRegistration.js`

```jsx
import React, { Component } from 'react';
import $ from 'jquery';

class UserRegistration extends Component {
    state = {
        username: '',
        email: ''
    };
    
    handleSubmit = (event) => {
        event.preventDefault();
        $.ajax({
            url: '/users',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(this.state),
            success: (result) => {
                localStorage.setItem('userId', result.user.id);
                alert('User created successfully!');
            },
            error: () => {
                alert('Failed to create user');
            }
        });
    };
    
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <input 
                    type="text" 
                    placeholder="Username"
                    onChange={(e) => this.setState({username: e.target.value})}
                />
                <input 
                    type="email" 
                    placeholder="Email"
                    onChange={(e) => this.setState({email: e.target.value})}
                />
                <button type="submit">Register</button>
            </form>
        );
    }
}
```

#### Step 6: Update Tests
**File:** `backend/test_flaskr.py`

Add tests for user and score endpoints.

### Files to Modify
1. `backend/models.py` - Add User and Score models
2. `backend/flaskr/__init__.py` - Add user/score endpoints
3. `frontend/src/components/UserRegistration.js` - New component
4. `frontend/src/components/QuizView.js` - Track scores
5. `backend/test_flaskr.py` - Add user/score tests
6. Database migration files

---

## 3. 📂 Add New Category Creation

### Overview
Allow users to create new categories for questions.

### Implementation Steps

#### Step 1: Add Create Category Endpoint
**File:** `backend/flaskr/__init__.py`

```python
@app.route('/categories', methods=['POST'])
def create_category():
    try:
        body = request.get_json()
        category_type = body.get('type')
        
        if not category_type:
            abort(400)
        
        # Check if category exists
        existing_category = Category.query.filter(Category.type == category_type).first()
        if existing_category:
            abort(422)
        
        new_category = Category(type=category_type)
        new_category.insert()
        
        return jsonify({
            'success': True,
            'created': new_category.id,
            'category': new_category.format()
        })
    except Exception as e:
        abort(422)
```

#### Step 2: Add Delete Category Endpoint (Optional)
```python
@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        category = Category.query.get(category_id)
        
        if category is None:
            abort(404)
        
        # Check if category has questions
        question_count = Question.query.filter(Question.category == category_id).count()
        if question_count > 0:
            return jsonify({
                'success': False,
                'error': 422,
                'message': f'Cannot delete category with {question_count} questions'
            }), 422
        
        category_type = category.type
        db.session.delete(category)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'deleted': category_id,
            'type': category_type
        })
    except Exception as e:
        abort(422)
```

#### Step 3: Add Frontend Category Creation Form
**File:** `frontend/src/components/CategoryForm.js`

```jsx
import React, { Component } from 'react';
import $ from 'jquery';

class CategoryForm extends Component {
    state = {
        categoryName: ''
    };
    
    handleSubmit = (event) => {
        event.preventDefault();
        
        $.ajax({
            url: '/categories',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({type: this.state.categoryName}),
            success: () => {
                alert('Category created successfully!');
                this.setState({categoryName: ''});
            },
            error: () => {
                alert('Failed to create category');
            }
        });
    };
    
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <input 
                    type="text" 
                    placeholder="Category Name"
                    value={this.state.categoryName}
                    onChange={(e) => this.setState({categoryName: e.target.value})}
                />
                <button type="submit">Add Category</button>
            </form>
        );
    }
}
```

#### Step 4: Add Tests
**File:** `backend/test_flaskr.py`

```python
def test_create_category(self):
    """Test POST /categories - create category"""
    res = self.client.post('/categories',
                          data=json.dumps({'type': 'Music'}),
                          content_type='application/json')
    data = json.loads(res.data)
    
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['created'])

def test_delete_category(self):
    """Test DELETE /categories/<id>"""
    # First create a category
    category = Category(type='Test Category')
    with self.app.app_context():
        category.insert()
        category_id = category.id
    
    # Delete it
    res = self.client.delete(f'/categories/{category_id}')
    data = json.loads(res.data)
    
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
```

### Files to Modify
1. `backend/flaskr/__init__.py` - Add create/delete endpoints
2. `frontend/src/components/CategoryForm.js` - New component
3. `backend/test_flaskr.py` - Add category tests
4. Update frontend to include category form

---

## 📝 Summary

### Recommended Implementation Order

1. **Start with Rating Field** (Easiest)
   - Quick to implement
   - Good learning exercise
   - Minimal code changes

2. **Add Category Creation** (Medium)
   - Useful feature
   - Moderate complexity
   - Good API design practice

3. **Implement User Tracking** (Most Intensive)
   - Most significant enhancement
   - Requires most planning
   - Adds significant value

### Testing Requirements

For each enhancement:
- Write unit tests for new endpoints
- Update existing tests if needed
- Test database migrations
- Verify frontend integration

### Documentation

Remember to update:
- API documentation in README
- Test documentation
- Database schema documentation

---

**Good luck with your enhancements! 🚀**
