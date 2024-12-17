# docker container run
- docker container run =>  menjalankan container secara langsung
  - jadi menjalankan container tanpa harus membuat terlebih dahulu

## docker run
```bash
docker container run --rm --name ubuntu \
--mount "type=bind,source=/home/ariafatah/nginx/backup,destination=/backup" \
--mount "type=volume,source=nginx,destination=/data" \
ubuntu:latest tar cvf /backup/backup-2.tar.gz /data

# --rm => untuk meremove container secara otomatis stelah progam telah selesai digunakan
# ubuntu:latest => dan agar bisa behenti kita bisa gunakan image ubuntu
```