# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    comic = scrapy.Field()
    chapter = scrapy.Field()
    img_page = scrapy.Field()
    img_url = scrapy.Field()
