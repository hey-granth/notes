# 📝 CloudNotes – Markdown Notes with Public Sharing

CloudNotes is a simple, lightweight Django-based web app that allows users to:
- Write notes using Markdown ✍️
- Save them securely to the cloud ☁️
- Share them publicly via unique URLs 🔗

---

## 🚀 Features

- ✅ User authentication (signup, login, logout)
- ✅ Create, view, and delete Markdown notes
- ✅ Real-time Markdown editing using SimpleMDE editor
- ✅ Public sharing of notes via `/username/<note_id>/` URLs
- ✅ Auto-logout on browser close for extra privacy
- ✅ Django Admin support for managing notes

---

## 🏗️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates + SimpleMDE Markdown Editor
- **Database:** PostgreSQL (for production), SQLite (for development)
- **Deployment:** Hosted on [Render](https://render.com)
- **Static File Serving:** WhiteNoise

---

## 📁 Folder Structure

```
cloudnotes/
├── notes/                 # Project settings
├── markdown_notes/        # Notes app: views, models, templates
├── users/                 # Authentication logic
├── templates/             # Base templates
├── static/                # Static files (CSS/JS)
├── manage.py
├── requirements.txt
└── Procfile
```

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/hey-granth/notes.git
cd notes
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Create a `.env` file and set:
```
SECRET_KEY=your_secret_key
DEBUG=True
```

### 5. Run locally

```bash
python manage.py migrate
python manage.py runserver
```

Then open [http://localhost:8000](http://localhost:8000)

---

## 🚀 Deploy to Render

1. Push code to GitHub
2. Add `render.yaml` and `Procfile`
3. Create new Web Service on [render.com](https://render.com)
4. Add `SECRET_KEY`, `DEBUG`, and `DATABASE_URL` as environment variables
5. Enable PostgreSQL
6. Add build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Future Improvements

- Note editing
- Note version history
- Rich Markdown support (tables, code highlighting)
- User profiles

---

Made with ❤️ using Django.