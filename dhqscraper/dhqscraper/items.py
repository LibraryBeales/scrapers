# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags
import re

def remove_multispaces(value):
    return re.sub.value.strip()    
#.replace('\n', ' ').replace('\t','')


class DhqscraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    year = scrapy.Field()
    volume = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field
    #original_file_name = scrapy.Field()

