# Django-Review-Website
Django website developed on Windows for a tecnical test.
All commands here are the ones I used on Windows.

# Instalation and execution
To run the website, you will need to have the following installed:
  - Python (personally, I used 3.12)
  - Django (run: pip install django)
  - Crispy (run: pip install django-crispy-forms, pip install crispy-bootstrap4)
  - Pillow (run: pip install Pillow)

After all the steps, you can run the website locally using the 'py manage.py runserver' command;

# How it is organized?
The website launches on the home page, where you can access the registered companies, login button and register button.

If you are already logged in, you will see a profile button and logout button.

To add a new review, you can click on the company you want and there you will see a button to create a new review.

It is only possible to add a new company through the Django Admin page (access 'yourLocalLink/admin'). The same applies to delete anything.

# Users
SuperUser:
- admin (password: NovoAdmin123)

Users:
- usuario1 (password: NovaSenha123)