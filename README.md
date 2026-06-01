```markdown
# 🚀 Role-Based Task Management System

A full-stack REST API built with FastAPI, featuring secure JWT authentication, role-based access control, and a Vanilla JavaScript frontend. Built as a backend developer internship assignment.

## 🛠 Tech Stack

* **Backend:** Python, FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication (via `python-jose` and `passlib`)
* **Frontend:** Vanilla HTML, CSS, JavaScript (Fetch API)

## 📁 Project Structure

This project follows a modular backend architecture for separation of concerns and scalability:

```text
├── backend/
│   ├── .env.example      # Template for environment variables
│   ├── requirements.txt  # Python dependencies
│   ├── database.py       # PostgreSQL connection setup
│   ├── models.py         # SQLAlchemy database tables
│   ├── schemas.py        # Pydantic models for data validation
│   ├── auth.py           # Password hashing and JWT logic
│   └── main.py           # FastAPI application and route endpoints
│
└── frontend/
    ├── index.html        # Authentication UI (Login/Register)
    ├── dashboard.html    # Protected Task Management UI
    └── style.css         # UI Styling

```

## ✨ Features

* **User Authentication:** Secure registration and login using hashed passwords (bcrypt) and JSON Web Tokens (JWT).
* **Role-Based Access Control (RBAC):** Automatic role assignment (the first registered user becomes an Admin, subsequent users are normal Users).
* **Task Management (CRUD):** Users can safely create, read, and delete their own tasks.
* **Auto-generated Documentation:** Interactive Swagger UI provided out-of-the-box by FastAPI.

---

## ⚙️ Setup Instructions

### 1. Backend Setup

**1. Navigate to the backend directory:**

```bash
cd backend

```

**2. Create and activate a virtual environment:**

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

```

**3. Install dependencies:**

```bash
pip install -r requirements.txt

```

**4. Configure environment variables:**
Create a file named `.env` in the `backend` folder and add your database credentials (you can reference `.env.example`):

```env
DATABASE_URL=your_postgresql_connection_string
SECRET_KEY=your_secret_key

```

**5. Run the server:**

```bash
uvicorn main:app --reload

```

**6. View API Documentation:**
FastAPI automatically generates interactive API documentation. Once the server is running, visit:
🔗 [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)

---

### 2. Frontend Setup

1. No local server setup or `npm install` is required for the frontend.
2. Locate the `frontend/index.html` file in your file explorer and double-click to open it directly in any modern web browser.
3. Register a new account, log in, and begin managing tasks via the protected dashboard.

```

```
