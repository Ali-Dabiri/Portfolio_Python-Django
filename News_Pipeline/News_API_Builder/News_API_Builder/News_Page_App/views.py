from rest_framework import generics
from .Serializer import NewsSerializer
from .models import News
from django.db.models import Q

class NewsList(generics.ListCreateAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = News.objects.all()
        filter_tags = self.request.query_params.get('tags')
        filter_keywords = self.request.query_params.get('keywords')
        filter_exclude_keywords = self.request.query_params.get('exclude_keywords')

        if filter_tags:
            queryset = queryset.filter(news_tag__icontains=filter_tags)
    
        if filter_keywords:
            keywords_list = filter_keywords.split(',')
            for keywords in keywords_list:
                    queryset = queryset.filter(
                        Q(news_content__icontains=keywords) |
                        Q(news_title__icontains=keywords)
                        )
            
        
        if filter_exclude_keywords:
            exclude_list = filter_exclude_keywords.split(',')
            for exclude in exclude_list:
                queryset = queryset.exclude(
                     Q(news_content__icontains=exclude) | 
                     Q(news_title__icontains=exclude)
                )

        return queryset
