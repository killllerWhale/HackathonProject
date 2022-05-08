import scrapy

class BookCheck(scrapy.Spider):
    name = "books"
    start_urls = ["https://avidreaders.ru/books/"]

    def parseLink(self, response):
        for products in response.css("div.wrap_description"):
            yield {
                "description": products.css("p").get()
            }



    def parse(self, response):
        for products in response.css("div.card_info"):
            yield {
                "name" : products.css("div.book_name a::text").get()
            }
