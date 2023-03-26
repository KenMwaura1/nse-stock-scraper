# useful for handling different item types with a single interface
import pymongo
from scrapy.exceptions import DropItem

from .items import NseScraperItem


class NseScraperPipeline:
    collection = "stock_data"

    def __init__(self, mongodb_uri, mongo_db):
        self.db = None
        self.client = None
        self.mongodb_uri = mongodb_uri
        self.mongo_db = mongo_db
        if not self.mongodb_uri:
            raise ValueError("MongoDB URI not set")
        if not self.mongo_db:
            raise ValueError("Mongo DB not set")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get("MONGODB_URI"),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'nse_data')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongo_db]
        # self.db[self.collection].create_index('stock_ticker')
        # self.client.test.test.insert_one({'test': 'test'})
        # Start with a clean database
        # self.db[self.collection].delete_many({})

    def close_spider(self, spider):
        self.client.close()
    
    def clean_stock_data(self,item):
        if item['ticker_symbol'] is None:
            raise DropItem('Missing ticker symbol in %s' % item)
        elif item['stock_name'] == 'None':
            raise DropItem('Missing stock name in %s' % item)
        elif item['stock_price'] == 'None':
            raise DropItem('Missing stock price in %s' % item)
        else:
            return item

    def process_item(self, item, spider):
        """
        process item and store to database
        """
        """
        if isinstance(item, NseScraperItem):
            data = dict(NseScraperItem(item))
            self.db[self.collection].insert_one(dict(data))
        """
        clean_stock_data = self.clean_stock_data(item)
        data = dict(NseScraperItem(clean_stock_data))
        print(data)
        # print(self.db[self.collection].insert_one(data).inserted_id)
        self.db[self.collection].insert_one(data)

        return item
