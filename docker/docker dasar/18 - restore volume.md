# restore volume
- restore volume => melakukan restore data backup

- langkah langkah
  - buat volume baru untuk lokasi restore data backup
  - buat container baru dengan dua mount
    - volume baru untuk restore backup dan bind mount folder dari sistem host yang berisi file backup
  - lakukan restore menggunakan container
    - dengan cara meng extract isi backup file ke dalam volume
  - isi file backup sekarang sudah di restore ke volume
  - delete container yang kita gunakan untuk melakukan restore
  - volume baru yang berisi data backup siap digunakan oleh container baru

## contoh
```bash
docker volume create nginx-data

docker container run --rm --name ubuntu \
--mount "type=bind,source=/home/ariafatah/nginx/backup,destination=/backup"
--mount "type=volume,source=nginx,destination=/data" ubuntu:latest \
bash -c "cd /data && tar xvf /backup/backup-2.tar.gz --strip 1"

docker container create --name nginx-restore -p 8082:80 --mount "type=volume,source=nginx-data,destination=/usr/share/nginx/html"

docker container start nginx-data
```