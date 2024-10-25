from django.test import TestCase
from rest_framework.test import APIClient
from .models import News 

class NewsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        News.objects.create(news_title="Test News 1", news_content="This is test content 1", news_tag="tech", news_source="Source A")
        News.objects.create(news_title="Test News 2", news_content="This is test content 2", news_tag="sports", news_source="Source B")
    def test_get_news_list(self):
        response = self.client.get('/api/news/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        
    def test_filter_by_tag(self):
        response = self.client.get('/api/news/?tags=tech')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['news_title'], "Test News 1")
    
    def test_filter_by_keywords(self):
        response = self.client.get('/api/news/?keywords=This')
        self.assertEqual(len(response.data), 2)
        self.assertIn(response.data[1]["news_source"], ["Source A", "Source B"])
    
    def test_exclude_keywords(self):
        response = self.client.get('/api/news/?exclude_keywords=content 1')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["news_title"], "Test News 2")

    def test_filter_by_keywords_and_exclude_keywords(self):
        response = self.client.get("/api/news/?keywords=content 1&exclude_keywords=content 2")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["news_title"], "Test News 1")