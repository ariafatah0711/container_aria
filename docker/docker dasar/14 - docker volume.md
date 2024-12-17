# docker volume
- docker volume => mirip dengan bind mount, namun memiliki managemenet volume
  - dimana kita bisa membuat volume, melihat daftar volume, dan menghapus volume
  - volume sendiri bisa danggap storage yang digunakan untuk menyimpan data
    - bedanya dengan bind mounts, data disimpan pada sistem host
    - sedangkan pada volume, data di manage oleh docker

- melihat docker volume
  - saat kita membuat container, dimanakah data di dalam container itu disimpan,
    - secara default semua data container disimapan didalam volume
  - jika kita coba melihat docker volume, kita akan lihat bahwa ada banyak volume yang sudah terbuat
    - walaupun kita belum peprnah membuatnya sama sekali
  - command
    ```bash
    docker volume ls
    ```

## membuat volume
```bash
docker volume create namavolume
docker volume create nginx

docker volume inspect nginx
[
    {
        "CreatedAt": "2024-06-26T20:57:58+07:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/nginx/_data",
        "Name": "nginx",
        "Options": null,
        "Scope": "local"
    }
]
```

## menghapus volume
- untuk menghapus volume pastikan tidak ada yang sedang menggunakan volume tersebut
  ```bash
  docker volume rm namavolume
  ```