# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from selected_scrapy.items import WongNaiItem


class WongNaiSpider(CrawlSpider):
    name = "wongnai"
    allowed_domains = ["www.wongnai.com"]
    start_urls = [
        "https://www.wongnai.com/restaurants?regions=9681&areas=1",
    ]

    rules = [
       Rule(LinkExtractor(
            allow=['/restaurants\?areas=\d*&regions=\d*&page.number=\d*&page.size=\d*']),
            callback='parse_item',
            follow=True)
    ]

    def parse_item(self, response):
        for href in response.xpath("//div[@class='wui-result']/ul/li/div/div[@class='top']/a[@class='photoC']/@href"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = WongNaiItem()
        category, province = response.xpath("//div[@class='statistic']/div[@class='item rank']/a/text()").extract()[0].split()
        item['title'] = response.xpath("//a[@class='fn']/span/text()").extract()[0]
        item['average'] = response.xpath("//div[@class='statistic']/div[@itemprop='ratingValue']/text()").extract()[0]
        item['province'] = province
        item['category'] = category
        item['image'] = response.xpath("//div[@class='primary summary-photos']/div/a/img/@src").extract()[0]
        item.save()
