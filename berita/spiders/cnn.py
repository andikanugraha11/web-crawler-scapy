# -*- coding: utf-8 -*-
import scrapy
from termcolor import colored

class CnnSpider(scrapy.Spider):
    name = 'cnn'
    allowed_domains = ['edition.cnn.com']
    start_urls = [
        'http://edition.cnn.com/regions/',
        'http://edition.cnn.com/africa'
        ]

    def parse(self, response):
        for link in response.xpath('//article/div/div[@class="cd__content"]/h3/a/@href').extract():
            if(link.endswith('index.html')):
                
                full_link = 'https://www.edition.cnn.com'+link
                print(colored(full_link, 'red'))
                yield response.follow(full_link, self.get_article)
    
    def get_article(self, response):
        title = response.css('h1.pg-headline::text').extract_first()
        print(colored(title, 'green'))

        yield {
            'title': title
            # 'body': price
        }
