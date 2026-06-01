```markdown
# 🚀 Role-Based Task Management System

A full-stack REST API built with FastAPI, featuring secure JWT authentication, role-based access control, and a Vanilla JavaScript frontend. Built as a backend developer internship assignment.

## 🛠 Tech Stack

* **Backend:** Python, FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication (via `python-jose` and `passlib`)
* **Frontend:** Vanilla HTML, CSS, JavaScript (Fetch API)

## ✨ Features

* **User Authentication:** Secure registration and login using hashed passwords (bcrypt) and JSON Web Tokens (JWT).
* **Role-Based Access Control (RBAC):** Automatic role assignment (Admin vs. User). 
* **Task Management (CRUD):** Users can create, read, and delete their own tasks securely.
* **Stateless Architecture:** Fully decoupled backend API and frontend client.
* **Auto-generated Documentation:** Interactive Swagger UI provided out-of-the-box by FastAPI.

---

## ⚙️ Setup Instructions

### 1. Backend Setup

**1. Navigate to the backend directory:**
```bash
cd backend

```

**2. Create a virtual environment:**

```bash
python -m venv venv

```

**3. Activate the virtual environment:**

* **Windows:** `venv\Scripts\activate`
* **Mac/Linux:** `source venv/bin/activate`

**4. Install dependencies:**

```bash
pip install -r requirements.txt

```

**5. Configure environment variables:**
Create a file named `.env` in the root folder and add your database credentials (see `.env.example` for reference):

```env
DATABASE_URL=your_postgresql_connection_string
SECRET_KEY=your_secret_key

```

**6. Run the server:**

```bash
uvicorn main:app --reload

```

**7. View API Documentation:**
FastAPI automatically generates interactive API documentation. Once the server is running, visit:
🔗 [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)

---

### 2. Frontend Setup

1. No local server setup or `npm install` is required for the frontend.
2. Locate the `frontend/index.html` file in your file explorer and open it directly in any modern web browser.
3. Register a new account, log in, and begin managing tasks via the protected dashboard.

```

```
