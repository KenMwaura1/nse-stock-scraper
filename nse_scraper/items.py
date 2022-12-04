# Define here the models for your scraped items

# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field


class NseScraperItem(Item):
    # define the fields for your item here like:
    stock_name = Field()
    stock_price = Field()
    stock_symbol = Field()
