FROM golang:1.18-alpine

ARG APP="main-app"

WORKDIR /app
COPY main.go .
RUN mv main.go ${APP}.go

EXPOSE 8080

ENV APP-ENV=${APP}
CMD ["go", "run", "/app/${APP-ENV}.go"]
