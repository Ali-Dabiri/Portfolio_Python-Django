
# News_API_Builder_2

News_API_Builder_2 is a Django REST API project that allows users to retrieve, filter, and manage news articles with tags, keywords, and customizable exclusions using `django-filter`. This project is ideal for handling a searchable and filterable database of news articles.

## Features
- Create and retrieve news articles with tags, content, and source fields.
- Filter news articles by tags and keywords.
- Exclude articles with specific keywords.
- Unit tests included to validate API functionalities.

## Requirements
- Python 3.10+
- Django==5.1.2
- djangorestframework==3.15.2
- django-filter==24.3
- Other requirements can be found in `requirements.txt`.

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/Ali-Dabiri/Portfolio_Django/tree/main/News_Pipeline/News_API_Builder_2
    cd News_API_Builder_2
    ```

2. **Set up a virtual environment**
    ```bash
    python -m venv News_API_Builder_2
    source News_API_Builder_2/bin/activate  # Unix/MacOS
    source News_API_Builder_2\Scripts\activate.bat # Windows
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the server**
    ```bash
    python manage.py runserver
    ```

## API Usage

### Endpoints
- **Retrieve all news articles**: `GET /api/news/`
- **Filter by tag**: `GET /api/news/?tags=<tag>`
- **Filter by keywords**: `GET /api/news/?keywords=<keyword1,keyword2>`
- **Exclude by keywords**: `GET /api/news/?exclude_keywords=<keyword1,keyword2>`

### Example
Fetch news articles containing "technology" in tags and excluding "sports" keywords:
```
GET /api/news/?tags=technology&exclude_keywords=sports
```

## Testing

Run unit tests with the following command:
```bash
python manage.py test News_Page_App_2
```

## Project Structure
- `models.py`: Defines the News model with title, content, tag, and source fields.
- `serializers.py`: Configures the serializer for News data.
- `filters.py`: Implements custom filters for tags, keywords, and exclusions.
- `views.py`: Contains the view logic for listing and creating news.
- `urls.py`: Defines the API endpoint for news listing.

## License
This project is licensed under the MIT License.
