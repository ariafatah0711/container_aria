# health check instruction
- health check => intruksi yang digunakan untuk memberi tahu docker bagaimana mengecek apakah container berjalan baik atau tidak
 - scr otomatis container akan memili status health
    - awal = starting
    - success = healty
    - gagal = unhealty

## health check
```bash
HEALTHCHECK NONE # default (tidak ada pengecekan)
HEALTCHECK [OPTION] CMD command # pengecekan sesuai perintah CMD disini
# OPTIONS
# --interval=DURATION (default 30s)
# --timeout=DURATION (default 30s)
# --start-period=DURATION (default 0s)
# retries=N (default 3)
```

## contoh
```bash
FROM golang:1.18-alpine

RUN apk add curl
RUN mkdir app
COPY main.go app

EXPOSE 8080

HEALTHCHECK --interval=5s --start-period=5s CMD curl -f http://localhost:8080/health
CMD go run app/main.go
```

## run
```bash
docker container ls
docker container inspect <nama_container>
```