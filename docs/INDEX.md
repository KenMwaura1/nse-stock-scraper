# Documentation Index

Complete documentation for the NSE Stock Scraper project.

## Main Documentation

- **[README.md](../README.md)** - Project overview, installation, and getting started
- **[QUICKSTART.md](QUICKSTART.md)** - Quick reference guide for common tasks
- **[DOCKER.md](DOCKER.md)** - Comprehensive Docker deployment guide
- **[IMPROVEMENTS.md](IMPROVEMENTS.md)** - Detailed changelog of all improvements and fixes

## Project Structure

```
nse-stock-scraper/
├── docs/                      # All documentation and images
│   ├── INDEX.md              # This file
│   ├── README.md             # Project overview
│   ├── QUICKSTART.md         # Quick reference
│   ├── DOCKER.md             # Docker guide
│   ├── IMPROVEMENTS.md       # Changelog
│   └── images/               # Screenshots and diagrams
├── config/                    # Configuration files
│   ├── .env.example          # Example environment variables
│   └── .env.docker           # Docker-specific environment
├── tests/                     # Test files and test data
│   ├── example-data.json     # Example scraped data
│   ├── test.json             # Test output file
│   └── .gitkeep              # Keeps empty directories in git
├── nse_scraper/              # Main application package
│   ├── spiders/              # Scrapy spiders
│   │   └── afx_scraper.py   # AFX NSE spider
│   ├── items.py              # Item definitions
│   ├── pipelines.py          # Data pipelines
│   ├── middlewares.py        # Custom middlewares
│   ├── settings.py           # Scrapy settings
│   ├── stock_notification.py # SMS notification script
│   └── migrations/           # Database migrations (future)
├── .github/                   # GitHub configuration
│   ├── workflows/            # GitHub Actions workflows
│   │   ├── python-app.yml   # Main CI/CD workflow
│   │   └── scraper-test.yml # Scraper test workflow
│   └── dependabot.yml        # Dependabot configuration
├── Dockerfile                # Container image definition
├── docker-compose.yml        # Multi-container orchestration
├── scrapy.cfg                # Scrapy project config
├── requirements.txt          # Python dependencies
├── README.md                 # Main project README
└── LICENSE                   # MIT License
```

## Quick Links

### For Getting Started
1. Read [README.md](../README.md) for project overview
2. Follow installation steps in main README
3. Use [QUICKSTART.md](QUICKSTART.md) for common commands

### For Docker Setup
- Read [DOCKER.md](DOCKER.md) for comprehensive Docker guide
- Use `docker-compose up` for quick local setup

### For Development
- Check [IMPROVEMENTS.md](IMPROVEMENTS.md) for recent changes
- Review CI/CD in `.github/workflows/`
- Check Dependabot configuration in `.github/dependabot.yml`

### For Testing
- Example test data: `tests/example-data.json`
- Test output: `tests/test.json`

## Configuration

Environment variables are configured via:
- `.env` file (git-ignored, for local development)
- `.env.docker` (for Docker deployments) - see `config/`
- `.env.example` (template) - see `config/`

## CI/CD & Automation

### GitHub Actions
- **Main workflow**: `.github/workflows/python-app.yml`
  - Lint, Security, Test, Build jobs
  - Tests Python 3.11, 3.12, 3.13
  - Tests MongoDB 6.0, 7.0, 8.0

- **Scraper test**: `.github/workflows/scraper-test.yml`
  - Dedicated scraper testing workflow

### Dependabot
- Configured in `.github/dependabot.yml`
- Monitors: pip, github-actions, docker
- Creates weekly update PRs

## Support & Troubleshooting

See the **Troubleshooting** section in [README.md](../README.md#troubleshooting) for common issues.

For detailed documentation on specific features:
- **Docker deployment**: See [DOCKER.md](DOCKER.md)
- **Quick commands**: See [QUICKSTART.md](QUICKSTART.md)
- **Code improvements**: See [IMPROVEMENTS.md](IMPROVEMENTS.md)
