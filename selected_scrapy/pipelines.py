# -*- coding: utf-8 -*-
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class SelectedScrapyPipeline(object):
    def process_item(self, item, spider):
        return item
