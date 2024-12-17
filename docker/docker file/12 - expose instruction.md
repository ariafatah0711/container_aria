# expose
- expose => intruksi untuk memberitahu bahwa container akan listen port pada nomer tertentu
  - instrukski EXPOSE tidak akan mempublish port apapaun sebenernya
  - hanya digunakan untuk dokumentasi / memberitahu
    - yang membuat container nya bahwa docker image akan menggunakan port tertentu

## expose
```bash
EXPOSE port #default tcp
EXPOSE port/tcp
EXPOSE port/udp
```

## contoh
```bash
FROM golang:1.18-alpine

RUN mkdir app
COPY main.go app

EXPOSE 8080

CMD go run app/main.go
```

## main go
- https://gist.github.com/khannedy/9262c7784a9ef65ced9dac712822a853
  ```go
  package main

  import (
      "fmt"
      "net/http"
  )

  func main() {
      http.HandleFunc("/", HelloServer)
      http.ListenAndServe(":8080", nil)
  }

  func HelloServer(w http.ResponseWriter, r *http.Request) {
      fmt.Fprintf(w, "Hello, World!")
  }
  ```