# bind mount
- bind mounts =mounting (sharing) file atau folder yang terdapat di sistem host ke container yang terdapat di docker
  - ini berguna ketika misal kita ingin mengirim konfigurasi dari luar container.
  - atau misal menyimpan data yang dibuat aplikadi di dalam container ke dalam folder sistem host

- jika file / folder tidak ada di sistem host, secara otomatis akan dibuatkan oleh docker

## bind mount
```bash
docker container create --name namacontainer --mount "type=bind,source=/folder/path,destination=/folder/pathcontainer,readonly" image:tag

# --mount => parameter untuk mounting nya

# type => mount, bind / volumee
# source => lokasi file/atau folder sistem host
# destination => lokasi file / folder di dalam container
# read only (opsional) => jika ada maka fie/folder hanya bisa dibaca di container tidak bisa ditulis
```

## contoh
```bash
docker container create --name mongodb-app --mount "type=bind,source=./mongodb,destination=/data/db" --publish 5002:8081 /
-e ME_CONFIG_MONGODB_ADMINUSERNAME=aria -e ME_CONFIG_MONGODB_ADMINPASSWORD=aria mongo:latest


docker container create --name nginx-linktree -p 8082:80 --mount "type=bind,source=/home/ariafatah/nginx,destination=/usr/share/nginx/html" nginx:latest
docker container start nginx-linktree

# open localhost:8080
# maka nanti web yang tampil adalah web file dari host kita yang berada di /home/ariafatah/nginx
```