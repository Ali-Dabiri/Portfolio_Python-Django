import scrapy
import scrapy.selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ZoomitNewsSearchSpiderSpider(scrapy.Spider):
    name = "Zoomit_News_Search_Spider"
    allowed_domains = ["zoomit.ir"]
    start_urls = ["https://www.zoomit.ir/search/news/"]

    def __init__(self, *args, **kwargs):
        super(ZoomitNewsSearchSpiderSpider, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)
        source_url = self.driver.current_url
        time.sleep(3)
     
        try:
            button_close_advertise = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div[2]/div[4]/div/button")))
            button_close_advertise.click()
            while True:    
                button_view_more = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div[2]/div[1]/div[4]/div/div/div/div/ul/button/div")))
                button_view_more.click()
                time.sleep(10)
        except Exception:
            self.logger.info("Erro for button view more.")

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
    def close(self):
        self.driver.quit()

