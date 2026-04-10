# 📚 Assignment Submission API (FastAPI + Firebase)

## 🚀 Overview
This project is a backend API built using FastAPI and Firebase Firestore for managing an assignment system. It allows students to submit assignments, and teachers to grade them. Authentication is handled using Firebase Email/Password with token-based login.

---

## 📦 Dependencies

pip install example

1) fastapi  
2) uvicorn  
3) pyrebase4  
4) firebase_admin  

---

## 🛣️ Routers

@router.post('/signup')  
@router.post('/login')  
@router.post('/ping')  

async def validate_token()

---

## 🔥 Firebase Setup

### 1) Create a project in Firebase

Authentication  
Project setting > service account > Python => copy code (paste in firebase file of project in vscode)  
Generate api key > rename serviceAccount.json and paste in root  

---

### 2) Add new web app

name: fastapiauth  
config > copy and paste in firebase file or env and make the code firebaseConfig JSON by adding double quotes  

do add  
"database_URL": ""  

---

## 🧠 Models
signup and login  

---

## 📚 Assignment Submission API (FastAPI + Firebase)

## 🚀 Overview
This project is a backend API built using FastAPI and Firebase Firestore for managing an assignment system. It allows students to submit assignments, and teachers to grade them. Authentication is handled using Firebase Email/Password with token-based login.

---

## ✨ Features

👨‍🎓 Student  
- Sign up using email & password  
- Login and receive authentication token  
- Submit assignments  
- View submitted assignments (without grades)  

👨‍🏫 Teacher  
- Login using email & password  
- View student submissions  
- Assign grades to submissions  

---

## 🏗️ Tech Stack
- FastAPI  
- Firebase Authentication  
- Firebase Firestore  
- Python  
- Uvicorn  

---

## 🔐 Authentication
- Firebase Email/Password authentication is used  
- On login, a Firebase ID token is generated  
- This token is used for protected routes (future improvement: middleware validation)  

⚠️ Note: Password hashing (bcrypt) is not implemented because Firebase handles authentication securely.

---

## 📌 API Endpoints

POST /signup → user signup  
POST /login → user login  
POST /ping → health check  

---

## 📂 Notes
- Firebase handles authentication securely  
- Firestore is used for storing assignments and submissions  
- Token-based authentication is used for protected routes  

---
