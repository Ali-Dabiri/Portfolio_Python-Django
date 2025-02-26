
# Django JWT Authentication API

### Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
    - [User Registration](#user-registration)
    - [User Login](#user-login)
    - [Token Operations](#token-operations)
    - [Authentication with JWT Header](#authentication-with-jwt-header)
- [Technologies Used](#technologies-used)
- [License](#license)
## Overview

Django JWT Authentication API is a Django-based authentication system that provides user registration, login, and token-based authentication using JSON Web Tokens (JWT). This application is built with Django REST Framework (DRF) and `rest_framework_simplejwt` for secure authentication.

## Features

- User registration with a custom user model
- User login with JWT token generation (access & refresh tokens)
- Token refreshing and verification
- Authentication via JWT token in the request header
- Secure password handling with Django's `AbstractBaseUser`

## Installation

1. Clone the repository:
    
    ```sh
    git clone https://github.com/Ali-Dabiri/Portfolio_Python-Django/tree/main/Authentication_API/Authentication_Token_API
    cd Authentication_Token_API
    ```
    
2. Create and activate a virtual environment:
    
    ```sh
    python -m venv venvname
	source venvname/bin/activate  # On macOS/Linux
	venvname\Scripts\activate.bat  # On Windows
    ```
    
3. Install dependencies:
    
    ```sh
    pip install -r requirements.txt
    ```
    
4. Apply database migrations:
    
    ```sh
    python manage.py migrate
    ```
    
5. Run the development server:
    
    ```sh
    python manage.py runserver
    ```
    

## API Endpoints

### User Registration

**Endpoint:** `POST /api/users/`

- Registers a new user.
- Example request:
    
    ```json
    {
      "username": "testuser",
      "password": "securepassword"
    }
    ```
    

### User Login

**Endpoint:** `POST /api/users/authentication/`

- Authenticates a user and returns JWT tokens.
    
- Example request:
    
    ```json
    {
      "username": "testuser",
      "password": "securepassword"
    }
    ```
    
- Example response:
    
    ```json
    {
      "message": "Login successful",
      "refresh": "<refresh_token>",
      "access": "<access_token>"
    }
    ```
    

### Token Operations

- **Obtain Token:** `POST /api/token/`
- **Refresh Token:** `POST /api/token/refresh/`
- **Verify Token:** `POST /api/token/verify/`
- **Refresh & Verify Token:** `POST /api/token/refresh-and-verify/`

### Authentication with JWT Header

**Endpoint:** `POST /api/token/authentication-token-header/`

- Verifies the provided JWT access token in the request header.

## Technologies Used

- Django
- Django REST Framework
- Simple JWT
- SQLite

## License

This project is licensed under the MIT License.
