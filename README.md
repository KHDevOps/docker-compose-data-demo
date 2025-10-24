# Docker Compose Data Pipeline

Simple ETL data pipeline using Docker Compose that fetches random user data and loads it into PostgreSQL.

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

## Data Pipeline

1. **Extract**: Fetches 50 random users from `https://randomuser.me/api/`
2. **Transform**: Cleans and structures the data (name, email, location, age, etc.)
3. **Load**: Inserts data into PostgreSQL `random_users` table

## Cleanup

```bash
docker-compose down -v
```