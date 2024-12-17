# container resource
- container resource limit => memberikan resource limit pada containernya
  - dengan ini kita bisa menjaga agar container tidak memakan banyak resource yang dapat menggagu container lain

- memory => menentukan jumlah memory
  ```bash
  # --memory <ukuran>
  # <ukuran> => b (bytes), k (kilo bytes), m (mega bytes), g (giga bytes),
  # misal --memory 100m => 100mb
  ```

- cpus
  ```bash
  # --cpus <ukuran>
  # <ukuran> => 1.5 (satu setengan cpu core)
  ```

## menambahkan resource limt
```bash
docker container create --name smallnginx --publish 8081:80 --memory 100m --cpus 0.5 nginx:latest

docker container start smallnginx

docker container stats
CONTAINER ID   NAME         CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O        PIDS
61453f7f015d   smallnginx   0.00%     3.125MiB / 100MiB     3.12%     15.9kB / 1.65kB   668kB / 12.3kB   3
15c77bfc9642   nginx-app    0.00%     3.801MiB / 3.018GiB   0.12%     39.5kB / 664B     1.41MB / 4.1kB   3
```