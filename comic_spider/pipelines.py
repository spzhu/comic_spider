# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests


class ComicSpiderPipeline(object):
    def process_item(self, item, spider):
        basedir = os.getcwd()
        path = "{}/{}/{}".format(basedir, item['comic'], item['chapter'])
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + '/{}{}'.format(item['img_page'], item['img_url'][-4:]), 'wb') as f:
            f.write(requests.get(item['img_url']).content)
        return item
