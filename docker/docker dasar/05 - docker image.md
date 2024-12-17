# docker image
- docker image => terdapat aplikasi dan dependency
  - sebelum kita bisa menjalankan aplikasi di docker, kita perlu memastikan memiliki docker image

## list docker image
```bash
docker iamge ls

┌─[ariafatah@aria-ubuntu]─[~]
└──╼ ❯❯❯ docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
localstack/localstack       latest    cd5422922d61   2 days ago      1.1GB
```

## donwoald docker image 
  - tag itu versinya (jika tidak pakai akan menggunakan versi latest(terbaru))
    ```bash
    docker image pull namaimage:tag

    docker image pull redis:latest
    ```
  - hapus docker image
    ```bash
    docker image rm namaitem:tag
    ```