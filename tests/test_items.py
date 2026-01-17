"""
Tests for nse_scraper items.py - Data schema validation
"""
import unittest
from datetime import datetime
from nse_scraper.items import NseScraperItem


class TestNseScraperItem(unittest.TestCase):
    """Test NseScraperItem field definitions and validation"""

    def test_item_creation(self):
        """Test creating a valid stock item"""
        item = NseScraperItem(
            ticker_symbol="BAT",
            stock_name="Britam Holdings",
            stock_price=38.5,
            stock_change=0.5,
            created_at=datetime.now()
        )
        self.assertEqual(item["ticker_symbol"], "BAT")
        self.assertEqual(item["stock_name"], "Britam Holdings")
        self.assertEqual(item["stock_price"], 38.5)
        self.assertEqual(item["stock_change"], 0.5)
        self.assertIsInstance(item["created_at"], datetime)

    def test_item_fields(self):
        """Test that all required fields exist"""
        item = NseScraperItem()
        required_fields = ["ticker_symbol", "stock_name", "stock_price", "stock_change", "created_at"]
        
        for field in required_fields:
            self.assertIn(field, item.fields)

    def test_item_with_partial_data(self):
        """Test creating item with partial data"""
        item = NseScraperItem(
            ticker_symbol="EABL",
            stock_name="East African Breweries"
        )
        self.assertEqual(item["ticker_symbol"], "EABL")
        self.assertEqual(item["stock_name"], "East African Breweries")

    def test_stock_price_as_float(self):
        """Test stock price is stored as float"""
        item = NseScraperItem(stock_price=42.75)
        self.assertIsInstance(item["stock_price"], (int, float))
        self.assertEqual(item["stock_price"], 42.75)

    def test_stock_change_as_float(self):
        """Test stock change is stored as float"""
        item = NseScraperItem(stock_change=-0.25)
        self.assertIsInstance(item["stock_change"], (int, float))
        self.assertEqual(item["stock_change"], -0.25)


if __name__ == "__main__":
    unittest.main()
