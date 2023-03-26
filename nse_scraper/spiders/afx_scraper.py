from scrapy.settings.default_settings import CLOSESPIDER_PAGECOUNT, DEPTH_LIMIT
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
from scrapy.linkextractors import LinkExtractor
from nse_scraper.stock_notification import stock_query


class AfxScraperSpider(CrawlSpider):
    name = 'afx_scraper'
    allowed_domains = ['afx.kwayisi.org']
    start_urls = ['https://afx.kwayisi.org/nse/']
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    custom_settings = {
        DEPTH_LIMIT: 1,
        CLOSESPIDER_PAGECOUNT: 1
    }

    rules = (
        Rule(LinkExtractor(deny='.html', ), callback='parse_item', follow=False),
        Rule(callback='parse_item'),
    )

    def parse_item(self, response, **kwargs):
        print("Processing: " + response.url)
        # Extract data using css selectors
        row = response.css('table tbody tr ')
        # use XPath and regular expressions to extract stock name and price
        raw_ticker_symbol = row.xpath('td[1]').re('[A-Z].*')
        raw_stock_name = row.xpath('td[2]').re('[A-Z].*')
        raw_stock_price = row.xpath('td[4]').re('[0-9].*')
        raw_stock_change = row.xpath('td[5]').re('[0-9].*')

        # create a function to remove html tags from the returned list
        def clean_stock_symbol(raw_symbol):
            clean_symbol = BeautifulSoup(raw_symbol, "lxml").text
            clean_symbol = clean_symbol.split('>')
            # clean_name1 = clean_name[1].split('<')
            # print(clean_name1)
            if len(clean_symbol) > 1:
                return clean_symbol[1]
            else:
                return None

        def clean_stock_name(raw_name):
            clean_name = BeautifulSoup(raw_name, "lxml").text
            clean_name = clean_name.split('>')
            # clean_name1 = clean_name[1].split('<')
            # print(clean_name1)
            if len(clean_name[0]) > 2:
                return clean_name[0]
            else:
                return None

        def clean_stock_price(raw_price):
            clean_price = BeautifulSoup(raw_price, "lxml").text
            return clean_price

        # Use list comprehension to unpack required values
        stock_name = [clean_stock_name(r_name) for r_name in raw_stock_name]
        stock_price = [clean_stock_price(r_price) for r_price in raw_stock_price]
        ticker_symbol = [clean_stock_symbol(r_symbol) for r_symbol in raw_ticker_symbol]
        stock_change = [clean_stock_price(raw_change) for raw_change in raw_stock_change]
        scraped_data = dict()
        if ticker_symbol is not None:
            cleaned_data = zip(ticker_symbol, stock_name, stock_price)
            for item in cleaned_data:
                 scraped_data= {
                    'ticker_symbol': item[0],
                    'stock_name': item[1],
                    'stock_price': item[2],
                    'stock_change': stock_change }
        # yield info to scrapy
        yield scraped_data

    # uncom,ment to use text notifications
    # stock_query()