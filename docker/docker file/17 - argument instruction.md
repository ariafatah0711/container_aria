# argument instruction
- argument instruction => merupakan intruksi yang digunakan untuk mendefinisikan variable yang bisa digunakan oleh pengguna untuk dikirim ketika melakukan proses docker build menggunakan perintah
  - --build-arg key=value
  - arg hanya digunakan pada saat proses build time
    - kalo env hanya berjalan di container
  - cara alses variable ARG sama seperti mengakses variable dari ENV
    - ${variable_name}

## argument
```bash
ARG key # argument variable
ARG key=defaultvalue # membuat argument variable dengan default value jika tidak di isi
```

## contoh
```bash
FROM golang:1.18-alpine

ARG APP="main-app"

WORKDIR /app
COPY main.go .
RUN mv main.go ${APP}.go

EXPOSE 8080

ENV APP-ENV=${APP}
CMD ["go", "run", "/app/${APP-ENV}.go"]
```

## run
```bash
docker build -t aria/arg --build-arg app=main-aria argument
```