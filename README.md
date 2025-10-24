# Docker Compose Data Pipeline

Simple ETL data pipeline using Docker Compose that fetches random user data and loads it into PostgreSQL every 5 minutes.

## Prerequisites

- Docker & Docker Compose
- Python 3.8+ (for testing)

## Quick Start

### 1. Start Everything
```bash
docker-compose up
```

### 2. Connect to Database
```bash
docker-compose exec postgres psql -U postgres -d postgres
```

### 3. Query Data
```sql
SELECT COUNT(*) FROM random_users;
SELECT * FROM random_users LIMIT 5;
```

## Components

- **PostgreSQL**: Database to store user data
- **ETL App**: Python script that extracts data from RandomUser API, transforms it, and loads into PostgreSQL
- **CI/CD**: GitHub Actions automatically builds and pushes Docker image to Docker Hub

## Data Pipeline

The ETL pipeline runs automatically every 5 minutes:

1. **Extract**: Fetches 50 random users from `https://randomuser.me/api/`
2. **Transform**: Cleans and structures the data (name, email, location, age, etc.)
3. **Load**: Inserts data into PostgreSQL `random_users` table
4. **Wait**: Sleeps for 5 minutes before next run

Watch the logs to see real-time ETL execution:
```bash
docker-compose logs -f etl
```

## CI/CD Setup

1. **Add GitHub Secret**:
   - `DOCKER_HUB_TOKEN`: your Docker Hub access token

2. **Push to GitHub**: Auto-builds and pushes to `khdevops/etl-app:latest`

## Testing

Run the integration test to verify everything works:

```bash
cd tests/
pip install -r requirements.txt
pytest test_simple.py -v -s
```

The test will:
- Start docker-compose services
- Wait for PostgreSQL to be ready
- Verify data is being inserted
- Clean up services

## Cleanup

```bash
docker-compose down -v
```