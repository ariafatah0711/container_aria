# container exec
- container exec => mengeksekusi kode progam yang terdapat dalam containerya
  - ini bisa digunakan masuk ke container juga

## masuk container
```bash
docker container exec -i -t containerid/containername /bin/bash
# i => interaktif (menjaga input tetap aktif)
# t => TTY (terminal akses)
# /bin/bash => kode progam yang terdapat dalam container
```

## contoh
```bash
docker container exec -i -t redis-app /bin/bash

root@7b4c0acad15d:/# redis-cli 

127.0.0.1:6379> set name "aria"
OK
127.0.0.1:6379> get name
"aria"
127.0.0.1:6379>
```