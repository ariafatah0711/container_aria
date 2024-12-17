# run container
- menjalankan container => menggunakan docker compose untuk menjalankan container semuanya
  - deengan ini dia akan membaca konfigurasi yaml dan akan menjalankanya
- melihat contianer => melihat container yang hanya ada pada configurasi filenya
- menghentikan container
- menghapus container => dan akan menghapus network, dan volume juga
  - dan dia dapat menghapus keetika container masih berjalan

## syntax
```bash
docker compose start
docker-compose start

docker compose ps
docker-compose ps

docker compose stop
docker-compose stop

docker compose down # network, container, volume akan dihapus
docker-compose down
```

- project name => secara default nama project adalah nama folder lokasi file docker-compose.yaml
  - untuk melihat daftar project yang sedang berjalan, kita bisa menggunakan perintah

## syntax
```bash
docker compose ls
docker-compose ls
````