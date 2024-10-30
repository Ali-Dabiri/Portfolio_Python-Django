import scrapy
import scrapy.selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ZoomitNewsSearchContentSpider(scrapy.Spider):
    name = "Zoomit_News_Search_Content_Spider"
    allowed_domains = ["zoomit.ir"]
    start_urls = ["https://www.zoomit.ir/search/news/"]

    def __init__(self, *args, **kwargs):
        super(ZoomitNewsSearchContentSpider, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)
        url_source = self.driver.current_url
        time.sleep(3)

        try:
            button_close_advertise = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div[2]/div[4]/div/button")))
            button_close_advertise.click()
            counter = 0
            while counter <= 5:    
                button_view_more = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div[2]/div[1]/div[4]/div/div/div/div/ul/button/div")))
                button_view_more.click()
                time.sleep(10)
                counter += 1
        except Exception:
            self.logger.info("Error for button view more.")


        page_source = self.driver.page_source
        scrapy_selector = scrapy.Selector(text=page_source)
        all_news_search = scrapy_selector.xpath("//*[@id='__next']/div[2]/div[1]/div[4]/div/div/div/div/ul")

        news_page_link = all_news_search.xpath(".//div[@class='sc-73a1c33f-0 cWbCJr']/a[@class='sc-f3acbc5d-0 ebqeWo']/@href").getall()
        
        for news_page_link_follow in news_page_link:
            collection_news_page_link = response.urljoin(news_page_link_follow)
            request_news_page_link = scrapy.Request(url=collection_news_page_link, callback=self.page_parse)
            yield(
                request_news_page_link
            )

    def page_parse(self, response):
        news_page_url_source = response.url
        all_news_page_header = response.xpath("//*[@id='__next']/div[2]/div[1]/main/article/header/div/div")

        news_page_title = all_news_page_header.xpath(".//h1/text()").getall()
        news_page_date = all_news_page_header.xpath(".//div[2]/span[1]/text()").getall()
        news_page_author = all_news_page_header.xpath(".//div[3]/a/div/span/text()").getall()
        news_page_tags = all_news_page_header.xpath(".//div[2]/div[1]/a/span[@class='sc-63f15cb9-0 cnEXvu']/text()").getall()
        news_page_study_time = all_news_page_header.xpath(".//div[2]/span[2]/text()").getall()
        news_page_content = response.xpath("//*[@id='__next']/div[2]/div[1]/main/article/div/div[5]/div/div/div/p[@class='sc-63f15cb9-0 chyqyp sc-4bdf9365-0 brkdqE']/text()").getall()

        for (
            news_page_title,
            news_page_date,
            news_page_author,
            news_page_study_time,
        ) in zip(
            news_page_title,
            news_page_date,
            news_page_author,
            news_page_study_time,
        ):
            yield{
                "News Page Url Source": news_page_url_source,
                "News Page Title": news_page_title,
                "News Page Date": news_page_date,
                "News Page Author": news_page_author,
                "News Page Tags": news_page_tags,
                "News Page Study Time": news_page_study_time,
                "News Page Content": news_page_content
            }
    
    def close(self):
        self.driver.quit()


 