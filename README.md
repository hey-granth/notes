# Notes

1. 🛠 Built with Django: A full-stack web app using Django that handles both frontend and backend logic in a beginner-friendly monolithic structure.

2. 👤 User Authentication: Users can sign up, log in, and manage their own private notes using Django’s built-in authentication system.

3. 📝 Markdown Notes: Users can create, edit, delete, and view notes written in Markdown, with live or saved HTML rendering using the markdown Python package.

4. 📦 App Structure:

   - `users`: handles auth and profiles.

   - `notes`: manages note creation and display.

   - `sync`: (optional) for cloud backup/export.

   - `pages`: (optional) for static views like home/about.

5. 🧠 Monolithic Architecture: No microservices required; all logic lives in a single Django project with modular apps.

6. 📚 Database:

   - Uses SQLite in development.

   - Will switch to PostgreSQL for production deployments.

7. 🖼 Frontend: Built using Django templates; can optionally be styled with Bootstrap or TailwindCSS for a clean UI.

8. ☁️ Cloud Sync (Planned): Future feature to sync notes to services like Google Drive or Dropbox, or export them as .pdf or .txt.

9. 🚀 Deployment Plan: Will be hosted for free on platforms like Render, Railway, or Fly.io with HTTPS and PostgreSQL.

10. 📈 Learning Goals: A project to practice Django models, views, templates, authentication, and deployment—ideal for beginners stepping into full-stack web development.