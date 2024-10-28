import scrapy
import scrapy.selector
from selenium import webdriver
import time


class ZoomitNewsSearchSpider(scrapy.Spider):
    name = "Zoomit_News_Search_Spider"
    allowed_domains = ["zoomit.ir"]
    start_urls = ["https://www.zoomit.ir/search/news/"]

    def __init__(self, *args, **kwargs):
        super(ZoomitNewsSearchSpider, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()


    def parse(self, response):
        #source_url = response.url
        self.driver.get(response.url)
        source_url = self.driver.current_url
        time.sleep(3)

        page_source = self.driver.page_source
        scrapy_selector = scrapy.Selector(text=page_source)
        all_news_search = scrapy_selector.xpath("//*[@id='__next']/div[2]/div[1]/div[4]/div/div/div/div/ul")

        news_title = all_news_search.xpath(".//span[@class='sc-63f15cb9-0 cbzARJ sc-1ff426ee-2 iEbDzs']/text()").getall()
        news_date = all_news_search.xpath(".//span[@class='fa']/text()").getall()
        news_image = all_news_search.xpath(".//img/@src").getall()
        news_study_time = all_news_search.xpath(".//span[2][@class='sc-63f15cb9-0 ktQteO fa']/text()").getall()

        for (
            news_title,
            news_date,
            news_image,
            news_study_time) in zip(
            news_title,
            news_date,
            news_image,
            news_study_time):

            yield{
                "URL Source": source_url,
                "News Title": news_title,
                "News Date": news_date,
                "News Image": news_image,
                "News Study Time": news_study_time
            }

