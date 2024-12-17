# backup volume
- backup volume => memanfaatkan container untuk melakukan backup data yang ada di dalam volume ke dalam archive seperti zip atau tar.gz

- tahapan melakukan backup
  - matikan container yang menggunakan volume yang ingin kita backup
  - buat container baru dengan dua mount
    - volume yang ingin kita backup,
    - bind mount folder dari sistem host
  - lakukan backup menggunakan container dengan cara meng archive isi volume dan simpan di bind moumt folder
  - isi file backup sekarang ada di folder sistem host
  - delete container yang ingin kita gunakan untuk melakukan backup

## contoh
```bash
docker container stop nginx-volume

mkdir -p /home/ariafatah/nginx/backup

docker container create --name nginxbackup \
--mount "type=bind,source=/home/ariafatah/nginx/backup,destination=/backup" \
--mount "type=volume,source=nginx,destination=/data"
nginx:latest

docker container start nginx-backup
docker exec -it nginx-backup bash

# /data => isinya adalah data dari volume mounting sebelumnya
# /backup => isinya masih kosong

tar cvf /backup/backup.tar.gz /data

# maka file backup sudah jadi

docker container stop nginx-backup
docker container rm nginx-backup
dockler container start nginx nginx
```