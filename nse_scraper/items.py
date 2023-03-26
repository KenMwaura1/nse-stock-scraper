from scrapy.item import Item, Field


class NseScraperItem(Item):
    # define the fields for your item here like:
    ticker_symbol = Field()
    stock_name = Field()
    stock_price = Field()
    stock_change = Field()
    