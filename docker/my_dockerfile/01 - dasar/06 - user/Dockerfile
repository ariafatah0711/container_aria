FROM golang:1.18-alpine

WORKDIR /app

RUN addgroup -S harbas
RUN adduser -SDh /app ariafatah harbas
RUN chown -R ariafatah:harbas /app
USER ariafatah

COPY main.go /app/

EXPOSE 8080

CMD go run main.go