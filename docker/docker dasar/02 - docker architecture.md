# docker architecture
- docker menggunakan arsitektur client-server
- docker client berkomunikasi dengan Docker daemon(server)
- docker client dan docker Daemon bisa berjalan di satu sistem yang sama
- docker menggunakan REST API

- ketika dia melakukan perintah docker 
  - dia akan mengirim perintahnya ke dalam docker Daemon
    - nanti docker daemon akan melakukan proses manage nya