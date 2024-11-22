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

---------------------------------------------------------------------

##### 2024/10/26 - 1403/08/05

- **Start Project: News_API_Builder_2**
- **Create Virtual Environment** (News_API_Builder_2)
   - `py -m venv News_API_Builder_2`
   - Install required packages:  
     - `pip install Django`
     - `pip install djangorestframework`
     - `pip install django-filter`
- **Study django-filter Documentation**  
   - Resource: [django-filter Documentation](https://pypi.org/project/django-filter/)
- **Start Django Project and App**
   - Initialize project and app:  
     - `django-admin startproject News_API_Builder_2`
     - `py manage.py startapp News_Page_App_2`
- **Configure Project Settings**
   - Add `News_Page_App_2`, `rest_framework`, and `django_filter` to `INSTALLED_APPS` in `settings.py`.
- **Define Models**
   - Write model classes for the news application.
- **Prepare Database**
   - Apply migrations:  
     - `py manage.py makemigrations News_Page_App_2`
     - `py manage.py migrate`
- **Insert Sample Data**
   - Use the Python shell to add initial news data into the database.
- **Define Serializer**
   - Write serializer to handle model data serialization.
- **Define Filters (filter.py)**
   - Implement filters using `django-filter`.
- **Define Views**
   - Write views to handle API requests.
- **Configure URLs**
   - Define URL routes in `News_Page_App_2`.
   - Update main URL routes in `News_API_Builder_2`.
- **Write Unit Tests**
    - Run unit tests:  
      - `py manage.py test News_Page_App_2`

-----------------------------------------------------------------

##### 2024/10/27 - 1403/08/06

- Start Zoomit_Scraper Project
- **Create Virtual Environment**: (Zoomit_Scraper)
	- `py -m venv Zoomit_Scraper`
- Install required packages:
    - `pip install Django`
    - `pip install scrapy`
- **Initialize Scrapy Project**
	- `scrapy startproject Zoomit_Product`
  - Create spider:
	  - `scrapy genspider Zoomit_Spider zoomit.ir`
- **Configure Spider and Test Crawling**
  - Add source URLs and test the spider:
    - `scrapy crawl Zoomit_Spider -o Zoomit_Product_Data.json`
- **Review robots.txt** for zoomit.ir
  - URL: [https://www.zoomit.ir/robots.txt](https://www.zoomit.ir/robots.txt)
- **Develop Scraper Logic**

------------------------------------------------------------------

##### 2024/10/28 - 1403/08/07

- **Start Scrapy Project** (`Zoomit_News_Search`)
    - Initialize project: `scrapy startproject Zoomit_News_Search`
    - Generate spider: `scrapy genspider Zoomit_News_Search_Spider zoomit.ir`
- **Add Source URL and Test Spider**
    - Run spider and save output to JSON: `scrapy crawl Zoomit_News_Search_Spider -o Zoomit_News_Search_Data.json`
- **Update Settings**  
    - Set `ROBOTSTXT_OBEY = False` in settings
- **Install Required Packages**  
    - `pip install selenium`
    - `pip install webdriver-manager`

---------------------------

##### 2024/10/29 - 1403/08/08

- **Developed Zoomit_News_Search project**
    - Implemented functionality to click "view more" button for loading additional content.
- **Started Scrapy Project: Zoomit_News_Search_Content**
    - Command: `scrapy startproject Zoomit_News_Search_Content`
    - Command: `scrapy genspider Zoomit_News_Search_Content_Spider zoomit.ir`
- **Configured Settings**
    - Set `ROBOTSTXT_OBEY = False` to allow unrestricted crawling.
- **Added Source URL and Tested Spider**
    - Command: `scrapy crawl Zoomit_News_Search_Content_Spider -o Zoomit_News_Search_Content_Data.json`
- **Wrote Initial Scraper Logic**

---------------------------

##### 2024/10/30 - 1403/08/09

- **Continued Zoomit_News_Search_Content Project**
    - Extracted elements from each search results page using:
        - `scrapy.Request`
- **Started Reuters_Scraper**
    - Command: `py -m venv Reuters_Scraper`
    - Installed packages: `scrapy`, `selenium`, `webdriver-manager`
- **Started Scrapy Project: Reuters_Gold_News_Search**
    - Command: `scrapy startproject Reuters_Gold_News_Search`
    - Command: `scrapy genspider Reuters_Gold_News_Search_Spider reuters.com`
- **Reviewed robots.txt for reuters.com**
    - URL: `https://www.reuters.com/robots.txt`
- **Configured Settings**
    - Set `ROBOTSTXT_OBEY = False` for full page access.
- **Added Source URL and Tested Spider**
    - Command: `scrapy crawl Reuters_Gold_News_Search_Spider -o Reuters_Gold_News_Search_Data.json`
- **Wrote Initial Scraper Logic**

----------------

##### 2024/11/01 - 1403/08/11

- **Continued Reuters_Gold_News_Search Project**
    - Created `extract_cookies_reuters.py` using Selenium to handle site cookies (not supported with Scrapy).
- **Rewrote Reuters_Gold_News_Search using Selenium Only**
    - Added source URL and ran initial tests.

---------------

##### 2024/11/02 - 1403/08/12

- **Continued Reuters_Gold_News_Search Project**
    - **Selenium Configuration**: Optimized Chrome options for better cookie management and detection avoidance.
    - **XPath vs. Class Name**: Found that XPath often provides more reliable element selection than class names.
        - *Non-functional:* 
            ```python
            all_news_title = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_6__1qUJ5 heading__base__2T28j heading__heading_6__RtD9P")))
            ```
        - *Functional:* 
            ```python
            all_news_title = WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='fusion-app']/div[2]/div[2]/div/div[2]/div[2]/ul/li/div/div/header/a/span")))
            ```

----------------------------

##### 2024/11/03 - 1403/08/13

- **Continued Reuters_Gold_News_Search Project**
    - **Data Collection**: Successfully extracted news titles from multiple pages.
    - **CSV Management**: Collected page URLs, titles, and news headlines, and saved them into a structured CSV file.
    - **Enhanced Navigation**: Implemented scrolling functions to ensure complete page loading before data extraction.
    - Defined `scroll_up` function for returning to top of page when necessary.

-----------------------------------------
#####  2024/11/04 - 1403/08/16
- **Continued Reuters_Gold_News_Search Project**
	- **Enhanced Script Update:** Improved script to filter news articles from the last six months, adding article dates to the CSV output for relevance.
- Set up **Reuters_Gold_News_Search_Content** environment
    - `py -m venv Reuters_Gold_News_Search_Content`
    - `pip install selenium`
    - `pip install webdriver-manager`
- Initiated Selenium project **Reuters_Gold_News_Search_Content**
- Reviewed `robots.txt` for reuters.com
    - URL: `https://www.reuters.com/robots.txt`
- Added source URL and tested CSV output
    - Filename: `Reuters_Gold_News_Search_Content_Data.csv`
- Developed Selenium scraper

-----------------------------------

##### 2024/11/08 - 1403/08/18

- Continued project work on **Reuters_Gold_News_Search_Content**
    - **Data Extraction**: Successfully collected URL source, page title, date, tags, author, and content.

-------------------------------------

##### 2024/11/09 - 1403/08/19

- Continued project work on **Reuters_Gold_News_Search_Content**
    - Improved content extraction in `all_news_content_page`.

-----------------------------------------

##### 2024/11/11 - 1403/08/21

- Continued project work on **Reuters_Gold_News_Search_Content**
    - Attempted to improve cookie handling to load more news with VPN (no successful result).

--------------------------------------

##### 2024/11/13 - 1403/08/23

- **Started the project (News_Updater)**
- **Created a virtual environment**
    - `py -m venv News_Updater`
    - Installed required packages:
        - `pip install django`
        - `pip install celery`
        - `pip install flower`
        - `pip install redis`
        - `pip install django-celery-beat`
- **Started the Django project and app**
    - `django-admin startproject News_Updater`
    - `py manage.py startapp News_Updater_App`
- **Configured settings**
    - Added `News_Updater_App` to `INSTALLED_APPS`
- **Studied about**:
    - Celery
    - Message Broker:
        - RabbitMQ
        - Redis
            - [Redis documentation for Celery](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#broker-redis)
        - Other brokers:
            - [Celery documentation on brokers](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html#broker-overview)
    - Sources:
        - [Celery Documentation](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)
        - [First steps with Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#first-steps)
- **Started writing a simple script with Celery**
- **Installed and activated WSL (Windows Subsystem for Linux)**
    - `wsl --install`
- **Installed `redis-server` in WSL**
    1. `sudo apt update`
    2. `sudo apt-get install redis-server`
- **Started `redis-server`**
    - `redis-server`
- **Checked Redis setup in WSL**
    - `redis-cli ping` 
        - Output ===> `PONG` (executed correctly)
- Ran:
    - `celery -A test1celery worker --loglevel=INFO`
- **Encountered `PermissionError` when running `celery -A test1celery worker --loglevel=INFO`**
    %% The `PermissionError` usually occurs due to access permission issues or incompatibilities of Python modules like billiard with Windows. %%
    - **Solution**: `celery -A test1celery worker --loglevel=INFO --pool=solo`

---------------------------

##### 2024/11/14 - 1403/08/24

- Continued studying:
    - Celery
    - Sources:
        - [Next steps with Celery](https://docs.celeryq.dev/en/stable/getting-started/next-steps.html#next-steps)
- **Getting started with Celery in a Django project**

---------------------------

##### 2024/11/20 - 1403/08/30

- Continued working on the project (News_Updater_App)
    - Created `celery.py` file
    - Made changes to `settings.py`
    - Configured Celery Beat
        - `python manage.py migrate`
        - `python manage.py shell`
            - Running code to create periodic tasks:
                ```python
                from django_celery_beat.models import PeriodicTask, IntervalSchedule
                
                schedule, created = IntervalSchedule.objects.get_or_create(
                    every=10,
                    period=IntervalSchedule.SECONDS,
                )
                
                PeriodicTask.objects.create(
                    interval=schedule,
                    name='Update News Periodically',
                    task='News_Updater_App.tasks.update_news', 
                )
                ```
    - Running Flower:
        - `celery -A News_Updater flower`
        - Access via: http://localhost:5555
- **Created `dockerfile`**
- **Created `docker-compose.yml`**
- **Installed Docker Desktop**
- **Running the project with Docker Compose**
    - `docker-compose up --build`
        - Ran `celery -A News_Updater worker --loglevel=INFO` in the Docker environment
    - Checked process status in Docker:
        - `docker ps -a`
- **Installed `iputils-ping` in Docker environment**
    - `apt-get update && apt-get install iputils-ping -y`
- **Tested `tasks`**
    - Ran in the shell:
        - `from News_Updater_App.tasks import update_news`
        - `update_news.delay()`

--------------------

##### 2024/11/22 - 1403/09/02

- **Initial testing and implementation (News_Updater_App)** 
    - `docker build -t news_updater .`
    - `docker-compose up --build`
    - Installed `gunicorn`:
        - `pip install gunicorn`
    - Checked process status:
        - `docker ps`
        - `docker image ls`
    - Viewed Docker logs:
        - `docker-compose logs celery`
    - **Monitored with Flower**
        - Access via: http://localhost:5555/
    - Ran in Docker:
        - `docker-compose exec web python manage.py shell`
            - Ran:
                ```python
                from news_updater.tasks import update_news
                update_news.delay()
                ```

