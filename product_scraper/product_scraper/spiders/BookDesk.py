import scrapy

class BookCheck(scrapy.Spider):
    name = "books"
    start_urls = ["https://avidreaders.ru/books/"]

    def parseLink(self, response):
        desc = response.css("div.wrap_description:nth-child(3)").get()
        return desc

    def parse(self, response):
        for products in response.css("div.card_info"):
            link = products.css("div.card_info a:last-child").attrib['href']
            description = self.parseLink(link)
            yield {
                "name": products.css("div.book_name a::text").get(),
                "description": description,
            }
        next_page = response.css("div.pagination li:last-child a").attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
