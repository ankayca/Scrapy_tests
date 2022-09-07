from ctypes import sizeof
import scrapy


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
        for t in range(0,len(response.css(".text::text").getall())):
            print("hello boyyy*******************" + str(self.counter))
            self.counter = self.counter +1
            print(response.css(".text::text")[t].get())
            # filename = f'quotes-{t}.html'
            # with open(filename, 'wb') as f:
            #     f.write(response.body)
            # self.log(f'Saved file {filename}')
            