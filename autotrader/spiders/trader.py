# -*- coding: utf-8 -*-
import scrapy
import json


class TraderSpider(scrapy.Spider):
    name = 'trader'
    allowed_domains = ['autotrader.com']
    #start_urls = ['http://autotrader.com/']

    custom_settings = {
        'FEED_URI': 'trader.json',
        'FEED_FORMAT': 'json'}

    def start_requests(self):
        url="https://www.autotrader.com/cars-for-sale/by-owner/Duluth+GA-30097?searchRadius=50&zip=30097&marketExtension=include&sellerTypes=p&startYear=2008&maxMileage=100000&isNewSearch=true&sortBy=relevance&numRecords=25&firstRecord=0"
        yield scrapy.Request(url)

    def parse(self, response):
        selected=response.xpath('.//script[contains(.,"window.__BONNET_DATA__=")]/text()').extract_first()
        myselected=selected[23:]
        mydict = json.loads(myselected)
        mycars=mydict['initialState']['inventory']
        return mycars
