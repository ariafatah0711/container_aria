# resource limit
- resource limit> => kita bisa menggunakan file konfigurasi docker compose untuk mengatur resource limit
  - untuk CPU dan memory tiap container yang akan kita buat
  - kita bisa menggunakana ttribute deploy
    - lalu didalamnya menggunakan attribute resource
  - reservation adalah resource yang dijamin bisa digunakan oleh container
  - limit adalah maksimal untuk resource yang diberikan ke container 
    - namun ingat bisa saja limit ini rebutan dengan container lain

## syntax
```yaml
deploy:
    resources:
        reservations:
            cpus: "0.25"
            memory: 50M
        limits:
            cpus: "0.5"
            memory: 100M
```

## melihat cpu, memory dan limit
```bash
docker container stats
```