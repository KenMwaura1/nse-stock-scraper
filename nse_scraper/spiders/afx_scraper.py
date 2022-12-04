from scrapy.spiders import CrawlSpider, Request
from bs4 import BeautifulSoup
from scrapy.spiders import Rule
# from scrapy.linkextractors import LinkExtractor


class AfxScraperSpider(CrawlSpider):
    name = 'afx_scraper'
    allowed_domains = ['afx.kwayisi.org']
    start_urls = ['https://afx.kwayisi.org/nse/']

    rules = (
        # Rule(LinkExtractor(allow='s?k=laptop&page=', restrict_css="a.s-pagination-next")),
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

        # print(raw_ticker_symbol)

        # create a function to remove html tags from the returned list
        def clean_stock_name(raw_name):
            clean_name = BeautifulSoup(raw_name, "lxml").text
            clean_name = clean_name.split('>')
            return clean_name[0]

        def clean_stock_price(raw_price):
            clean_price = BeautifulSoup(raw_price, "lxml").text
            return clean_price

        # Use list comprehension to unpack required values
        stock_name = [clean_stock_name(r_name) for r_name in raw_stock_name]
        stock_price = [clean_stock_price(r_price) for r_price in raw_stock_price]
        stock_symbol = [clean_stock_name(r_symbol) for r_symbol in raw_ticker_symbol]
        # using list slicing to remove the unnecessary data
        stock_symbol = stock_symbol[6:]
        # print(stock_symbol)
        cleaned_data = zip(stock_symbol, stock_name, stock_price)
        for item in cleaned_data:
            scraped_data = {
                'ticker': item[0],
                'name': item[1],
                'price': item[2],
            }
            # yield info to scrapy
            yield scraped_data
