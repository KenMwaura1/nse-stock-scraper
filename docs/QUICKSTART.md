# Quick Start After Updates

## 1. Update Dependencies
```bash
pip install -r requirements.txt --upgrade
```

## 2. Set Up Environment
```bash
cp .env.example .env
# Edit .env with your credentials
nano .env
```

## 3. Test the Scraper
```bash
# Run and preview in JSON
scrapy crawl afx_scraper -o test.json

# Watch logs in real-time
scrapy crawl afx_scraper --loglevel=DEBUG
```

## 4. Test Notifications
```bash
python nse_scraper/stock_notification.py
```

## 5. Schedule for Production

### Option A: Heroku with Advanced Scheduler
```
Command: python nse_scraper/stock_notification.py
Schedule: Daily 11:00 AM
Timezone: Africa/Nairobi
```

### Option B: Linux/Mac Cron
```bash
# Edit crontab
crontab -e

# Add (runs daily at 11 AM)
0 11 * * * cd /path/to/nse-stock-scraper && python nse_scraper/stock_notification.py
```

### Option C: Docker
```bash
docker run -d \
  -e MONGODB_URI="your_connection_string" \
  -e at_username="your_username" \
  -e at_api_key="your_api_key" \
  -e mobile_number="your_number" \
  -e MONGODB_DATABASE="nse_data" \
  your-image:latest \
  python nse_scraper/stock_notification.py
```

## Key Improvements Made

| Aspect | Before | After |
|--------|--------|-------|
| Spider Type | CrawlSpider (Rules) | Simple Spider (parse()) |
| Stock Price | String | Float |
| Timestamps | None | created_at added |
| Stock Change | List (bug) | Parsed float |
| Duplicate Data | Unbounded inserts | Unique index + upsert |
| Logging | print() statements | Proper logging module |
| Dependencies | 2020-2021 versions | 2023-2024 versions |
| Configuration | Hardcoded | Settings file + .env |
| Error Handling | Minimal | Comprehensive |
| Documentation | Sparse | Complete |

## Files Changed

### Modified
- ✏️ `nse_scraper/spiders/afx_scraper.py` - Complete refactor
- ✏️ `nse_scraper/stock_notification.py` - Fixed import issue + improvements
- ✏️ `nse_scraper/pipelines.py` - Better validation + MongoDB indexing
- ✏️ `nse_scraper/items.py` - Added created_at field
- ✏️ `nse_scraper/settings.py` - Modern configuration
- ✏️ `requirements.txt` - Updated all packages
- ✏️ `README.md` - Enhanced documentation
- ✏️ `.gitignore` - Fixed merge conflicts

### Created
- ➕ `.env.example` - Configuration template
- ➕ `images/.gitkeep` - Preserve directory
- ➕ `IMPROVEMENTS.md` - Detailed change log

## Debugging Tips

```bash
# See detailed logs
scrapy crawl afx_scraper --loglevel=DEBUG

# Check MongoDB connection
python -c "import pymongo; from dotenv import load_dotenv; import os; load_dotenv(); print(pymongo.MongoClient(os.getenv('MONGODB_URI')).admin.command('ping'))"

# Test notification manually
python nse_scraper/stock_notification.py

# Check cached data
ls -la httpcache/
```

## Common Issues & Solutions

### ImportError: No module named 'nse_scraper'
```bash
# Make sure you're in the project root
cd /path/to/nse-stock-scraper
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### MongoDB connection timeout
- Check firewall/IP whitelist in MongoDB Atlas
- Verify MONGODB_URI format is correct
- Check network connectivity

### SMS not sending
- Verify Africa's Talking credentials
- Check account balance
- Ensure phone number format: +254XXXXXXXXX

---
For more details, see [IMPROVEMENTS.md](IMPROVEMENTS.md) and [README.md](README.md)
