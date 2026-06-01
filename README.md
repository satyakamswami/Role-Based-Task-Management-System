# 🚀 Role-Based Task Management System

A full-stack REST API built with FastAPI, featuring secure JWT authentication, role-based access control, and a Vanilla JavaScript frontend. Built as a backend developer internship assignment.

---

# 🛠 Tech Stack

* **Backend:** Python, FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication (`python-jose`, `passlib`)
* **Frontend:** Vanilla HTML, CSS, JavaScript (Fetch API)

---

# 📁 Project Structure

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

---

# ✨ Features

* **User Authentication:** Secure registration and login using hashed passwords (bcrypt) and JSON Web Tokens (JWT).
* **Role-Based Access Control (RBAC):** Automatic role assignment:

  * The first registered user becomes an **Admin**
  * All subsequent users become normal **Users**
* **Task Management (CRUD):** Users can safely create, read, and delete their own tasks.
* **Auto-generated Documentation:** Interactive Swagger UI provided out-of-the-box by FastAPI.

---

# ⚙️ Setup Instructions

## 1. Backend Setup

### Step 1: Navigate to the backend directory

```bash
cd backend
```

### Step 2: Create and activate a virtual environment

```bash
python -m venv venv
```

#### On Windows

```bash
venv\Scripts\activate
```

#### On Mac/Linux

```bash
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure environment variables

Create a `.env` file inside the `backend` folder and add:

```env
DATABASE_URL=your_postgresql_connection_string
SECRET_KEY=your_secret_key
```

You can use `.env.example` as a reference.

### Step 5: Run the server

```bash
uvicorn main:app --reload
```

### Step 6: Open API Documentation

Once the server is running, visit:

```text
http://localhost:8000/docs
```

---

# 🌐 Frontend Setup

1. No local server setup or `npm install` is required.
2. Open the `frontend/index.html` file directly in any modern browser.
3. Register a new account, log in, and start managing tasks from the dashboard.

---

# 📌 Notes

* Ensure PostgreSQL is installed and running before starting the backend server.
* Make sure the database specified in `DATABASE_URL` already exists.
* The frontend communicates with the FastAPI backend using the Fetch API.

---

# 📄 License

This project is built for educational and internship assignment purposes.
