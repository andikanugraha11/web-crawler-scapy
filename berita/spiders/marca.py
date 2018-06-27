# -*- coding: utf-8 -*-
import scrapy


class MarcaSpider(scrapy.Spider):
    name = 'marca'
    allowed_domains = ['www.marca.com/en']
    start_urls = ['http://www.marca.com/en/']

    def parse(self, response):
        pass
