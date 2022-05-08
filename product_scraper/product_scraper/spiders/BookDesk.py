import scrapy

class BookCheck(scrapy.Spider):
    name = "books"
    start_urls = ["https://avidreaders.ru/books/"]

    def parseLink(self, response):
        global desc
        desc = response.css("div.wrap_description p").get()

    def parse(self, response):
        for products in response.css("div.card_info"):
            self.parseLink(response)
            yield {
                "name": products.css("div.book_name a::text").get(),
                "description": desc
            }
        next_page = response.css("div.pagination li:last-child").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)