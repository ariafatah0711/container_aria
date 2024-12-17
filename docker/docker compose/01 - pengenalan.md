# pengenalan
- docker compose => aplikasi yang digunakan untuk mendefiniskan dan menjalankan multiple Docker Container Secara sekaligus 
  - dengan menggunakan docker compose, kita bisa menggunakan file YAML untuk melakukan konfigurasi docker container
  - lalu dengan sebuah perintah, kita bisa membuat semua docker container dan menjalankan sekaligus dari file konfigurasi tersebut
  - dengan begitu, kita tidak perlu lagi mengetikan perintah docker create seecara manual ketika ingin membuat docker container

# fitur docker container
- memiliki multiple isolated environment dalam satu docker host / server, atau dibilang project.
  - hal ini memungkinkan kita bisa membuat banyak sekali jenis environement untuk docker compos
  - hanya membuat container yang berubah. docker compose bisa mendeteksi container mana yang mana harus dibuat
    - dan tidak perlu dibuat ulang dari perubayan file konfigurasi

# kapan membuat docker compose
- membuat development environment => ketika kita develop aplikasi
  - kita sering butuh tool-tool berbeda untuk tiap projectnya
- automated testing => kadang ketika kita bisa membuat automation testing, banyak sekali hal yang harus kita jalankan secara manual
  - docker compose bisa membantu kita untuk otomatisi proses setup nya
- development

# menginstall docker compose
## install
```bash
docker-compose # docker compos versi dulu terpisah

docker compose # docker compose versi terbaru (tidak terpisah)
```