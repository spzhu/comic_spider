# -*- coding: utf-8 -*-
import scrapy
from comic_spider.items import ComicSpiderItem
from selenium import webdriver


class ComicspiderSpider(scrapy.Spider):
    name = 'comicspider'
    allowed_domains = ['sfacg.com']
    start_urls = ['http://comic.sfacg.com/HTML/JQRDLSGEF/']

    def parse(self, response):
        url_list = []
        try:
            lis = response.xpath('//ul[@class="serialise_list Blue_link2"]/li')
            for li in lis:
                url = 'http://comic.sfacg.com' + li.xpath('./a/@href').extract()[0]
                print(url)
                yield scrapy.Request(url, callback = self.get_chapter_img)
        except:
            raise


    def get_chapter_img(self, response):
        browser = webdriver.PhantomJS()
        browser.get(response.url)
        browser.implicitly_wait(3)
        page_num = len(browser.find_elements_by_tag_name('option'))
        next_page = browser.find_element_by_xpath('//div[@class="page_turning AD_D2"]/a[4]')
        for page in range(page_num):
            item = ComicSpiderItem()
            try:
                item['comic'] = browser.find_element_by_xpath('//div[@class="Reduction_left"]/a[3]').text
                item['chapter'] = browser.find_element_by_xpath('//div[@class="Reduction_left"]').text[-4:] 
                item['img_page'] = browser.find_element_by_id('CurrentPage').text
                item['img_url'] = browser.find_element_by_id('curPic').get_attribute('src')
            except:
                raise
            next_page.click()
            browser.implicitly_wait(3)
            yield item
        browser.quit()

