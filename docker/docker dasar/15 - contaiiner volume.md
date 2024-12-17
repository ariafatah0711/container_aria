## container volume
- container volume => volume yang kita buat tidak akan hilang jika container dihapus

## command
```bash
--mount "type=volume,source=namavolume,destination/folder/path"

# type=volume
# source=namavolume
```

## contoh
```bash
docker volume create nginx

docker container --name nginx-volume -p 8085:80 --mount "type=volume,source=nginx,destination=/usr/share/nginx/html" nginx:latest

docker container start nginx-volume
# lalu ubah isi file webnya di /usr/share/nginx/html
docker container stop nginx-volume
docker container rm nginx-volume
# setelah dihapus maka hanya containernya saja yang dihapus tapi data web kita masih ada di volume yang sebelumnya
```