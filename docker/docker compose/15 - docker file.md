# docker file
- docker file => membuat container dari docker file yang kita buat
  - hal ini mempermudahkan kita sehingga tidak membuat image nya terlebih dahulu secara manual

- build
  - ketika kita ingin membuat container dari dockerfile kita tidak menggunakan attribute image lagi di service nya
  - kita harus menggunakan attribute build, dimana terdapat attribute
    - context: berisi path ke file dockerfile
    - dockerfile: nama file dockerfile, bisa diganti jika mau
    - args: argument yang dibutuhkan ketika melakukan docker build

- image name
  - secara default docker compose akan membuat image dengan nama random ketika melakukan build dockerfile
  - jika kita ingin menentukan namanya kita bisa tambahkan attribute image pada servicenya
    - secara otomatis docker compose akan membuat image dengan nama sesuai dengan itu

## syntax
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

- build dockerfile
  - ketika kita menggunakan perintah docker compose start
  - secara otomatis docker compose akan malkukan build terlebih dahulu jika imagenya belum dibuat
  - tapi jika kita hanya ingin melakukan build image saja, tanpa membuat container, kita juga bisa menggunakan perintah docker compose build
  ```bash
  docker compose build
  ```

- menghapus image
  - hasil image dari docker compose tidak akan dihapus ketika melkaukan perintah docker compose down
  - jadi untuk menghapus kita harus hapus manual menggunakan perintah docker image rm nama-image:tag
  ```bash
  docker image rm nama_image
  ```

- build ulang => ketika kita mengubah kode progam
  - lalu kita coba stop dan start ulang container menggunakan docker compose, 
    - bukan berarti code progam terbaru akan berjalan
  - hal ini karena image versi baru otomatis terbuat,
    - sehingga jika kita ingin menggunakan docker image versi baru
    - kita harus hapus dulu containernya, lalu buat ulang dengan image baru