import os
from dotenv import load_dotenv

load_dotenv()

BOT_NAME = 'nse_scraper'

SPIDER_MODULES = ['nse_scraper.spiders']
NEWSPIDER_MODULE = 'nse_scraper.spiders'

# MongoDB configuration
MONGODB_URI = os.getenv("MONGODB_URI")
MONGO_DATABASE = os.getenv("MONGODB_DATABASE", "nse_data")

# Item pipelines
ITEM_PIPELINES = {
    'nse_scraper.pipelines.NseScraperPipeline': 300,
}

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# User agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

# Request settings
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
}

# Concurrent requests (be respectful)
CONCURRENT_REQUESTS = 8
CONCURRENT_REQUESTS_PER_DOMAIN = 2

# Download delay (be respectful to target server)
DOWNLOAD_DELAY = 1

# HTTP Cache settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 3600  # Cache for 1 hour instead of 6 minutes
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Retry settings
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

# AutoThrottle (optional, but recommended)
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
