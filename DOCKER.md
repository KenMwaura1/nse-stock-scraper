# Docker Deployment Guide

## Quick Start

### Option 1: Using docker-compose (Recommended)

```bash
# Clone and setup
git clone https://github.com/KenMwaura1/nse-stock-scraper.git
cd nse-stock-scraper

# Create environment file
cp .env.docker .env
# Edit .env with your credentials
nano .env

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f scraper
```

### Option 2: Manual Docker Commands

```bash
# Build image
docker build -t nse-scraper:latest .

# Run container with local MongoDB
docker run -d \
  --name nse-scraper \
  -e MONGODB_URI="mongodb://host.docker.internal:27017/" \
  -e MONGODB_DATABASE="nse_data" \
  -e at_username="your_username" \
  -e at_api_key="your_key" \
  -e mobile_number="your_number" \
  nse-scraper:latest

# View logs
docker logs -f nse-scraper
```

## Common Tasks

### Run Scraper with Debug Logging
```bash
docker-compose run --rm scraper crawl afx_scraper --loglevel=DEBUG
```

### Run Stock Notifications
```bash
docker-compose run --rm scraper python nse_scraper/stock_notification.py
```

### Access MongoDB
```bash
docker-compose exec mongodb mongosh
```

### View MongoDB Data
```bash
# Connect to MongoDB
docker-compose exec mongodb mongosh

# In the MongoDB shell:
use nse_data
db.stock_data.find().pretty()
```

### Stop All Services
```bash
docker-compose down

# Stop and remove volumes (careful - deletes data!)
docker-compose down -v
```

### Rebuild Images (after code changes)
```bash
docker-compose up --build
```

## Configuration

### Environment Variables

Edit `.env` file (or `.env.docker` for template):

```bash
# Africa's Talking SMS settings
at_username=your_africas_talking_username
at_api_key=your_africas_talking_api_key
mobile_number=+254XXXXXXXXX

# MongoDB settings
MONGODB_URI=mongodb://mongodb:27017/
MONGODB_DATABASE=nse_data
```

### Volume Management

**MongoDB Volumes:**
- `mongodb_data` - Database files (persistent)
- `mongodb_config` - Database configuration (persistent)

**Scraper Volumes:**
- `httpcache/` - HTTP response cache (mounted from host)

**View volumes:**
```bash
docker-compose config | grep volumes
docker volume ls
docker volume inspect nse-stock-scraper_mongodb_data
```

### Network

Services communicate via `nse_network` Docker bridge network:
- Scraper → MongoDB via `mongodb:27017`
- Container → Host via `host.docker.internal`

## Health Checks

### MongoDB Health
```bash
docker-compose exec mongodb mongosh --eval "db.adminCommand('ping')"
```

### Scraper Health
```bash
docker-compose exec scraper python -c "import pymongo; import os; pymongo.MongoClient(os.getenv('MONGODB_URI')).admin.command('ping')"
```

## Performance Tips

1. **First run**: Pulls images (~500MB), subsequent runs are faster
2. **Cache**: Docker layer caching speeds up rebuilds
3. **Volumes**: MongoDB data persists across container restarts
4. **Health checks**: Services wait for dependencies (MongoDB waits before scraper runs)

## Troubleshooting

### MongoDB won't start
```bash
# Check logs
docker-compose logs mongodb

# Reset MongoDB
docker-compose down -v
docker volume rm nse-stock-scraper_mongodb_data nse-stock-scraper_mongodb_config
docker-compose up
```

### Scraper can't connect to MongoDB
```bash
# Verify MongoDB is running
docker-compose ps

# Test connection
docker-compose run --rm scraper python -c "import pymongo; print(pymongo.MongoClient('mongodb://mongodb:27017').admin.command('ping'))"
```

### Port already in use
```bash
# MongoDB defaults to port 27017
# Change in docker-compose.yml:
# ports:
#   - "27018:27017"  # Use 27018 instead

# Find process using port
lsof -i :27017
```

### Out of disk space
```bash
# Clean up unused Docker resources
docker system prune -a
docker volume prune
```

## Production Deployment

### Using Environment Variables Instead of .env

```bash
docker-compose up \
  -e at_username="$AT_USERNAME" \
  -e at_api_key="$AT_API_KEY" \
  -e mobile_number="$MOBILE_NUMBER" \
  -e MONGODB_URI="$MONGODB_URI"
```

### Using External MongoDB

Modify `docker-compose.yml`:
```yaml
# Remove the mongodb service and set in .env:
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/
```

### Resource Limits

Add to `docker-compose.yml` service:
```yaml
services:
  scraper:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

### Logging

View logs from all services:
```bash
docker-compose logs

# Follow specific service
docker-compose logs -f scraper

# Last 100 lines
docker-compose logs --tail=100 scraper
```

## Docker Build Details

### Multi-stage Build
- **Builder stage**: Installs dependencies (smaller final image)
- **Final stage**: Includes only runtime requirements

### Security
- Non-root user (`scraper:1000`)
- Minimal base image (`python:3.11-slim`)
- Health checks enabled

### Image Size
- Base Python 3.11: ~150MB
- With dependencies: ~400MB
- Multi-stage optimization reduces size by ~40%

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [docker-compose Manual](https://docs.docker.com/compose/)
- [MongoDB Docker Hub](https://hub.docker.com/_/mongo)
- [Python Docker Best Practices](https://docs.docker.com/language/python/)
