# docker container stats
- docker container stats => melihatt detail resouce penggunaan dari tiap container
  - dengan ini kita bisa melihat container mana yang paling banyak memakan cpu / memory

## contaienr stats
```bash
docker container stats

CONTAINER ID   NAME        CPU %     MEM USAGE / LIMIT     MEM %     NET I/O       BLOCK I/O        PIDS
15c77bfc9642   nginx-app   0.00%     3.789MiB / 3.018GiB   0.12%     14.7kB / 0B   1.41MB / 4.1kB   3
7b4c0acad15d   redis-app   0.26%     10.17MiB / 3.018GiB   0.33%     14.4kB / 0B   7.63MB / 0B      6
```