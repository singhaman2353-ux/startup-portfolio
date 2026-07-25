# 🚀 Startup Portfolio & Client Intake Platform

A full-stack web application built using **HTML, CSS, JavaScript, and Flask**. Visitors can explore a startup's services, learn about its workflow, and submit project inquiries through a live contact form. The application also includes an **Admin Dashboard** for viewing submitted inquiries.

---

## 🌐 Live Demo

### Frontend
https://startup-portfolio-one.vercel.app

### Backend API (Health Check)
https://startup-portfolio-api.onrender.com/api/health

### Admin Dashboard
https://startup-portfolio-one.vercel.app/admin.html

> **Note:** Render's free tier spins down after inactivity. The first request may take **30–50 seconds** while the backend wakes up.

---

# ✨ Features

- Responsive startup landing page
- Services & Process sections
- Client inquiry/contact form
- Flask REST API
- Fetch API integration
- Client-side & server-side validation
- Admin Dashboard for viewing submissions
- Dynamic table populated from REST API
- CORS configured for production deployment
- Deployed on **Vercel** and **Render**

---

# 🛠 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript (ES6)
- Fetch API

### Backend
- Python
- Flask
- Flask-CORS
- Gunicorn

### Tools
- Git
- GitHub
- VS Code
- Vercel
- Render

---

# 📂 Project Structure

```text
startup-portfolio/
│
├── frontend/
│   ├── index.html
│   ├── admin.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── runtime.txt
│   └── submissions.jsonl
│
├── README.md
└── .gitignore
```

---

# 🔗 API Endpoints

## Health Check

```http
GET /api/health
```

Returns:

```json
{
  "status": "ok"
}
```

---

## Submit Client Inquiry

```http
POST /api/contact
```

Example Request

```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "company": "Acme Inc.",
  "budget": "2k-10k",
  "message": "Need a business website."
}
```

Possible Responses

| Status | Description |
|--------|-------------|
| 201 | Inquiry received successfully |
| 400 | Invalid or missing fields |
| 500 | Server storage error |

---

## View All Submissions

```http
GET /api/submissions
```

Returns all stored client inquiries as JSON for the Admin Dashboard.

---

# 🚀 Local Setup

## Clone Repository

```bash
git clone https://github.com/singhaman2353-ux/startup-portfolio.git
```

## Navigate to Project

```bash
cd startup-portfolio
```

## Install Backend Dependencies

```bash
cd backend

pip install -r requirements.txt
```

## Run Backend

```bash
python app.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

## Run Frontend

Open the **frontend** folder using **VS Code Live Server**.

For local development, ensure the API URL inside:

```
frontend/js/main.js
```

points to:

```javascript
const API_BASE_URL = "http://127.0.0.1:5000";
```

---

# 📖 What I Learned

This project helped me understand:

- Building REST APIs with Flask
- Frontend–backend communication using Fetch API
- Handling JSON requests and responses
- Client-side and server-side validation
- CORS configuration
- Dynamic DOM manipulation
- Building an Admin Dashboard
- Git & GitHub workflow
- Deploying a full-stack application using Vercel and Render

---

# 🔮 Future Improvements

- Admin authentication
- SQLite/PostgreSQL integration
- Search & filter submissions
- Export submissions to CSV
- Pagination
- Email notifications
- Better dashboard UI & analytics

---

# 👨‍💻 Author

**Aman Singh**

Aspiring Full Stack Developer

GitHub: https://github.com/singhaman2353-ux

---

## ⭐ Support

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub.
