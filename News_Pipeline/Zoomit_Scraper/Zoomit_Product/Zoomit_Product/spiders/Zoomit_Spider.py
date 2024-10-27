import scrapy


class ZoomitSpiderSpider(scrapy.Spider):
    name = "Zoomit_Spider"
    allowed_domains = ["zoomit.ir"]
    start_urls = [
        "https://www.zoomit.ir/product/list/mobile/",
        "https://www.zoomit.ir/product/list/tablet/",
        "https://www.zoomit.ir/product/list/laptop/",
        "https://www.zoomit.ir/product/list/tv/",
        "https://www.zoomit.ir/product/list/wearables/",
        "https://www.zoomit.ir/product/list/headphone/",
        "https://www.zoomit.ir/product/list/hdd/",
        "https://www.zoomit.ir/product/list/gaming-console/"
        ]

    def parse(self, response):
        source_url = response.url
        all_product_search = response.xpath("//*[@id='__next']/div[2]/form/div/div[3]/div/div[2]/div[2]/div[3]")
                                        
        product_name = all_product_search.xpath(".//a/span/text()").getall()
        product_price = all_product_search.xpath(".//p/span/text()").getall()
        product_score = all_product_search.xpath(".//span[@class='sc-63f15cb9-0 kEpdZx fa']/text()").getall()
        product_image = all_product_search.xpath(".//div/img/@src").getall()
        product_specifications_1 = all_product_search.xpath(".//div[2]/div[1]/span[1]/text()").getall()
        product_specifications_2 = all_product_search.xpath(".//div[2]/div[1]/span[2]/text()").getall()
        product_specifications_3 = all_product_search.xpath(".//div[2]/div[2]/span[1]/text()").getall()
        product_specifications_4 = all_product_search.xpath(".//div[2]/div[2]/span[2]/text()").getall()
        product_specifications_5 = all_product_search.xpath(".//div[2]/div[3]/span[1]/text()").getall()
        product_specifications_6 = all_product_search.xpath(".//div[2]/div[3]/span[2]/text()").getall()
        product_specifications_7 = all_product_search.xpath(".//div[2]/div[4]/span[1]/text()").getall()
        product_specifications_8 = all_product_search.xpath(".//div[2]/div[4]/span[2]/text()").getall()

        for (
            product_name,
            product_price,
            product_score,
            product_image,
            product_specifications_1,
            product_specifications_2,
            product_specifications_3,
            product_specifications_4,
            product_specifications_5,
            product_specifications_6,
            product_specifications_7,
            product_specifications_8) in zip (
            product_name,
            product_price,
            product_score,
            product_image,
            product_specifications_1,
            product_specifications_2,
            product_specifications_3,
            product_specifications_4,
            product_specifications_5,
            product_specifications_6,
            product_specifications_7,
            product_specifications_8):
            yield{
                "Source URL": source_url,
                "Product Name": product_name,
                "Product Price": product_price,
                "Product Score": product_score,
                "Product_Image": product_image,
                "Product Specifications_1": product_specifications_1,
                "Product Specifications_2": product_specifications_2,
                "Product Specifications_3": product_specifications_3,
                "Product Specifications_4": product_specifications_4,
                "Product Specifications_5": product_specifications_5,
                "Product Specifications_6": product_specifications_6,
                "Product Specifications_7": product_specifications_7,
                "Product Specifications_8": product_specifications_8
            }
