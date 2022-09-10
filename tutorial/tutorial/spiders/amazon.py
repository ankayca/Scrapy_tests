import scrapy
import os
from time import sleep
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

basedir = os.path.dirname(os.path.realpath('__file__'))

class DribbbleSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com.tr"]
    start_urls = ['https://www.amazon.com.tr/s?i=electronics&bbn=13709907031&rh=n%3A12466496031%2Cn%3A13709880031%2Cn%3A13709907031%2Cp_n_feature_sixteen_browse-bin%3A13710916031&dc&fs=true&ds=v1%3A8r1nG18W3gHXEyln4hz8vLecS6SLzgVuZit79SbnFlI&qid=1662791208&rnid=13710915031&ref=sr_nr_p_n_feature_sixteen_browse-bin_1']


    def parse(self, response):

        # download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads
        # the version of the driver must match the version of chrome installed to work

        # instantiate a chrome options object so you can set the size and headless preference
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--incognito")
        # comment out the following line if you don't want to actually show Chrome instance
        # but you can still see that the crawling is working via output in console

        #chrome_options.add_argument("--headless")


        # comment out the following two lines to setup ProxyMesh service
        # make sure you add the IP of the machine running this script to you ProxyMesh account for IP authentication
        # IP:PORT or HOST:PORT you get this in your account once you pay for a plan

        # PROXY = "us-wa.proxymesh.com:31280"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)

        chrome_driver_path = os.path.join(basedir, 'chromedriver')
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver_path)

        driver.get('https://www.amazon.com.tr/s?i=electronics&bbn=13709907031&rh=n%3A12466496031%2Cn%3A13709880031%2Cn%3A13709907031%2Cp_n_feature_sixteen_browse-bin%3A13710916031&dc&fs=true&ds=v1%3A8r1nG18W3gHXEyln4hz8vLecS6SLzgVuZit79SbnFlI&qid=1662791208&rnid=13710915031&ref=sr_nr_p_n_feature_sixteen_browse-bin_1')
        scrapy_selector = Selector(text = driver.page_source)

        self.logger.info("*********** before scrolling ************")
        self.logger.info(scrapy_selector.css('.s-card-border').getall())
        for datas in scrapy_selector.css('.s-card-border'):
            yield{
                "name":datas.css(".a-color-base.a-text-normal::text").get(),
                "price":datas.css('.a-price-whole::text').get(),
                "url":datas.css(".a-text-normal  ::attr(href)").get()
            }
        
        
            # self.logger.info(datas.css(".a-color-base.a-text-normal::text").getall())
            # print("FIYATTT")
            # self.logger.info(datas.css('.a-price-whole::text').get())
            # self.logger.info(datas.css(".a-text-normal  ::attr(href)").get())
            # self.logger.info("*********** selammmm ************")
            
        # self.logger.info(len(scrapy_selector.css('.vcard a[data-subject]::text').getall()))

        # # designer page with an infinite scroll
        # last_height = driver.execute_script("return document.body.scrollHeight")
        # SCROLL_PAUSE_TIME = 15
        # MAX_SCROLL = 10
        # i = 0
        # while i <= MAX_SCROLL:
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     i += 1
        #     # IMPORTANT!!!
        #     # you have to get the selector again after each scrolling
        #     # in order to get the newly loaded contents
        #     scrapy_selector = Selector(text = driver.page_source)
        #     self.logger.info("*********** during scrolling ************")
        #     self.logger.info("Total scrolls executed: {}".format(i))
        #     self.logger.info("this is the current designer names extracted: {}".format(scrapy_selector.css('.vcard a[data-subject]::text').getall()))
        #     self.logger.info("Total names extracted: {}".format(len(scrapy_selector.css('.vcard a[data-subject]::text').getall())))

        #     sleep(SCROLL_PAUSE_TIME)
        #     new_height = driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height

        # self.logger.info("*********** scrolling done ************")
        # self.logger.info("final designer names extracted: {}".format(scrapy_selector.css('.vcard a[data-subject]::text').getall()))
        # self.logger.info("Final total names extracted: {}".format(len(scrapy_selector.css('.vcard a[data-subject]::text').getall())))

        # # the following demostrates how to find the search location box
        # # enter "New York" and then click the search button
        # search_location = driver.find_element_by_css_selector('#location-selectized').send_keys('New York')
        # sleep(1)
        # search_button = driver.find_element_by_css_selector('input[type="submit"]')
        # search_button.click()
        sleep(30)
        driver.quit()
#149.28.10.207


