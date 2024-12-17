# multi stage build
- multi stage build => dimana ddalam docker file, kita bisa membuat beberapa build stage atau tahapn build
  - kita bisa gunakan beberapa intruksi FROM
    - setiap intruksi FROM artinya adalah build stage
  - hal build stage terakhir adalah build stage yang akan dijadikan sebagai image
    - artinya kita bisa memanfaatkan docker build stage
    - untuk mealkukan kode progam golang kita lalu dipindahkan ke image selanjutnya

## builder
```bash
FROM golang:1.18-alpine as builder

FROM alpine:3
COPY --from=builder /app/main ./
```

## contoh
```bash
FROM golang:1.18-alpine as builder
WORKDIR /app
COPY main.go /app
RUN go build -o /app/main main.go

FROM alpine:3
WORKDIR /app
COPY --from=builder /app/main ./
CMD /app/main
```