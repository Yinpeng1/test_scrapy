# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    briefTitle = scrapy.Field()
    detailUrl = scrapy.Field()
    # detailTitle = scrapy.Field()
    place = scrapy.Field()
    seeNum = scrapy.Field()
    briefImg = scrapy.Field()
    likeNum = scrapy.Field()

