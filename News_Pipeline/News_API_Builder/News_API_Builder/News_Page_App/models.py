from django.db import models

class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_content = models.CharField(max_length=200)
    news_tag = models.TextField()
    news_source = models.CharField(max_length=200)
    