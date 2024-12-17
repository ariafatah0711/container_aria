# pengenalan
- sebelum menggunakan kubernetes
  - dari monolith ke microservices
    - monolith
      - saat kita membuat sebuah aplikasi dan semua fitur di buat dalam 1 aplikasi tersebut
    - microservices
      - aplikasi di pecah menjadi kecil
      - dimana tiap aplikasi hanya mengurus satu tugas dengan baik dan semua aplikasi dapat berkomunikasi
  - dari virtual mechine ke container

- kubernetes => aplikasi untuk automation development, scalling dan management aplikasi berbasis container
  - berawal dari google yang membuat internal system bernama borg, kemudian berganti menjadi omega, 
    - lalu di buatnya kubernetes dari pengalaman aplikasi tadi dan perkenalakna pada tahun 2014
  - sistem ini digunakan untuk membantu developer dan infra enginer untuk me manage ribuan server di google
  - dibuat dari bahasa pemograman golang

- alur kerja menggunakan kubernetes
  - configuration file yang digunakan untuk membuat config untuk mengatur cpu, node, atau aplikasi nanti yang akan digunakan
    - bisa beruapa json atau yml
  - nanti configurasinya kita upload ke kubernetes master
  - dan akan di jalankan di kubernetes workers