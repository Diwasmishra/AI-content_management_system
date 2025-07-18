# AI-Based Content Management System (Next.js + Django + MySQL + Mistral 7B)

An intelligent, role-based content management platform that combines a modern Next.js frontend, a powerful Django backend, a MySQL database, and AI integration via Mistral 7B hosted locally through LM Studio. Built to streamline article workflows with AI-powered writing assistance — all in a seamless full-stack solution.

## 🔧 Tech Stack

| Layer      | Tech Used                                        |
|------------|--------------------------------------------------|
| Frontend   | Next.js, Tailwind CSS                            |
| Backend    | Django REST Framework                            |
| Database   | MySQL                                            |
| AI Layer   | LM Studio with `mistral-7b-instruct-v0.2` model  |
| Dev Tools  | Git, REST APIs, .env, VS Code                    |

## ✨ Features

- 🧠 AI-generated responses using Mistral 7B via LM Studio  
- 👥 Role-based dashboards for Admin, Reviewer, and Author  
- ✅ Add, review, approve, and publish articles  
- 📊 Filter articles by category, status, date, and author  
- 🔄 Backend APIs with Django REST Framework  
- 🎨 Responsive UI with Tailwind CSS  
- 🔐 Environment variables managed with `.env`  

---

## 🗂️ Folder Structure

```
AICMS/
├── frontend/ # Next.js frontend
│ ├── pages/ # Routes for each role dashboard
│ ├── components/ # Reusable UI components
│ └── utils/ai.js # Connects frontend to local LM Studio
├── backend/ # Django backend
│ ├── cmsapi/ # Article APIs and logic
│ ├── users/ # Role-based auth system
│ ├── ai_integration/ # LM Studio connection code
│ └── .env # DB and config secrets (git-ignored)
└── README.md
```

---

## 🧠 How AI Integration Works

- LM Studio runs locally at `http://localhost:1234`  
- Frontend sends article prompts or queries to this local server  
- Mistral 7B (`mistral-7b-instruct-v0.2`) responds with suggestions or summaries  
- AI assists authors in drafting and refining content
- 
> 💡 No external OpenAI API needed. Completely free, offline, and secure.

---

## 🧪 Setup Guide

### 1. Clone the Repo

```bash
git clone https://github.com/Diwasmishra/<repo-name>.git
cd AICMS
```

### 2. Backend (Django + MySQL)
```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # or source venv/bin/activate (Linux/Mac)
```
### 3. Install Requirements
```bash
pip install -r requirements.txt
```
### 4. 🔐 Configure MySQL & .env
```bash
DB_NAME=your_db_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```
### 5. Migrate & Run the Backend
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### 6. Frontend (Next.js + Tailwind)
```bash
cd ../frontend
npm install
npm run dev
```
App runs at: http://localhost:3000
### 7. Run LM Studio (AI Assistant)

 - Download from https://lmstudio.ai

 - Load mistral-7b-instruct-v0.2 GGUF model

 - Enable API server on http://localhost:1234

 - Keep LM Studio running while using the app

---

## 🧹 Best Practices Followed

#### 1] .env file is excluded from version control

#### 2] Self-hosted Mistral 7B model — no external API keys

#### 3] Modular backend and frontend architecture

#### 4] Role-based access separation and clean routing

#### 5] AI integration without exposing any credentials

---

## 🔮 Future Roadmap

#### 🧠 AI-based plagiarism detection

#### 🧾 Markdown support in articles

#### 📤 Export articles to PDF

#### 📨 Notification system for article review updates

#### 🛡️ Blockchain-based verification of published content

---

### 📸 Project Screenshots
You can view sample screenshots of the project here:
[📄 Click to view AICMS_Screenshots.pdf](https://drive.google.com/file/d/1658TA63s1T8YyIzoiYpIQgiMxfp7nUKr/view?usp=sharing)

---

### 👨‍💻 About Me

Hi, I'm Diwas Mishra — a full-stack developer passionate about building intelligent, real-world applications using modern tools and private AI.

[🌐 LinkedIn](https://www.linkedin.com/in/diwas-mishra-b2109a2a9)

📧 mishradiwasbrijesh@gmail.com

