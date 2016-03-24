import re
import scrapy
from wordpressversions.items import WordpressVersionItem


class WordpressVersionsSpider(scrapy.Spider):
    name = "wordpress_versions"

    start_urls = []

    def __init__(self):
        super(WordpressVersionsSpider, self).__init__()

        urls_to_process = []

        with open('domains.txt') as f:
            lines = f.read().splitlines()

        for line in lines:
            urls_to_process.append(
                'http://' + line + '/readme.html'
            )

        self.start_urls = urls_to_process

    def parse(self, response):
        regex = re.compile(r'wordpress', re.IGNORECASE)
        is_wordpress = len(response.xpath('//title/text()').re(regex)) > 0
        if not is_wordpress:
            return

        version_parts = re.search(
            r"Version ([0-9]+).([0-9]+).?([0-9]+?)",
            response.body,
            re.I
        ).groups()

        print version_parts
        version = '.'.join(version_parts)

        item = WordpressVersionItem()
        item['version'] = version

        yield item
