## create container
- membuat container => menggunakan configurasi file docker compose
  - pada file yaml, kita tambahkan bagian
    - services untuk menentukan containernya
  - dalam servicec tersebut, kita bisa tentukana container name dan image untuk docker container yang akan kita buat

## syntax
```yaml
version: "3.18"

services:
  nginx-aria: # harus uniqw
    container_name: nginx-aria # nama container
    image: nginx:latest # nama image:tag
```

## contoh
```yaml
version: "3.18"

services:
  nginx-aria:
    container_name: nginx-aria
    image: nginx:latest
```

- setelah konfigurasi file, container tidak langsung jadi kita harus membuatnya dengan menggunakan docker compose
  - dan jika ingin buat compose kita perlu masuk ke dalam folder nya terlebih dahulu
  ```bash
  cd pengenalan

  docker-compose create
  docker compose create
  ```