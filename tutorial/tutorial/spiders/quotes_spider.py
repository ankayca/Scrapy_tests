
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #page = response.url.split("/")[-2]
        self.counter = 0
        for t in response.css(".quote"):
            print("hello boyyy******************" + str(self.counter))
            self.counter = self.counter +1
            yield {
                'text':t.css(".text::text").get().replace('"' ,''),
                'author':t.css(".author::text").get().replace('"' ,''),
                'tags':t.css(".tag::text").getall()}
        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
        print("------------------" + next_page)
