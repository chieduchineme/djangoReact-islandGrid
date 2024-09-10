# DjangoBackend-ReactFrontend Project

## Overview

This project is a web application built using:
- **Backend**: Django (Python) REST API for handling server-side logic and database interactions.
- **Frontend**: React.js for creating a dynamic, responsive user interface.
  
## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup (Django)](#backend-setup-django)
  - [Frontend Setup (React)](#frontend-setup-react)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [License](#license)

---

## Prerequisites

Make sure you have the following tools installed on your machine:

- [Python 3.x](https://www.python.org/downloads/)
- [Node.js (with npm)](https://nodejs.org/)
- [Git](https://git-scm.com/)

---

## Setup Instructions

### Backend Setup (Django)

1. **Clone the repository**:
   ```bash
   git clone djangoReact-islandGrid
   cd djangoBackend

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

3. Install backend dependencies:
pip install -r requirements.txt

4. Set up environment variables: 
by creating a .env file in the backend directory to store sensitive information like secret keys, database settings, etc.
env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url

5. Run database migrations:
python manage.py migrate


# Frontend Setup (React)
1. Navigate to the frontend directory:
cd ../reactFrontend

2. Install frontend dependencies:
npm install

3. Set up environment variables:
Create a .env file in the frontend directory to store variables such as the backend API URL:
REACT_APP_API_URL=http://localhost:8000/api/


# Deployment
# Backend (Django)
1. Set up your production environment variables (e.g., DEBUG=False).
2. Install production dependencies using:
pip install -r requirements.txt
3. Run migrations on your production database:
python manage.py migrate


# Frontend (React)
1. Build the React project for production:
npm run build
2. Serve the static files in production (using Nginx, Apache, or any other web server).


# Common Deployment Options
Django: Deploy with services like Heroku, DigitalOcean, or AWS.
React: Deploy on platforms like Vercel, Netlify, or GitHub Pages.
