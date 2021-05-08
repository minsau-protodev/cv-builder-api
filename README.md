# cv-builder-api

Backend API for CV Builder project

# Setup

## Data Base - PostgreSQL

- Install Docker
- In root folder exec next command:
  ```bash
  docker-compose -f "docker/docker-compose.yml" up -d --build
  ```
- Connect using the next data:
  - Host: localhost
  - Port: 5432
  - User: cv-builder
  - Pass: cv-builder
  - DB: builder

## Server - Django

- Install dependencies (with poetry or pip)
  ```bash
  pip install -r requirements.txt
  ```
- Run migrations
  ```bash
  python manage.py migrate
  ```
