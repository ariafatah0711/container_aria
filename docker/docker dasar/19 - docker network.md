# docker network
- docker network => membuat jaringan di dalam docker
  - saat kita membuatt container di docker
    - secara default container akan saling terisolasi satu sama lain, jadi jika kita mencoba memanggil antar container
    - bisa dipastikan bahwa kita tidak akan bisa melakukanya
  - dengan menggunakan network
    - kita bisa mengoneksikan container dengan container lain dalam satu network yang sama
  - jika beberapa container terdapat pada satu network yang sama
    - maka secara otomatis coontainer tersebut bisa saling berkomunikasi

- network driver => type network yang nanti akan digunakan
  - bridge => membuat network secara virtual yang memungkinkan container
    - yang terkoneksi di bridge network yang sama saling berkomunikasi
  - host => membuat nerwork yang sama dengan sistem host
    - host hanya jalan di docker linux
  - none (default) => tidak bisa berkomunikasi

## perintah
```bash
docker netwrok ls #melihat list network

docker network create -driver bridge jakarta #membuat network type bridge bernama jakarta
# -d / --driver

docker network rm jakarta #menghapus network docker yang sudah tidak digunakan
# dan pastikan hapus container yang sudahh tidak menggunakan networknya
```