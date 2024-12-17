# working directory
- working directory => intruksi untuk menentukan direktori / folder untuk menjalankan intruksi
  - RUN, CMD, ENTRYPOINT, COPY, ADD
  - jika workdir tidak ada, secara otomatis direktorinya akan dibuat secara otomatis direktorinya akan dibuat
    - dan selanjutnya setelah kita tentukan lokasi workdir nya
    - direktori tersebut akan dijadikan tempat menjalankan intruksi selanjutnya
  - workdir juga bisa digunakan sebagai path untuk lokasi pertama ketika kita masuk ke dalam docker container

## workdir
```bash
WORKDIR /app # artinya working directorynya adalah /app
WORKDIR docker # (relative) artinya sekarang working directornya adalah /app/docker

WORKDIR /home/app # (absolute path) /home/app
```

## contoh
```bash
FROM golang:1.18-alpine

WORKDIR /app
COPY main.go /app

EXPOSE 8080
CMD go run main.go # sudah tidak perlu pergi ke /app
```