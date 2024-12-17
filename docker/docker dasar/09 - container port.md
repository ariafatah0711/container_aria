# port container
- container port => saat kita install aplikasi container docker tertentu maka aplikasi akan berjalan pada port tertentu
  - dan os host kita tidak bisa mengakses docker secara langsung

- port forwading => meneruskan sebuah port yang terdapat di sistem hostnya ke dalam docker container
  - dengan ini kita bisa mengakses container dari host

## command
```bash
docker container create --name container_name --publish porthost:portcontainer image:tag
# -p / --publish => bisa juga menggunakan 2 portcontainer
```

## contoh
```bash
docker container create --name nginx-app -p 8080:80 nginx:latest
docker container start nginx-app

docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
15c77bfc9642   nginx:latest   "/docker-entrypoint.…"   16 seconds ago   Up 3 seconds    0.0.0.0:5001->80/tcp, :::5001->80/tcp   nginx-app
```