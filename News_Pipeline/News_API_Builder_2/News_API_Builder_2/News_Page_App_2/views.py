from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import News
from .serializer import NewsSerializer
from .filters import NewsFilter

class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter
