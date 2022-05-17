import scrapy

class BookCheck(scrapy.Spider):
    name = "books"
    allowed_domain =["avidreaders.ru"]
    start_urls = ["https://avidreaders.ru"]

    def parseLink(self, response, **kwargs):
        item = {
            "name": response.css("div.book_info h1::text").get(),
            "description": response.css("div.wrap_description p:nth-child(3)::text").get()[1:],
        }
        yield item

    def parse(self, response, **kwargs):
        genres = response.css("ul.genres_list li a::attr(href)").getall()
        yield from response.follow_all(genres)
        link = response.css("div.card_info a:last-child::attr(href)").getall()[:1000]
        yield from response.follow_all(link, callback=self.parseLink)
        href = response.css("div.pagination li:last-child a::attr(href)").getall()
        yield from response.follow_all(href)
        pass
