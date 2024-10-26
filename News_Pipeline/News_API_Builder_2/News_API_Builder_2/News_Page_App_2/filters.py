from django_filters import rest_framework as filters
from django.db.models import Q
from .models import News

class NewsFilter(filters.FilterSet):
    tags = filters.CharFilter(field_name="news_tag", lookup_expr='icontains')
    keywords = filters.CharFilter(method='filter_keywords')
    exclude_keywords = filters.CharFilter(method='filter_exclude_keywords')

    class Meta:
        model = News
        fields = ['tags', 'keywords', 'exclude_keywords']

    def filter_keywords(self, queryset, name, value):
        keywords_list = value.split(',')
        for keyword in keywords_list:
            queryset = queryset.filter(
                Q(news_content__icontains=keyword) |
                Q(news_title__icontains=keyword)
            )
        return queryset
    
    def filter_exclude_keywords(self, queryset, name, value):
            exclude_list = value.split(',')
            for exclude in exclude_list:
                queryset = queryset.exclude(
                    Q(news_content__icontains=exclude) |
                    Q(news_title__icontains=exclude)
                )
            return queryset