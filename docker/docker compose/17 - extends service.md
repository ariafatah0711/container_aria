# extends service
- saat membuat aplikasi menggunakan docker, kadang kita inign menjalankan aplikasi tersebut ke beberapa server
  - baik itu local di laptop di server development atau server production
  - kadang ada kalanya beberapa hal berbeda misal konfigurasi
  - pada kasus ini mau tidak mau kita haarus membuat banyak file konfigurasi docker compose
    - misal untuk di local, di development dan di production

- extend service => kita melakukan merge beberapa konfigurasi file sekaligus
  - dengan bergitu kita bisa membuat file konfigurasi umum, dan spesial untuk setipa jenis environment misalnya
  - saat menjalankan docker compose, kita bisa gunakan perintah
    ```-f namafile.yaml``` jika ingin menggunakan nama file yang bukan docker-compose.yaml

## syntax
```yaml
# prod.yaml
version: '3.9'

services:
  app:
    environment:
      - "MODE=prod"
```

## run
```bash
docker compose -f prod.yaml create

docker compose -f docker-compose.yaml -f prod.yaml create
docker compose -f docker-compose.yaml -f dev.yaml create
```