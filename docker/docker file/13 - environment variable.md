# env variable
- environment variable instruction => merupakan instruksi yang digunakan untuk mengubah environment variable
  - baik ketika tahapan build atau ketika jalan dalam docker container
  - ENV yang sudah ddi definisikan di dalam Dockerfile bisa digunakan kembali dengan menggunakan sintaks ${NAMA_ENV}
  - environment variable yang dibuat menggunakan instruksi ENV disimpan di dalam docker image 
    - dan bisa dilihat menggunakan perintah docker image inspect
  - selain itu, env var juga bisa diganti nilainya ketika pembuatan docker container
    - dengan perintah "docker contaienr create --env key=value" atau -e key=value

## env
```bash
ENV key=value
ENV key1=value1 key2=value2
```

## contoh
```bash
FROM golang:1.18-alpine

ENV APP_PORT=8080

RUN mkdir app
COPY main.go app/

EXPOSE ${APP_PORT}

CMD go run app/main.go
```

## main.go
```go
package main

import (
    "fmt"
    "net/http"
    "os"
)

func main() {
    port := os.Getenv("APP_PORT")
    fmt.Println("Run app in port : " + port)
    http.HandleFunc("/", HelloServer)
    http.ListenAndServe(":" + port, nil)
}

func HelloServer(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, World!")
}
```