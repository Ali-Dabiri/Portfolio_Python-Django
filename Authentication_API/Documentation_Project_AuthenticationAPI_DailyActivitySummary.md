
# Documentation_Project_AuthenticationAPI_DailyActivitySummary

##### 2025/02/01 - 1403/11/13

- **Start Project:** `Authentication_Token_API`
- **Create a virtual environment:**
    - `py -m venv Authentication_Token_API`
- **Install required packages in the virtual environment:**
    - `pip install Django`
    - `pip install djangorestframework`
    - `pip install djangorestframework-simplejwt`
- **Create a Django project:**
    - `django-admin startproject Authentication_Token_API`
- **Create a Django app:**
    - `django-admin startapp Authentication_Token_App`
- **Create `urls.py` and `serializer.py` in the Django app using the VSCode terminal:**
    - `code urls.py`
    - `code serializer.py`
- **Configure `settings.py`:**
    - Add the following to `INSTALLED_APPS`:
        - `Authentication_Token_App`
        - `rest_framework`
        - `rest_framework_simplejwt`
- **Configure `urls.py` in the Django project:**
    - Import the `include` module
- **Define `models.py`:**
    - Use the following modules:
        - `AbstractBaseUser`
        - `BaseUserManager`
        - `PermissionsMixin`
- **Configure `settings.py`:**
    - Set `AUTH_USER_MODEL`
- **Define the serializer in `serializers.py`**
- **Define views in `views.py`**
- **Define URL patterns in `urls.py` for the Django app**
- **Create database migrations:**
    - `py manage.py makemigrations Authentication_Token_App`
- **Apply migrations to create tables in the database:**
    - `py manage.py migrate`
- **Modify `views.py`:**
    - Define a class to verify tokens using JWT in the request headers

---

##### 2025/02/02 - 1403/11/14

- **Continue Project: `Authentication_Token_API`**
- **Implement a `GET` method to retrieve the user list:**
    - Add `def get(self, request):` to `RegisterUserView`
- **Study JSON structure and JWT authentication**

---

##### 2025/02/03 - 1403/11/15

- **Continue Project: `Authentication_Token_API`**
- **Further study HTTP headers and JWT token structure**
- **Authenticate users using a username and password, verifying the token in the JWT header (via the payload)**

---


##### 2025/02/05 - 1403/11/17

- Start Project: RoleBase_API
- Create a virtual environment:
    - `py -m venv RoleBase_API`
- Install required packages:
    - `pip install Django`
    - `pip install djangorestframework`
    - `pip install djangorestframework-simplejwt`
- Create a Django project:
    - `django-admin startproject RoleBase_API`
- Create a Django app:
    - `django-admin startapp RoleBase_App`
- Create `serializer.py` and `urls.py` in VSCode Terminal:
    - `code serializer.py`
    - `code urls.py`

### Django Configuration

- Configure `settings.py`:
    - Add installed apps:
        - `RoleBase_App`
        - `rest_framework`
        - `rest_framework_simplejwt`
- Configure `urls.py` in the Django app:
    - Import `include` module

### Model and View Definitions

- Define models in `models.py`.
- Define serializers in `serializer.py`.
- Define views in `views.py`:
    - **User Role:**
        - Signup
        - Login
- Define URLs in `urls.py` in the Django app.

### Database Setup

- Create the database based on `models.py`:
    - `py manage.py makemigrations RoleBase_App`
- Create tables based on `models.py`:
    - `py manage.py migrate`

### View Enhancements

- Modify `views.py`:
    - **Admin Role:**
        - Display all users
        - Create users by Admin

### Model Enhancements

- Update `models.py`:
    - Add a datetime column:
        - `date_time = models.DateField(auto_now_add=True)`
- Save changes:
    - `py manage.py makemigrations RoleBase_App`
    - `py manage.py migrate`
- Further improvements to `models.py`:
    - Add a date column:
        - `date = models.DateField(auto_now_add=True)`
    - Add a time column:
        - `time = models.TimeField(auto_now_add=True)`

### Database Reset

- Delete the database:
    - `rm db.sqlite3`
- Delete `0001_initial.py` in the `__pycache__` folder.
- Save changes:
    - `py manage.py makemigrations RoleBase_App`
    - `py manage.py migrate`

### Additional View Enhancements

- Modify `views.py`:
    - **Manager Role:**
        - Filter data based on date and time

---

##### 2025/02/09 - 1403/11/20


- Continue Project: RoleBase_API
- Enhance `models.py`:
    - Add a role column to manage user roles.
- Improve `views.py`:
    - Implement user signup and assign roles.
    - Define a login endpoint to include the `role` parameter in the JWT payload.
    - Implement an endpoint to show all users (accessible only to Admins with valid JWT authorization).
    - Allow Admins to create usernames and passwords for roles `admin` and `users` (with role validation in JWT authorization for security).
- Further enhancements to `views.py`:
    - Add filters for date and time ranges (restricted to Managers with valid role authorization in JWT payload).
