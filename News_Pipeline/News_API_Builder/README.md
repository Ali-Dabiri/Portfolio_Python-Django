
# News API Builder

This project is a Django-based news API that allows users to fetch, filter, and retrieve news articles. It supports filtering based on tags and keywords and allows exclusion of specific keywords.

## Features

- Fetch a list of news articles with details like title, content, tags, and source.
- Filter news articles by tags or keywords.
- Exclude articles containing specified keywords.
- Includes unit tests for API validation and functionality.

## Requirements

- Python 3.10+
- Django 5.1.2+
- Django REST framework 3.15.2

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/News_API_Builder.git
   cd News_API_Builder
   ```

2. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv News_API_Builder
   source News_API_Builder/bin/activate  # Unix/MacOS
   source News_API_Builder\Scripts\activate.bat # Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Django Project:**
   ```bash
   python manage.py makemigrations News_Page_App
   python manage.py migrate
   ```

5. **Run the Server:**
   ```bash
   python manage.py runserver
   ```

## Usage

Once the server is running, access the API endpoint at:

```
http://127.0.0.1:8000/api/news/
```

### Filtering Options

- **By Tag**: `?tags=tag_name`
- **By Keyword**: `?keywords=keyword1,keyword2`
- **Exclude by Keyword**: `?exclude_keywords=keyword3`

For example:
```
http://127.0.0.1:8000/api/news/?tags=technology&keywords=AI,robotics&exclude_keywords=finance
```

## Running Tests

To execute the unit tests for this API:

```bash
python manage.py test News_Page_App
```

## Project Structure

- **models.py**: Defines the `News` model to store news article data.
- **serializers.py**: Serializes the `News` model for API responses.
- **views.py**: Contains the `NewsList` view for handling API requests.
- **urls.py**: Routes the API endpoints.
