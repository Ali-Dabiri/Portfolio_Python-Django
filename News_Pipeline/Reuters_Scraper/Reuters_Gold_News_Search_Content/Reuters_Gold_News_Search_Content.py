from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import csv
from datetime import datetime, timedelta


class ReutersGoldNewsSearch:
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument("--ignore-certificate-errors")
        self.option.add_argument('--disable-web-security')
        self.option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36")
        self.option.add_argument("--disable-blink-features=AutomationControlled")
        self.option.add_experimental_option("excludeSwitches", ["enable-logging"])        
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.option)
    
    def list_cookies(self):
        cookies = self.driver.get_cookies()

        for cookie in cookies:
            self.driver.add_cookie(cookie)
    
    def close_popup(self):
        try:                                                                                                 
            button_close_popup = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "_4ao5eF8B")))
            button_close_popup.click()
        except Exception as err:
            print(f"not found button_close_popup = {err}")

    def accept_cookie(self):
        try:                                                                                                 
            button_accept_cookie = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            button_accept_cookie.click()
        except Exception as err:
            print(f"not found Accept Cookies = {err}")

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
    
    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)
    

    def parse(self):
        self.driver.get("https://www.reuters.com/site-search/?query=commodity+gold")
        
        self.list_cookies()
        time.sleep(3)
        
        self.driver.refresh()
        time.sleep(3)
        
        self.close_popup()                                                                                        
        self.accept_cookie()

        try:    
            six_months_ago = datetime.now() - timedelta(days=180)
            date_time_compare = datetime.strftime(six_months_ago, '%Y-%m-%dT%H:%M:%SZ')
            print("Six months ago:", six_months_ago)
            print("Date time compare:", date_time_compare)

            url_source_all_page = []
            page_title_all_page = []
            news_title_all_page = []
            news_date_all_page = []
            news_tag_all_page = []
            news_author_all_page = []
            news_content_all_page = []

            while date_time_compare:            
                self.scroll_down()
                self.scroll_up()

                all_news_title = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='fusion-app']/div[2]/div[2]/div/div[2]/div[2]/ul/li/div/div/header/a/span")))            
                for news_title in all_news_title:
                    news_title_text = news_title.text
                    link_news_title = WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.LINK_TEXT, news_title_text)))    
                    link_news_title.click()
                    time.sleep(4)
                                    
                    url_source_page = self.driver.current_url
                    url_source_all_page.append(url_source_page)
                    
                    self.driver.get(url_source_page)
                    time.sleep(3)                    
        
                    self.list_cookies()      
                    time.sleep(3)

                    self.driver.refresh()
                    time.sleep(3)
                    
                    self.close_popup()                                                                                        
                    self.accept_cookie()

                    self.scroll_down()
                    self.scroll_up()
                    
                    page_title_page = self.driver.title
                    page_title_all_page.append(page_title_page)

                    news_page = WebDriverWait(self.driver, 8).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='main-content']/article/div[1]/div/header/div/div/h1")))
                    news_title_page = [title.text for title in news_page]
                    news_title_all_page.extend(news_title_page)
                    if not news_title_page:
                        print("not found news_title_page.")
                                                                                                                                        
                    all_news_date_page = WebDriverWait(self.driver, 7).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='main-content']/article/div[1]/div/header/div/div/div[1]/div[1]/time")))
                    news_date_page = [date.get_attribute('datetime') for date in all_news_date_page]
                    news_date_all_page.extend(news_date_page)
                    if not news_date_page:
                        print("not found news_date_page.")
                                                                                                                         
                    all_news_tag_page = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='main-content']/article/div[1]/div/header/div/div/span/nav/ul/li/a")))
                    news_tag_page = ', '.join([tag.text for tag in all_news_tag_page])
                    news_tag_all_page.append(news_tag_page)
                    if not news_tag_page:
                        print("not found news_tag_page.")
                                                                                                                                    
                    all_news_author_page_path = WebDriverWait(self.driver, 6).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='main-content']/article/div[1]/div/header/div/div/div/div[1]/div[@class='text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__tag_label__6ajML']")))
                    if all_news_author_page_path:                        
                        try:     
                            if WebDriverWait(self.driver, 6).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='main-content']/article/div[1]/div/header/div/div/div/div[1]/div/a[@class='text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__tag_label__6ajML link__link__3Ji6W link__underline_on_hover__2zGL4 author-name__author__au-bT']"))):
                                all_news_author_page = WebDriverWait(self.driver, 6).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='main-content']/article/div[1]/div/header/div/div/div/div[1]/div/a[@class='text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__tag_label__6ajML link__link__3Ji6W link__underline_on_hover__2zGL4 author-name__author__au-bT']")))
                        except Exception as err:
                            print(f"not found xpath = {err}")  
                        try:
                            if WebDriverWait(self.driver, 6).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='main-content']/article/div[1]/div/header/div/div/div/div[1]/div/span[2][@class='text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__tag_label__6ajML']"))):
                                all_news_author_page = WebDriverWait(self.driver, 6).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='main-content']/article/div[1]/div/header/div/div/div/div[1]/div/span[2][@class='text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__tag_label__6ajML']")))
                        except Exception as err:
                            print(f"not found xpath = {err}")       
                        news_author_page = ', '.join([author.text for author in all_news_author_page])
                        news_author_all_page.append(news_author_page)
                        if not news_author_page:
                            print("not found news_author_page.")

                    all_news_content_page = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='main-content']/article/div[1]/div/div/div/div[2]/div[@class='text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__small__1kGq2 body__full_width__ekUdw body__small_body__2vQyf article-body__paragraph__2-BtD']")))
                    news_content_page = ' \n'.join([content.text for content in all_news_content_page])
                    news_content_page = news_content_page.replace("\n, opens new tab\n", " ")
                    news_content_all_page.append(news_content_page)
                    if not news_content_page:
                        print("not found news_content_page.")
                    
                
                    self.driver.back()
                    time.sleep(3)
                    
                
                button_next_page = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='fusion-app']/div[2]/div[2]/div/div[2]/div[3]/button[2]")))
                button_next_page.click()
                time.sleep(3)
                
                if news_date_all_page[-1] >= date_time_compare:
                    continue
                else:
                    break

        except Exception as err:
            print(f"Error while navigating pages and gathering data = {err}")

        try:
            with open("Reuters_Gold_News_Search_Content_Data.csv", "w", newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["URL Address", "Page Title", "News Title", "News Date", "News Tag", "News Author", "News Content"])
                
                for (
                    counter_url_source_all_page,
                    counter_page_title_all_page,
                    counter_news_title_page,
                    counter_news_date_all_page,
                    counter_news_tag_all_page,
                    counter_news_author_all_page,
                    counter_news_content_all_page
                ) in zip (
                    url_source_all_page,
                    page_title_all_page,
                    news_title_all_page,
                    news_date_all_page,
                    news_tag_all_page,
                    news_author_all_page,
                    news_content_all_page
                ):
                    if counter_news_date_all_page >= date_time_compare:    
                        csv_writer.writerow([counter_url_source_all_page,
                                            counter_page_title_all_page,
                                            counter_news_title_page,
                                            counter_news_date_all_page,
                                            counter_news_tag_all_page,
                                            counter_news_author_all_page,
                                            counter_news_content_all_page])                
                        
        except Exception as err:
            print(f"Error while writing data to CSV = {err}")

if __name__ == "__main__":
    scraper = ReutersGoldNewsSearch()
    scraper.parse()