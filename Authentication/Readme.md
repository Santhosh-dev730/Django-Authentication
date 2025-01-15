Dependencies
------------

#. Bulma - 0.9.3

#. Python - 3.12.0

#. Django - 5.0.3


# Django Authentication System
A simple user authentication system built with Django, featuring user registration, login, logout, and personalized user experience. This project demonstrates how to use Django's built-in authentication framework for user management.

## Features
- User Registration
  - Create an account with username, email, and password.
- User Login
  - Authenticate users securely.
- User Logout
  - Log out users
- Error Messages
  - Display error and success messages using Django messages framework.

### Prerequisites
1. Make sure you have installed Python 3 on your device.
2. Create a vitual environment.
```
python -m venv .venv
source .venv/bin/activate
```
3. Create a project and app
```
django-admin startproject auth
django-admin startapp my_app
```
4. You need to make migrations into db.sqlite3 (database) to create the table for the new model
```
python manage.py makemigrations
python manage.py migrate
```
5. Test the Project
```
python manage.py runserver
```
