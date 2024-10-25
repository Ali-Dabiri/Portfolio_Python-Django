from django.urls import path
from .views import NewsList

urlpatterns = [
    path('api/news/', NewsList.as_view(), name='news-list'),
]
