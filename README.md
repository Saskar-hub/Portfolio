# Professional Developer Portfolio Website

A modern, responsive, and fully manageable developer portfolio built with Django and custom CSS.

## 🚀 Features
- **Modern UI/UX**: Clean, professional design with smooth animations.
- **Fully Responsive**: Optimized for mobile, tablet, and desktop.
- **Dark Mode**: Built-in dark/light mode toggle.
- **Custom Admin Dashboard**: A tailored dashboard to manage all content (Projects, Skills, Experience, Messages, Bio).
- **Dynamic Content**: No hardcoded text; everything can be edited via the admin panel.
- **Project Filtering**: Filter projects by category (Web, AI, Mobile, etc.).
- **Contact Form**: Functional contact form with message management in the dashboard.
- **SEO Friendly**: Optimized structure and meta tags.

## 🛠️ Tech Stack
- **Backend**: Python 3.x, Django 5.x
- **Database**: SQLite (default)
- **Frontend**: HTML5, Custom CSS3 (Flexbox/Grid), Vanilla JavaScript
- **Icons**: FontAwesome 6.4

## 📦 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd <project-folder>
   ```

2. **Install dependencies**:
   ```bash
   pip install django
   ```

3. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Seed Initial Data (Recommended)**:
   ```bash
   python seed_data.py
   ```
   *This will create a default user 'admin' and populate the site with sample data.*

5. **Create Superuser (If not using seed data)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Site**:
   - Public Website: `http://127.0.0.1:8000/`
   - Custom Admin Dashboard: `http://127.0.0.1:8000/admin-dashboard/`
   - Default Credentials (if seeded): `admin` / `admin123`

## 🔐 Admin Dashboard
The custom admin dashboard allows you to:
- **Manage Projects**: Add, edit, or delete projects with images and tech stacks.
- **Update Skills**: Categorize skills and set proficiency levels.
- **Experience & Education**: Maintain your professional timeline.
- **Inbox**: View and delete messages sent via the contact form.
- **Profile Management**: Update your bio, tagline, resume, and social links dynamically.

## 📁 Project Structure
- `portfolio/`: Main app containing models, views, and templates.
- `my_portfolio/`: Project configuration settings and URLs.
- `media/`: Folder for uploaded images and resumes.
- `static/`: Custom CSS, JS, and image assets.
