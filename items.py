# Define here the models for your scraped items

import scrapy
from itemloaders.processors import TakeFirst,MapCompose
from w3lib.html import remove_tags


def remove_currency(value):
    return value.replace('£','').strip()


class WiskeyscraperItem(scrapy.Item):
    
    name = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags,remove_currency),output_processor = TakeFirst())
    link = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
