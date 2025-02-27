
# Role-Based Authentication API with Django & JWT

## Table of Contents

- [Introduction](#introduction)
    - [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
    - [Clone the repository](#1-clone-the-repository)
    - [Create a virtual environment](#2-create-a-virtual-environment-and-activate-it)
    - [Install dependencies](#3-install-dependencies)
    - [Apply database migrations](#4-apply-database-migrations)
    - [Create a superuser](#5-create-a-superuser-optional-for-admin-access)
    - [Run the development server](#6-run-the-development-server)
- [API Endpoints](#api-endpoints)
    - [User Registration](#1-user-registration)
    - [User Login](#2-user-login)
    - [Show All Users (Admin Only)](#3-show-all-users-admin-only)
    - [Create a New User (Admin Only)](#4-create-a-new-user-admin-only)
    - [Get User History (Manager Only)](#5-get-user-history-manager-only)
- [Role-Based Access Control (RBAC)](#role-based-access-control-rbac)
- [Testing the API with Postman](#testing-the-api-with-postman)
- [License](#license)

## Introduction

This project is a **Role-Based Authentication API** built with **Django REST Framework (DRF)** and **JWT authentication**. The API allows user authentication with different roles (User, Admin, Manager) and provides access control based on roles. Users can register, log in, and interact with different endpoints depending on their assigned role.

### Key Features:

- User registration and login with JWT authentication
- Role-based access control (RBAC) for Admins and Managers
- Secure API endpoints for different user roles
- Token-based authentication using **JWT (JSON Web Token)**
- Filtering users by date and time (for Managers)

---

## Technologies Used

- **Django** 
- **Django REST Framework (DRF)**
- **JWT Authentication** (via `djangorestframework-simplejwt`)
- **SQLite**

---

## Installation

### 1. Clone the repository:

```sh
git clone https://github.com/Ali-Dabiri/Portfolio_Python-Django/tree/main/Authentication_API/RoleBase_API
cd RoleBase_API
```

### 2. Create a virtual environment and activate it:

```sh
python -m venv venvname
source venvname/bin/activate  # On macOS/Linux
venvname\Scripts\activate.bat  # On Windows
```

### 3. Install dependencies:

```sh
pip install -r requirements.txt
```

### 4. Apply database migrations:

```python
python manage.py migrate
```

### 5. Create a superuser (optional for Admin access):

```python
python manage.py createsuperuser
```

### 6. Run the development server:

```python
python manage.py runserver
```

Now the API is available at `http://127.0.0.1:8000/`

---

## API Endpoints

### **1. User Registration**

**Endpoint:** `POST /api/signup/`

#### Request Body:

```json
{
  "user_name": "testuser",
  "user_password": "testpassword",
  "role": "user"
}
```

#### Response:

```json
{
  "message": "User created successfully"
}
```

### **2. User Login**

**Endpoint:** `POST /api/login/`

#### Request Body:

```json
{
  "user_name": "testuser",
  "user_password": "testpassword"
}
```

#### Response:

```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

---

### **3. Show All Users (Admin Only)**

**Endpoint:** `GET /api/users/`

#### Headers:

```json
{
  "Authorization": "Bearer <access_token>"
}
```

#### Response:

```json
[
  {
    "id": 1,
    "user_name": "testuser",
    "role": "user",
    "date": "2024-02-07",
    "time": "12:30:00"
  }
]
```

---

### **4. Create a New User (Admin Only)**

**Endpoint:** `POST /api/create-user/`

#### Request Body:

```json
{
  "user_name": "newuser",
  "user_password": "newpassword",
  "role": "manager"
}
```

#### Response:

```json
{
  "message": "User created successfully"
}
```

---

### **5. Get User History (Manager Only)**

**Endpoint:** `GET /api/users/history/`

#### Query Parameters (Optional):

```
start_date=2024-02-01&end_date=2024-02-05&start_time=10:00:00&end_time=15:00:00
```

#### Headers:

```json
{
  "Authorization": "Bearer <access_token>"
}
```

#### Response:

```json
[
  {
    "id": 1,
    "user_name": "testuser",
    "role": "user",
    "date": "2024-02-01",
    "time": "12:00:00"
  }
]
```

---

## Role-Based Access Control (RBAC)

|Role|Endpoints Accessible|
|---|---|
|User|`/api/login/`, `/api/signup/`|
|Manager|`/api/users/history/`|
|Admin|`/api/users/`, `/api/create-user/`|

---

## Testing the API with Postman

1. **Login** using `/api/login/` and copy the **access token**.
2. **Make authorized requests** by adding the token to the **Authorization header** as `Bearer <access_token>`.
3. Try different roles (`admin`, `manager`, `user`) to test role-based access.

---

## License

This project is licensed under the MIT License.****
