# volume instruction
- volume => merupakan intruksi yang digunakan untuk membuat volume secara otomatis ketika membuat docker container
  - semua file yang terdapat di volume secara otomatis akan otomatis di copy ke dalam docker volume
    - walaupun kita tidak membuat docker volume ketika membuat docker containernya
    - ini sangat cocok pada kasus ketika aplikasi kita misal menyimpan data di dalam file sehingga data bisa secara otomatis aman berada di docker volume

## volume
```js
VOLUME /path/to/path
VOLUME  /path/folder1 /path/folder2
VOLUME ["/path/A", "/path/b", "/etc/nginx"]
```

## contoh
```bash
FROM golang:1.18-alpine

ENV APP_PORT=8080
ENV APP_DATA=/logs

RUN mkdir ${APP_DATA}
RUN mkdir app
COPY main.go app

EXPOSE ${APP_PORT}
VOLUME ${APP_DATA}

CMD go run app/main.go
```

## main.go
```go
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	port := os.Getenv("APP_PORT")
	fmt.Println("Run app in port : " + port)
	http.HandleFunc("/", HelloServer)
	http.ListenAndServe(":"+port, nil)
}

func HelloServer(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, %s", r.URL.Path[1:])

	dataString := "Hello " + r.URL.Path[1:]
	dataBytes := []byte(dataString)

	destination := os.Getenv("APP_DATA")
	file := destination + "/" + r.URL.Path[1:] + ".txt"
	err := ioutil.WriteFile(file, dataBytes, 0666)
	if err != nil {
		panic(err)
	}
	fmt.Println("DONE Write File : " + file)
}
```

## run
```bash
docker container create --name volume -e APP_PORT=8080 -p 8080:8080 aria/volume
docker start volume
# go to http://localhost:8080/aria

# and see the logs
docker logs volume
```