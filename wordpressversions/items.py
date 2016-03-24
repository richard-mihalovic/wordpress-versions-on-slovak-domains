import scrapy


class WordpressVersionItem(scrapy.Item):
    version = scrapy.Field()
