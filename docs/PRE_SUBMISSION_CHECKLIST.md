# Pre-Submission Review Checklist

## ✅ Checklist Before Submission

Use this checklist to ensure your project is ready for submission and evaluation.

---

## 📋 1. Code Quality & Documentation

### Documentation Requirements
- [ ] **README.md exists** in project root with complete documentation
  - [ ] Installation instructions for dependencies
  - [ ] Instructions for running the development server
  - [ ] API endpoint documentation with URL, request parameters, and response body
  - [ ] Project structure overview
  
- [ ] **Code Documentation**
  - [ ] Clear variable and function names
  - [ ] Adequate code comments
  - [ ] Follows PEP 8 style guide
  
- [ ] **Environment Control**
  - [ ] `.gitignore` includes virtual environment directories
  - [ ] `.gitignore` excludes local environment files
  - [ ] No secrets or credentials in code
  - [ ] Environment variables properly configured

### Code Review Checklist
- [ ] All code follows Python best practices
- [ ] No TODO comments in submitted code
- [ ] Endpoints are logically named following REST conventions
- [ ] Error handling is comprehensive

---

## 🔗 2. HTTP Request Handling

### RESTful Principles
- [ ] **Endpoints properly named** (e.g., `/questions`, `/categories`)
- [ ] **Correct HTTP methods used:**
  - [ ] GET for retrieving data
  - [ ] POST for creating/searching data
  - [ ] DELETE for removing data

### Endpoint Implementation
- [ ] **GET /categories** - Returns all categories
- [ ] **GET /questions** - Returns paginated questions (10 per page)
- [ ] **DELETE /questions/<id>** - Deletes a question
- [ ] **POST /questions** - Creates a new question
- [ ] **POST /questions** - Searches for questions by term
- [ ] **GET /categories/<id>/questions** - Gets questions by category
- [ ] **POST /quizzes** - Plays quiz game with random questions

### Error Handling
- [ ] **Error handlers implemented** using `@app.errorhandler` decorator:
  - [ ] 400 Bad Request handler
  - [ ] 404 Not Found handler
  - [ ] 422 Unprocessable Entity handler
  - [ ] 500 Internal Server Error handler
- [ ] **Error responses formatted as JSON**
- [ ] All error handlers return consistent format

---

## 🧪 3. Testing & API Documentation

### Test Requirements
- [ ] **Uses unittest library** for testing
- [ ] **Test file:** `backend/test_flaskr.py` exists
- [ ] **All tests pass** (run: `python test_flaskr.py`)
- [ ] **Test coverage:**
  - [ ] At least one success test for each endpoint
  - [ ] At least one error test for applicable endpoints
- [ ] **Tests verify CRUD operations:**
  - [ ] CREATE (POST) operations verified
  - [ ] READ (GET) operations verified
  - [ ] DELETE operations verified

### Test Execution
```bash
cd backend
python test_flaskr.py
```
Expected result: All tests pass ✅

---

## 📚 4. API Documentation

### Endpoint Documentation
Each endpoint must be documented in `README.md` with:

#### GET /categories
- [ ] URL documented
- [ ] Request arguments documented
- [ ] Response body format documented
- [ ] Example JSON response provided

#### GET /questions
- [ ] URL documented
- [ ] Query parameters documented (page number)
- [ ] Response body format documented
- [ ] Example JSON response provided

#### DELETE /questions/<id>
- [ ] URL with parameter documented
- [ ] Success response documented
- [ ] Error response documented (404)
- [ ] Example JSON responses provided

#### POST /questions (Create)
- [ ] URL documented
- [ ] Request body format documented
- [ ] Required fields documented
- [ ] Success response documented
- [ ] Example JSON request/response provided

#### POST /questions (Search)
- [ ] URL documented
- [ ] Request body format documented
- [ ] Success response documented
- [ ] Example JSON request/response provided

#### GET /categories/<id>/questions
- [ ] URL with parameter documented
- [ ] Response body format documented
- [ ] Success and error responses documented
- [ ] Example JSON responses provided

#### POST /quizzes
- [ ] URL documented
- [ ] Request body format documented
- [ ] Response body format documented
- [ ] Example JSON request/response provided

---

## 🗄️ 5. Database & Models

### Database Setup
- [ ] **Database schema** properly defined in `backend/models.py`
- [ ] **SQLAlchemy models** correctly configured:
  - [ ] Question model with proper fields
  - [ ] Category model with proper fields
  - [ ] Models have proper relationships

### Database Operations
- [ ] Models have `insert()`, `update()`, `delete()`, and `format()` methods
- [ ] Database connection properly configured
- [ ] Test database (`trivia_test`) can be created
- [ ] Schema can be loaded from `trivia.psql`

