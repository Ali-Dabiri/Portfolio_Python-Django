
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
