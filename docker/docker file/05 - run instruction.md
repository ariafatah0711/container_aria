# run instruction
- run instruction => sebuah instruksi unuk mengeksekusi perintah di dalam image pada saat build state
    - hasil perintah RUN akan di commit dalam perubahan image tersebut
    - jadi perintah RUN akan diekseukusi pada saatt proses docker build saja
    - setealh menjadi docker image, perintah tersebut tidak akan di jalankan lagi

## run
```bash
FROM alpine:3

RUN command
RUN ["executable", "argument", "..."]
```

## Dockerfile
```bash
FROM alpine:3

RUN mkdir hello
RUN echo "hello WOrld" > "hello/world.txt"
RUN cat "hello/world.txt"
```