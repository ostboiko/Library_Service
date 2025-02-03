# Library_Service




library-service
Overview
Library Service is a Django project designed to manage various aspects of a library, book and borrowings.

Contents
    Pages
        Book API
        Borrowing API
        User API
        Instructions for Local Setup
        Environment Configuration



# Book API
URL: /api/book-service/
Description: Endpoint for managing book.

# Borrowing API
URL: /api/borrowing-service/
Description: Endpoint for managing borrowing - book, user.


# User API
URL: /api/user/
Description: Endpoint for user-related functionalities like registration and token management.

Instructions for Local Setup
Clone the repository: git clone https://github.com/ostboiko/Library_Service

Install necessary dependencies: pip install -r requirements.txt
Start the server: python manage.py runserver

# Environment Configuration
Create a .env file based on env.sample and enter your secret keys and other settings.