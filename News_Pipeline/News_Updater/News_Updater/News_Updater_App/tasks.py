from celery import shared_task

@shared_task
def update_news():
    print("Updating news database...")
    return "News database updated."