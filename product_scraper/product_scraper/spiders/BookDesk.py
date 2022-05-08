import scrapy

class BookCheck(scrapy.Spider):
    name = "books"
    start_urls = ["https://avidreaders.ru/books/"]

    def parse(self, response):
        for products in response.css("div.card_info"):
            yield {
                "name" : products
            }
