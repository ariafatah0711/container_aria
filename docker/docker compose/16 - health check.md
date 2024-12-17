# health check
- docker health check => secara default container yang dibuat, baik itu secara manual ataupun menggunakan docker compose
  - pasti akan selalu menggunakan health check yang dibuat di docker file
  - namun, jika kita ingin mengubah health check tersebut, itu juga bisa dilakukan
  - kita bisa ubah di file konfigurasi docker compose pada attribute healthcheck di service

## syntax
```yaml
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 1m30s
      timeout: 30s
      retries: 3
      start_period: 5s

health check
# test => berisikan cara melakukan test health check
# interval
# timeout
# retries => total retry
# start_period => waktu mulai
```

## contoh
```yaml
version: '3.8'

services:
  app:
    container_name: app
    build:
      context: ./app
      dockerfile: dockerfile
    image: "app-golang:2.0.0"
    environment:
      - "APP_PORT=8080"
    ports:
      - "8080:8080"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 1m30s
      timeout: 30s
      retries: 3
      start_period: 5s
```