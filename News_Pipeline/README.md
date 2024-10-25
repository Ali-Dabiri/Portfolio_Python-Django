# Documentation_Project_News Pipeline_(Daily Activity Summary) 

##### 2024/10/25 - 1403/08/04

1. **Create Virtual Environment**  
   - `py -m venv News_API_Builder`
   - Install required packages:  
     - `pip install Django`
     - `pip install djangorestframework`

2. **Start Django Project and App**  
   - `django-admin startproject News_API_Builder`
   - `py manage.py startapp News_Page_App`

3. **Configure Settings**  
   - Add `News_Page_App` and `rest_framework` to `INSTALLED_APPS` in the project’s settings.

4. **Define Models**  
   - Write the model classes for the news application.

5. **Prepare Database**  
   - Apply model migrations to the database:  
     - `py manage.py makemigrations News_Page_App`
   - Create tables in the database:  
     - `py manage.py migrate`

6. **Insert Sample Data**  
   - Use the Python shell to add initial news data into the database.

7. **Define Serializer**  
   - Write serializer for model data serialization.

8. **Define Views**  
   - Write views to handle API requests.

9. **Configure URLs**  
   - Define URL routes in `News_Page_App`.
   - Define main URL routes in `News_API_Builder`.

10. **Write Unit Tests**  
    - Run unit tests for the application:  
      - `py manage.py test News_Page_App`
