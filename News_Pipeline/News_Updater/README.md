
# News_Updater 

This project is designed to collect and update news articles in a database. The data collection process is handled by Celery tasks, which are executed periodically. The project uses Django as the web framework, Redis as the message broker, and Flower for monitoring Celery tasks. Docker is used to containerize the entire application, making it easy to deploy and manage.

**Note**: This is an initial and testing version of the project, not yet complete.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Dockerfile](#dockerfile)
- [Monitoring Celery Tasks](#monitoring-celery-tasks)
- [License](#license)

## Features

- Collects news articles from a specified source (e.g., news APIs or web scraping).
- Uses Celery for periodic background tasks to update the news database.
- Redis is used as the message broker for Celery tasks.
- Flower is used to monitor and manage Celery tasks.
- Dockerized application for easy deployment.

## Requirements

- Docker and Docker Compose
- Python 3.10+
- Redis
- Celery
- Django
- Gunicorn

## Installation

Follow the steps below to get the project up and running on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/Ali-Dabiri/Portfolio_Python-Django/tree/main/News_Pipeline/News_Updater
cd News_Updater
```

### 2. Set up Docker and Docker Compose

Ensure that Docker and Docker Compose are installed on your system.

### 3. Build and start the containers

Use the following command to build and start the containers:

```bash
docker-compose up --build
```

This will build the Docker images and start the following services:

- **django_app**: The Django web application.
- **redis**: Redis service for message brokering.
- **celery_worker**: Celery worker for processing background tasks.
- **celery_beat**: Celery Beat for periodic tasks.
- **celery_flower**: Flower for monitoring Celery tasks (available on port 5555).

### 4. Access the application

Once the containers are running, you can access the Django application at:

```bash
http://localhost:8000
```

Flower (for monitoring Celery tasks) is available at:

```bash
http://localhost:5555
```

### 5. Running Celery tasks

The Celery worker will automatically start running once the containers are up. You can add new tasks (e.g., `update_news()`) by calling them through the Django application or using Django's admin panel.

### 6. Stop the containers

To stop the containers, press `Ctrl+C` and run the following command to stop all services:

```bash
docker-compose down
```

## Configuration

You can configure the following settings in the `settings.py` file for the Django project:

- **CELERY_BROKER_URL**: URL of the message broker (e.g., Redis).
- **CELERY_RESULT_BACKEND**: URL for storing the task results.
- **CELERY_ACCEPT_CONTENT**: The content types that Celery can accept (e.g., `json`).
- **CELERY_TASK_SERIALIZER**: The serialization format for tasks (e.g., `json`).

For example:

```python
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
```

## Dockerfile

The project is containerized using Docker. The Dockerfile is as follows:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "News_Updater.wsgi:application"]
```

### Docker Compose File

The `docker-compose.yml` file defines the services that make up the application:

```yaml
version: '3.8'

services:
  web:
    build: .
    container_name: django_app
    command: gunicorn News_Updater.wsgi:application --bind 0.0.0.0:8000
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - redis

  redis:
    image: redis:6.0-alpine
    container_name: redis

  celery:
    build: .
    container_name: celery_worker
    command: celery -A News_Updater worker --loglevel=info
    depends_on:
      - redis
    volumes:
      - .:/app

  celery-beat:
    build: .
    container_name: celery_beat
    command: celery -A News_Updater beat --loglevel=info
    depends_on:
      - redis
    volumes:
      - .:/app

  flower:
    build: . 
    container_name: celery_flower
    command: celery -A News_Updater flower
    ports:
      - "5555:5555"
    depends_on:
      - redis
    volumes:
      - .:/app
```

## Monitoring Celery Tasks

You can monitor Celery tasks via Flower, which is accessible at:

```bash
http://localhost:5555
```

## License

This project is licensed under the MIT License.
