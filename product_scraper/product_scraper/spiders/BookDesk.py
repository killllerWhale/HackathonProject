import scrapy

class BookCheck(scrapy.Spider):
    name = "books"
    start_urls = ["https://avidreaders.ru/books/"]

    def parse(self, response):

