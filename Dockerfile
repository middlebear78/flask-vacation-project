# Stage 1: build the React frontend
FROM node:18-alpine AS frontend-build
WORKDIR /frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

# Stage 2: Flask API + built frontend served by gunicorn
FROM python:3.12-slim
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
# gunicorn: production WSGI server; cryptography: required by PyMySQL for
# MySQL 8's caching_sha2_password auth plugin
RUN pip install --no-cache-dir -r requirements.txt gunicorn==23.0.0 cryptography

COPY backend/ backend/
COPY --from=frontend-build /frontend/dist frontend/dist

EXPOSE 5000
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "backend.app:app"]
