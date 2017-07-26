# -*- coding: utf-8 -*-
import scrapy
from ..items import BizhiItem
from scrapy import Request

class A5857spiSpider(scrapy.Spider):
    name = '5857spi'
    allowed_domains = ['5857.com']
    start_urls = ['http://www.5857.com/pcbz/70842.html']

    def parse(self, response):
        item = BizhiItem()
        item['image_urls'] = response.xpath('//a[@class="title_czky"]/@href').extract()
        yield item
        next_page = response.xpath('//a[@class="a1"]/@href').extract()[1]
        if next_page is not None:
            print(next_page)
            next_page = response.urljoin(next_page)
            print(next_page)
            yield Request(next_page, callback=self.parse, dont_filter=True)