---

## 🚀 6. Application Functionality

### Backend Setup
- [ ] **Flask application** starts without errors
- [ ] **CORS** properly configured for frontend
- [ ] **Environment variables** set up correctly
- [ ] **Database connection** works

### Frontend Integration
- [ ] Frontend can connect to backend
- [ ] All API endpoints work from frontend
- [ ] CORS allows frontend requests
- [ ] No console errors in browser

### Core Functionality
- [ ] View questions with pagination works
- [ ] Add new questions works
- [ ] Delete questions works
- [ ] Search questions works
- [ ] Filter by category works
- [ ] Play quiz game works

---

## 📁 7. Project Structure

### Required Files
- [ ] `backend/flaskr/__init__.py` - Main Flask application
- [ ] `backend/models.py` - Database models
- [ ] `backend/test_flaskr.py` - Test suite
- [ ] `backend/trivia.psql` - Database schema
- [ ] `backend/requirements.txt` - Python dependencies
- [ ] `frontend/src/` - Frontend React application
- [ ] `README.md` - Main documentation
- [ ] `.gitignore` - Git ignore file

### File Organization
- [ ] No unnecessary files committed
- [ ] Documentation organized in `docs/` folder
- [ ] Code is properly structured
- [ ] No hardcoded credentials

---

## 🧹 8. Code Cleanup

### Before Submission
- [ ] **Remove all TODO comments**
- [ ] **Remove debug print statements**
- [ ] **Remove commented-out code** unless for reference
- [ ] **Ensure all imports are used**
- [ ] **No syntax errors or warnings**
- [ ] **Code is properly formatted**

### Environment
- [ ] Virtual environment is in `.gitignore`
- [ ] `__pycache__` directories are in `.gitignore`
- [ ] `.env` files are in `.gitignore`
- [ ] Test database credentials are in `.gitignore`

---

## 🎯 9. Final Verification

### Manual Testing
- [ ] **Start the Flask server** - Does it start without errors?
- [ ] **Run all tests** - Do all tests pass?
- [ ] **Test each endpoint** - Do they return expected responses?
- [ ] **Test error handling** - Do error handlers work?
- [ ] **Frontend loads** - Does the React app load?
- [ ] **Frontend-Backend communication** - Do they communicate correctly?

### Documentation Review
- [ ] README.md is complete and accurate
- [ ] All API endpoints are documented
- [ ] Installation instructions are clear
- [ ] Examples are provided for each endpoint
- [ ] No broken links or formatting issues

### Git Commit
- [ ] All changes are committed
- [ ] Commit messages are meaningful
- [ ] Ready to push to remote repository

---

## 📝 10. Submission Readiness

### Pre-Submission Checklist
- [ ] All code is committed and pushed to GitHub
- [ ] Repository is public (if required)
- [ ] README.md is complete
- [ ] All tests pass locally
- [ ] Application runs without errors
- [ ] Documentation is complete

### Quick Test Command
```bash
# Run all tests
cd backend
python test_flaskr.py

# Expected output: All tests pass
```

---

## 🚨 Common Issues to Check

### Backend Issues
- [ ] Port 5000 is available
- [ ] Database is running (Docker container)
- [ ] Environment variables are set
- [ ] Virtual environment is activated
- [ ] All dependencies are installed

### Testing Issues
- [ ] Test database exists (`trivia_test`)
- [ ] Test database is populated
- [ ] No test data conflicts
- [ ] Tests run in correct order

### Frontend Issues
- [ ] Node modules installed (`npm install`)
- [ ] React app starts without errors
- [ ] Proxy configuration is correct
- [ ] CORS headers are received

---

## ✅ Final Sign-Off

### Ready for Submission?
- [ ] All checklist items completed
- [ ] All tests passing (15/15)
- [ ] All endpoints working
- [ ] Documentation complete
- [ ] Code is clean and professional
- [ ] No errors or warnings

### Submission Information
- **Repository URL:** _____________________
- **Branch:** _____________________
- **Last Commit:** _____________________

---

## 🎓 Evaluation Criteria Reminder

Your project will be evaluated on:

1. **Code Quality & Documentation** - Clean, well-documented code
2. **HTTP Request Handling** - RESTful design, proper HTTP methods
3. **Testing** - Unit tests covering all endpoints
4. **Error Handling** - Comprehensive error handlers
5. **API Documentation** - Complete endpoint documentation
6. **Functionality** - All required features working

---

## 📞 Support

If you encounter issues during review:
1. Check the error messages carefully
2. Review the documentation in `docs/`
3. Verify environment setup
4. Check test output for specific failures
5. Review server logs for backend issues

---

**Good luck with your submission! 🚀**
