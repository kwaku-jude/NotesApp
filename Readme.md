# 📒 EduNotes - Student Note-Taking Management System

EduNotes is a web-based API built with **Django REST Framework** that allows students to efficiently manage, organize, and share academic notes.  
The system provides authentication, academic categorization, and note management features.

---

## 🚀 Features

- User **registration, login, and logout** with JWT authentication  
- Create, read, update, and delete **notes**  
- Organize notes by **academic level, course, lecturer**  
- Add **tags** to notes  
- Public or private visibility control  
- API documentation with **drf-spectacular**

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/notesapp.git
   cd notesapp
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the server:
   ```bash
   python manage.py runserver
   ```

---

## 🔐 Authentication

The NotesApp supports **user authentication** using JWT tokens. Base URL (local):

```
http://127.0.0.1:8000/api/accounts/
```

### 📌 Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/accounts/register/` | Register a new user |
| POST | `/api/accounts/login/` | Login and get tokens |
| POST | `/api/accounts/logout/` | Logout user |

### 📝 Register

**Request:**
```http
POST http://127.0.0.1:8000/api/accounts/register/
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "username": "student01",
  "email": "student01@example.com",
  "password": "strongpassword123"
}
```

**Response:**
```json
{
  "message": "User registered successfully.",
  "user": {
    "id": 1,
    "username": "student01",
    "email": "student01@example.com"
  }
}
```

### 🔑 Login

**Request:**
```http
POST http://127.0.0.1:8000/api/accounts/login/
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "username": "student01",
  "password": "strongpassword123"
}
```

**Response (JWT):**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1...",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVC..."
}
```

### 🚪 Logout

**Request:**
```http
POST http://127.0.0.1:8000/api/accounts/logout/
Authorization: Bearer <access_token>
Content-Type: application/json
```

**Response:**
```json
{
  "message": "Successfully logged out."
}
```

---

## 📝 Notes API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/notes/` | List all notes |
| POST | `/api/notes/` | Create a new note |
| GET | `/api/notes/{id}/` | Retrieve a single note |
| PUT | `/api/notes/{id}/` | Update a note |
| DELETE | `/api/notes/{id}/` | Delete a note |

### Example **Create Note** request:

**Request:**
```http
POST http://127.0.0.1:8000/api/notes/
Authorization: Bearer <access_token>
Content-Type: application/json
```

**Body:**
```json
{
  "title": "Lecture 1 - Introduction",
  "content": "This is my note for lecture 1.",
  "level": 1,
  "course": 2,
  "lecturer": 1,
  "tags": "intro,basics",
  "is_public": true
}
```

---

## 📚 API Documentation

After running the server, view interactive API docs at:
* Swagger UI → `http://127.0.0.1:8000/api/schema/swagger-ui/`
* ReDoc → `http://127.0.0.1:8000/api/schema/redoc/`

---

## 🛠️ Tech Stack

* Django 5.2.5
* Django REST Framework
* JWT Authentication (SimpleJWT)
* PostgreSQL / SQLite
* drf-spectacular for docs

---

## 👨‍💻 Author

**Tanson Jude Antwi**