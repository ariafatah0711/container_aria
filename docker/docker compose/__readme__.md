## docker compose
- docker compose => aplikasi yang digunakan untuk mendefiniskan dan menjalankan multiple Docker Container Secara sekaligus
  ```bash
  DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
  mkdir -p $DOCKER_CONFIG/cli-plugins
  curl -SL https://github.com/docker/compose/releases/download/v2.29.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose

  chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
  # or
  sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose

  docker compose version
  ```

## perintah compose
```bash
# docker-compose or docker compose

docker-compose up --force-recreate # create ulang / network yang error

docker-compose create # membuat container
docker-compose start # start container semua docker container yang di konfigurasi
docker-compose ps # list container yang ada pada file konfigurasi
docker-compose stop # stop container yang ada pada konfigurasi
docker-compose down # menghapus container, volume, network (meskipun sedang container berjalan)

docker-compose ls # list docker compose (list berdasarkan nama folder yang berisi docker-compose.yaml yang sudah dibuat)
docker-compose build # hanya melakukan build docker file / image

docker compose -f prod.yaml create
docker compose -f prod.yaml start
docker compose -f prod.yaml down

docker compose -f docker-compose.yaml -f prod.yaml create

docker events --filter 'container=nama' # melihat kejadian secara realtime
```

## konfigurasi
- konfigurasi docker-compose.yaml
  ```yaml
  version: "3.18"

  services:
    nginx-aria:
      container_name: nginx-aria
      image: nginx:latest
  ```

### port
- port => kita bisa mengekspose port di container keluar menggunakan port forwading
  - kita bisa melakukan hal tersebut di konfigurasi file docker compose dengan menggunakan attributes port
    - short syntax => kita bisa gunakan syntax pendek yang berisi string 
      - ```HOST:CONTAINER``` misal ```8080:80```
    - long syntax => syntax panjang yang bisa kiat buat dalam bentuk object
      ```yaml
      target: <port didalam container>
      published: <port yang digunakan di host>
      protocol: <jenis port (TCP/UDP)>
      mode: <host untuk port di tiap node, atau ingress untuk swarm mode>
      # karena kita tidak menggunakan docker swarm. jadi kita cukup gunakan nilai host
      ```

- contoh
  ```yaml
  # docker-compose.yaml
  version: "3.18"

  services:
    nginx-aria-1:
      container_name: nginx-aria-1
      image: nginx
      ports:
        - target: 80
          published: 8081
          protocol: tcp
    nginx-aria-2:
      container_name: nginx-aria-2
      image: nginx
      ports:
        - "8082:80"
  ```

### environment variable
```yaml
environment
    MONGO_INITDB_ROOT_USERNAME: ariafatah
    MONGO_INITDB_ROOT_PASSWORD: ariafatah
    MONGO_INITDB_DATABASE: 
```

### bind mount
- short yntax
  ```yaml
  SOURCE:TARGET:MODE

  # SOURCE => lokasi di host (bisa gunakan relative path dengan diawali titik atau absolute path)
  # TARGET => lokasi di container
  # MODE => mode bind mount
      # ro (read only)
      # rw (read write) default

  volumes:
      - "./data:/data/db"
  ```

- long syntax
  - kita bisa gunakan dalam bentuk nested object di volumes dengan attribute
    ```yaml
    type: volume/bind # type mount, (volume/bind)
    source: ./data # target path di container
    target: /data/db # target path di container
    read_only: false # flag read only atau tidak defaultnya false

    volumes:
        - type: bind
          source: "./data-2"
          target: "/data/db"
          read_only: false
    ```

## volume
```yaml
volumes:
    mongo-data1:
        name: mongo-data-1
    mongo-data-2:
        name: mongo-data-2

services:
    mongodb-1:
        volumes:
            - "mongo-data-1:/data/db"
    mongodb-2:
        volumes:
            - type: volume
                source: mongo-data-2
                target: "/data/db"
                read_only: false
```

## network
```yaml
networks:
    network-harbas:
        name: network-harbas
        driver: bridge/host/none # type network 
mongodb-harbas:
    networks:
        - network-harbas
```

## depends on
```yaml
services:
  mongodb-server: # ini
    image: mongo
  mongodb-express-web:
    container_name: mongodb-express-web
    image: mongo-express
    depends_on:
      - mongodb-server # id nya bukan name contianer
```

## restart
```yaml
restart: <option>

# option
no #default nya tidak pernah restart
always # selalu restart jika container berhenti
on-failure # restart jika container error dengan indikasi error ketike exit
unless-stopped # selalu restart container ketika dihentikan manual
```

## resource limit
```yaml
deploy:
    resources:
        reservations:
            cpus: "0.25"
            memory: 50M
        limits:
            cpus: "0.5"
            memory: 100M
```

- melihat cpu, memory dan limit
  ```bash
  docker container stats
  ```

- contoh
  ```yaml
  version: '3.8'

  services:
    nginx-aria-1:
      container_name: nginx-aria-1
      image: nginx
      ports:
        - target: 80
          published: 8081
          protocol: tcp
      deploy:
        resources:
            reservations:
                cpus: "0.25"
                memory: 50M
            limits:
                cpus: "0.5"
                memory: 100M
  ```

## docker file
```yaml
services:
  app:
    container_name: app
    build:
      context: ./app
      dockerfile: dockerfile
    image: "app-golang:1.0.0" # nama image 
    environment:
      - "APP_PORT=9000"
    ports:
      - "9000:9000"

# context => lokasi folder path berisi dockerfile
# dockerfil => nama dockerfile
# image => nama image hasil build
# args => argument untuk environment docker file
```

## health check
```yaml
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 1m30s
      timeout: 30s
      retries: 3
      start_period: 5s

health check
# test => berisikan cara melakukan test health check
# interval
# timeout
# retries => total retry
# start_period => waktu mulai
```

## extend service
```yaml
version: '3.9'

services:
  app:
    container_name: app
    build:
      context: "./app"
      dockerfile: Dockerfile
    image: "app-golang:3.0.0"
    environment:
      - "APP_PORT=8080"
      - "MODE=local"
    ports:
      - "8080:8080"
```

- contoh
  ```yaml
  # prod.yaml
  version: '3.9'

  services:
    app:
      environment:
        - "MODE=prod"
  ```