from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import csv


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

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
    
    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)
    

    def parse(self):
        self.driver.get("https://www.reuters.com/site-search/?query=commodity+gold")

        self.list_cookies()
        time.sleep(3)

        self.driver.refresh()
        time.sleep(3)

                                                                                                
        try:                                                                                                 
            button_close_popup = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "_4ao5eF8B")))
            button_close_popup.click()
        except Exception as err:
            print(f"not found button_close_popup = {err}")
            
        try:                                                                                                 
            button_accept_cookie = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            button_accept_cookie.click()
        except Exception as err:
            print(f"not found Accept Cookies = {err}")


        try:    
            url_source_all_pages = []
            page_title_all_pages = []
            news_title_all_pages = []
            counter_page = 0 

            while counter_page <= 5:            
                self.scroll_down()
                url_source = self.driver.current_url
                url_source_all_pages.append(url_source)
                
                page_title = self.driver.title
                page_title_all_pages.append(page_title)

                all_news_title = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='fusion-app']/div[2]/div[2]/div/div[2]/div[2]/ul/li/div/div/header/a/span")))
                news_title = [title.text for title in all_news_title]
                news_title_all_pages.extend(news_title)
                if not news_title:
                    print("not found news_title.")

                self.scroll_up()
                button_next_page = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='fusion-app']/div[2]/div[2]/div/div[2]/div[3]/button[2]")))
                button_next_page.click()
                time.sleep(3)
                counter_page += 1

        except Exception as err:
            print(f"Error while navigating pages and gathering data = {err}")

        try:
            with open("Reuters_Gold_News_Search_Data.csv", "w", newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["URL Address", "Page Title", "News Title"])
                
                length_news_title = len(news_title)
                counter_lenght_news_title = 0
                counter_url_source_all_pages = 0
                counter_page_title_all_pages = 0
                for (
                    counter_news_title_all_pages
                ) in zip (
                    news_title_all_pages
                ):
                    csv_writer.writerow([url_source_all_pages[counter_url_source_all_pages], 
                                        page_title_all_pages[counter_page_title_all_pages], 
                                        ', '.join(counter_news_title_all_pages)]
                                        )
                    if counter_lenght_news_title < length_news_title:
                        counter_lenght_news_title += 1
                    if counter_lenght_news_title == length_news_title:
                        counter_url_source_all_pages += 1
                        counter_page_title_all_pages += 1
                        counter_lenght_news_title = 0
    
        except Exception as err:
            print(f"Error while writing data to CSV = {err}")

if __name__ == "__main__":
    scraper = ReutersGoldNewsSearch()
    scraper.parse()