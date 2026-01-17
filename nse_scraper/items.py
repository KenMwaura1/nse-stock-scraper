from scrapy.item import Item, Field


class NseScraperItem(Item):
    """Item for holding stock data"""
    ticker_symbol = Field()
    stock_name = Field()
    stock_price = Field()
    stock_change = Field()
    created_at = Field()
