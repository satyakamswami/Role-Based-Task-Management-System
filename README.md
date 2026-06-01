# Backend Developer Internship Assignment

## Tech Stack
* **Backend:** Python, FastAPI, PostgreSQL, SQLAlchemy, JWT Auth
* **Frontend:** Vanilla HTML, CSS, JavaScript (Fetch API)

## Setup Instructions

### 1. Backend Setup
1. Navigate to the `backend` folder: `cd backend`
2. Create a virtual environment: `python -m venv venv`
3. Activate it:
   * Windows: `venv\Scripts\activate`
   * Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file and add your PostgreSQL `DATABASE_URL` and a secret `SECRET_KEY`.
6. Run the server: `uvicorn main:app --reload`
7. API Documentation is automatically generated at: `http://localhost:8000/docs`

### 2. Frontend Setup
1. Simply open the `frontend/index.html` file in any modern web browser. No server setup is required.
2. Register an account, log in, and manage your tasks via the protected dashboard.
