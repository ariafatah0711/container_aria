# entrypoint
- entry point => intruksi untuk menentukan excutable fie yang akan dijalankan oleh container
  - biasanya entrypoint itu erat dengan intruksi CMD
  - saat kita membuat intruksi CMD tanpa excutable file, scr otomatis CMD akan menggunakan ENTRYPOINT

## ENTRYPOINT
```js
ENTRYPOINT ["excutable", "param1", "param2"]
ENTRYPOINT [excutable param1 param2]s
// saat gunain CMD [param1, param2] => param tersebut akan dikirim ke ENTRYPOINT
```

## contoh
```js
FROM golang:1.18-alpine

RUN mkdir /app
COPY main.go /app

EXPOSE 8080

ENTRYPOINT [ "go", "run" ]
CMD ["/app/main.go"]
```

- run
```bash
docker image inspect
```