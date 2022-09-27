# Media List Management System
Database to manage media lists, built with Django 4.1 and Bootstrap 5.2.

## Prereqs
- [Python 3.10.4 or later](https://www.python.org/downloads/)
- Any code editor

## Installation Instructions
### 1. Create virtual environment
From the root directory, run `python -m venv venv`

### 2. Activate virtual environment
From the root directory, on **macOS**: run `source venv/bin/activate` <br>
From the root directory, on **Windows**: run `venv\Scripts\activate`

### 3. Install required dependencies
From the root directory, run `pip install -r requirements.txt`

### 4. Run migrations
From the root directory, run <br> `python manage.py makemigrations` <br>
`python manage.py migrate`

### 5. Create a superuser to access Django admin interface
From the root directory, run <br>
`python manage.py createsuperuser` <br>
and enter a username, email, and password

### 6. Run app
From the root directory, run <br>
`python manage.py runserver`

## Deployment
coming soon# media-list-management-system
