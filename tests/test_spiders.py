"""
Tests for nse_scraper spiders - Spider functionality
"""
import unittest
from scrapy import Request
from nse_scraper.spiders.afx_scraper import AfxScraperSpider


class TestAfxScraperSpider(unittest.TestCase):
    """Test AfxScraperSpider configuration and methods"""

    def setUp(self):
        """Set up spider instance for testing"""
        self.spider = AfxScraperSpider()

    def test_spider_name(self):
        """Test spider has correct name"""
        self.assertEqual(self.spider.name, "afx_scraper")

    def test_spider_allowed_domains(self):
        """Test spider allowed domains are configured"""
        self.assertIn("afx.kwayisi.org", self.spider.allowed_domains)

    def test_spider_start_urls(self):
        """Test spider has start URLs"""
        self.assertTrue(len(self.spider.start_urls) > 0)
        self.assertIn("afx.kwayisi.org", self.spider.start_urls[0])

    def test_clean_text_method(self):
        """Test _clean_text removes whitespace"""
        result = self.spider._clean_text("  Hello World  ")
        self.assertEqual(result, "Hello World")
        
        result = self.spider._clean_text("Multiple  Spaces")
        self.assertNotIn("  ", result)

    def test_clean_price_conversion(self):
        """Test _clean_price converts string to float"""
        # Valid price
        result = self.spider._clean_price("42.50")
        self.assertEqual(result, 42.50)
        self.assertIsInstance(result, float)
        
        # Integer price
        result = self.spider._clean_price("100")
        self.assertEqual(result, 100.0)

    def test_clean_price_invalid(self):
        """Test _clean_price handles invalid input"""
        result = self.spider._clean_price("invalid")
        self.assertIsNone(result)
        
        result = self.spider._clean_price("")
        self.assertIsNone(result)
        
        result = self.spider._clean_price(None)
        self.assertIsNone(result)

    def test_spider_has_parse_method(self):
        """Test spider has parse method"""
        self.assertTrue(hasattr(self.spider, "parse"))
        self.assertTrue(callable(self.spider.parse))


if __name__ == "__main__":
    unittest.main()
