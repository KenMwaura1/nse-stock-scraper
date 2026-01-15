# Project Structure Guide

## Directory Organization

### Root Level Files

```
├── Dockerfile              # Multi-stage Docker image definition
├── docker-compose.yml      # Local development with MongoDB
├── requirements.txt        # Python package dependencies
├── scrapy.cfg             # Scrapy project configuration
├── LICENSE                # MIT License
└── README.md              # Main project documentation
```

### `/docs` - Documentation & Media

All project documentation centralized in one folder:

```
docs/
├── INDEX.md               # Documentation index (this folder's guide)
├── README.md              # [DEPRECATED - kept for reference]
├── QUICKSTART.md          # Quick reference for common commands
├── DOCKER.md              # Comprehensive Docker deployment guide
├── IMPROVEMENTS.md        # Detailed changelog of fixes & improvements
└── images/
    ├── nse-scraper.png    # App screenshot
    ├── Atlas-DB.png       # Database screenshot
    └── charts-dashboard.png # Charts dashboard screenshot
```

### `/config` - Configuration Files

Environment and config templates:

```
config/
├── .env.example           # Template for local development
└── .env.docker            # Template for Docker setup
```

**Usage:**

```bash
cp config/.env.example .env
# Edit with your credentials
```

### `/nse_scraper` - Main Application

Core Scrapy project code:

```
nse_scraper/
├── __init__.py            # Package initialization
├── items.py               # Scrapy item definitions (data schema)
├── pipelines.py           # Data processing pipelines (validation, MongoDB)
├── middlewares.py         # Custom middlewares (if needed)
├── settings.py            # Scrapy configuration (logging, concurrency, etc.)
├── stock_notification.py  # SMS notification script (Africa's Talking)
├── spiders/               # Spider implementations
│   ├── __init__.py
│   └── afx_scraper.py    # Main AFX NSE web scraper
└── migrations/            # Database migration scripts (future use)
    └── .gitkeep
```

**Key Files:**

- `afx_scraper.py` - Scrapes stock prices from AFX website
- `pipelines.py` - Validates and stores data in MongoDB
- `stock_notification.py` - Sends SMS alerts for price changes
- `settings.py` - Configures Scrapy (logging, delays, retries, etc.)

### `/tests` - Test Files & Test Data

Test data and test outputs:

```
tests/
├── example-data.json      # Example raw scraped data format
├── test.json              # Test output from scraper runs
├── example.json           # Additional test examples
└── .gitkeep               # Maintains directory in git
```

### `/.github` - GitHub Configuration

CI/CD and automation:

```
.github/
├── workflows/             # GitHub Actions workflows
│   ├── python-app.yml    # Main CI/CD pipeline (Lint, Security, Test, Build)
│   └── scraper-test.yml  # Dedicated scraper testing
└── dependabot.yml        # Automated dependency updates config
```

## Optimization Rationale

### Why Organize This Way?

1. **`/docs` Folder**
   - ✅ Centralized documentation (easier to find)
   - ✅ Keeps root directory clean
   - ✅ Images organized with docs
   - ✅ Documentation can be versioned with code
   - ✅ GitHub automatically recognizes `/docs` for GitHub Pages

2. **`/config` Folder**
   - ✅ Separates configuration from code
   - ✅ Easy to see all config templates
   - ✅ Clear where to find environment setup
   - ✅ Can expand with database configs, logging configs, etc.

3. **`/tests` Folder**
   - ✅ Test data separate from main app
   - ✅ Easy to exclude from production deployments
   - ✅ Clear testing artifacts location
   - ✅ Room for future unit tests

4. **`/nse_scraper` Structure**
   - ✅ Follows Scrapy best practices
   - ✅ `spiders/` clearly separate spider implementations
   - ✅ Added `migrations/` for future database schema changes
   - ✅ Standard package structure (easy to maintain)

## Environment Files

### Local Development

```bash
# Copy template
cp config/.env.example .env

# Edit with your credentials
nano .env
```

### Docker Development

```bash
# Copy Docker template
cp config/.env.docker .env

# Edit with credentials
nano .env
```

**Files are git-ignored:**

- `.env` (local)
- `.env.docker` (if using in root, not in config/)

## Building & Running

### Local (Python)

```bash
# Install dependencies
pip install -r requirements.txt

# Run scraper
scrapy crawl afx_scraper

# Send notifications
python nse_scraper/stock_notification.py
```

### Docker

```bash
# Build and run
docker-compose up --build

# View logs
docker-compose logs -f scraper

# Stop services
docker-compose down
```

## Adding New Files

### Adding Documentation

→ Place in `docs/` and reference in `docs/INDEX.md`

### Adding Configuration

→ Place in `config/` with `.example` or `.docker` suffix

### Adding Spiders

→ Create in `nse_scraper/spiders/` following naming convention

### Adding Tests

→ Place test data in `tests/` directory

### Adding Database Migrations

→ Place in `nse_scraper/migrations/` with timestamp prefix

## Key Paths for Common Tasks

| Task | Path |
|------|------|
| View documentation | `docs/INDEX.md` |
| Update environment | `cp config/.env.example .env` |
| Run main spider | `nse_scraper/spiders/afx_scraper.py` |
| View test data | `tests/example-data.json` |
| Check CI/CD | `.github/workflows/python-app.yml` |
| Scrapy config | `nse_scraper/settings.py` |
| Data validation | `nse_scraper/pipelines.py` |

## Summary

The reorganized structure:

- ✅ **Cleaner root** - Only essential files at root
- ✅ **Centralized docs** - All documentation in `/docs`
- ✅ **Clear config** - All templates in `/config`
- ✅ **Organized tests** - Test data in `/tests`
- ✅ **Standard layout** - Follows Python/Scrapy conventions
- ✅ **Easy to scale** - Room for new spiders, migrations, utilities

This structure makes the project easier to navigate, maintain, and extend.
