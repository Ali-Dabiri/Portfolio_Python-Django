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
