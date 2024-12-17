# from instruction
- from instruction => FROM digunakan untuk membuat build stage dari image yang kita tentukan
  - biasanya jarang sekali kita akan membuat docker image dari scatch (kosongan).
  - biasanya kita akan membuat docker image dari Docker image lain yang sudah ada

- jika dari awal kita bisa gunakan linux seperti ubuntu
- jika dari kosong kita bisa gunakan scracth

## syntax
```bash
FROM image:version
```

## Dockerfile
```bash
FROM alpine:3
# alpine adalah linus ringan pada docker
```

## build
```bash
mkdir app && cd app
nano Dockerfile
***
isi Dockerfile
***

cd ..
docker build -t ariafatah/app:1.0.1 app 

docker image ls
```

## run
```bash
FROM alpine:3

RUN command
RUN ["executable", "argument", ""]
```