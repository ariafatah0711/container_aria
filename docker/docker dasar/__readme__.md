# docker dasar
```bash
docker --version
```

# image
```bash
docker iamge ls # show docker image

docker image pull redis:latest # pull docker image
docker image rm redis:latest # remove docker image
```

# container
```bash
docker container ls -a # semua container
docker container ls # hanya container yang sedang berjalan

docker container create --name redis-app redis:latest # membuat container

docker container start redis-app # start container with name container
docker container start 7b4c0acad15d # with container ID

docker container stop redis-app # stop container

docker container rm redis-app # menghapus container
```

# container logs
```bash
docker container logs redis-app # logs yang terjadi
docker container logs -f redis-app # logs secara realtime
```

# container exec
```bash
docker container exec -i -t redis-app /bin/bash

root@7b4c0acad15d:/# redis-cli 

127.0.0.1:6379> set name "aria"
OK
127.0.0.1:6379> get name
"aria"
127.0.0.1:6379>
```

# docker port forwading
```bash
docker container create --name nginx-app -p 8080:80 nginx:latest
docker container start nginx-app

docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
15c77bfc9642   nginx:latest   "/docker-entrypoint.…"   16 seconds ago   Up 3 seconds    0.0.0.0:5001->80/tcp, :::5001->80/tcp   nginx-app
```

# docker env
```bash
docker container create --name mongodb-app --publish 27017:27017 --env MONGO_INITDB_ROOT_USERNAME=aria --env MONGO_INITDB_ROOT_PASSWORD:aria  mongo:latest

# untuk mengubah variable user dan password login
```

# container stats
```bash
docker container stats

CONTAINER ID   NAME        CPU %     MEM USAGE / LIMIT     MEM %     NET I/O       BLOCK I/O        PIDS
15c77bfc9642   nginx-app   0.00%     3.789MiB / 3.018GiB   0.12%     14.7kB / 0B   1.41MB / 4.1kB   3
7b4c0acad15d   redis-app   0.26%     10.17MiB / 3.018GiB   0.33%     14.4kB / 0B   7.63MB / 0B      6
```

# container resource limit
```bash
docker container create --name smallnginx --publish 8081:80 --memory 100m --cpus 0.5 nginx:latest

docker container start smallnginx

docker container stats
CONTAINER ID   NAME         CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O        PIDS
61453f7f015d   smallnginx   0.00%     3.125MiB / 100MiB     3.12%     15.9kB / 1.65kB   668kB / 12.3kB   3
15c77bfc9642   nginx-app    0.00%     3.801MiB / 3.018GiB   0.12%     39.5kB / 664B     1.41MB / 4.1kB   3
```

# bind mounts
```bash
docker container create --name mongodb-app --mount "type=bind,source=./mongodb,destination=/data/db" --publish 5002:8081 /
-e ME_CONFIG_MONGODB_ADMINUSERNAME=aria -e ME_CONFIG_MONGODB_ADMINPASSWORD=aria mongo:latest

docker container create --name nginx-linktree -p 8082:80 --mount "type=bind,source=/home/ariafatah/nginx,destination=/usr/share/nginx/html" nginx:latest

# --mount => parameter untuk mounting nya

# type => mount, bind / volumee
# source => lokasi file/atau folder sistem host
# destination => lokasi file / folder di dalam container
# read only (opsional) => jika ada maka fie/folder hanya bisa dibaca di container tidak bisa ditulis
```

# docker volume
```bash
docker volume create nginx

docker container --name nginx-volume -p 8085:80 --mount "type=volume,source=nginx,destination=/usr/share/nginx/html" nginx:latest 

docker container start nginx-volume
# lalu ubah isi file webnya di /usr/share/nginx/html
docker container stop nginx-volume
docker container rm nginx-volume
# setelah dihapus maka hanya containernya saja yang dihapus tapi data web kita masih ada di volume yang sebelumnya
```

# docker run
- backup
  ```bash
  docker container run --rm --name ubuntu \
  --mount "type=bind,source=/home/ariafatah/nginx/backup,destination=/backup" \
  --mount "type=volume,source=nginx,destination=/data" \
  ubuntu:latest tar cvf /backup/backup-2.tar.gz /data

  # --rm => untuk meremove container secara otomatis stelah progam telah selesai digunakan
  # ubuntu:latest => dan agar bisa behenti kita bisa gunakan image ubuntu

  # lalu setelah nama image kita bisa tambahkan perintah yang akan dijalankan itu
  ```
- restore volume
  ```bash
  docker volume create nginx-data

  docker container run --rm --name ubuntu \
  --mount "type=bind,source=/home/ariafatah/nginx/backup,destination=/backup"
  --mount "type=volume,source=nginx,destination=/data" ubuntu:latest \
  bash -c "cd /data && tar xvf /backup/backup-2.tar.gz --strip 1"

  docker container create --name nginx-restore -p 8082:80 --mount "type=volume,source=nginx-data,destination=/usr/share/nginx/html"

  docker container start nginx-data
  ```

# docker network
```bash
docker netwrok ls #melihat list network

docker network create -driver bridge jakarta #membuat network type bridge bernama jakarta
# -d / --driver

docker network rm jakarta #menghapus network docker yang sudah tidak digunakan
# dan pastikan hapus container yang sudahh tidak menggunakan networknya

docker network connect mongo-net mongodb
# menambahkan network pada container mongodb

docker network disconnect mongo-net mongodb
# menghapus network mongo-net pada container mongodb
```

## make container with docker network
```bash
docker network create -d bridge mongo-net

docker container create --name mongodb --network mongo-net \
-e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=admin mongo:latest

docker image pull mongo-express

docker container create --name mongodb-express --network mongo-net -p 8081:8081 \
-e ME_CONFIG_MONGODB_URL=mongodb://admin:admin@mongodb:27017 mongo-express:latest

# mongodb://root:admin@mongo:27017
# root => user, admin => pass
# @mongodb => nama container, :27017 => port_container

docker container start mongodb mongodb-express

# go to http://localhost:8081

user: admin
pass: pass
```

# inspect => melihat detail
```bash
docker image inspect nama_image
docker container inspect nama_container
docker volume inspect nama_volume
docker network inspect nama_network
```

# prune => menghapus yang tidak dipakai
```bash
docker image prune
docker container prune
docker volume prune
docker netowrk prune

docker system prune # container, network, image
```