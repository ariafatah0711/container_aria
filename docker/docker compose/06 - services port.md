# services port
- services => container disimpan dalam konfigurasi file bernama servicecs
  - kita bisa menambahkan satu atau lebih services dalam konfigurasi filenya
- komentar => cukup tambahkan #
- port => kita bisa mengekspose port di container keluar menggunakan port forwading
  - kita bisa melakukan hal tersebut di konfigurasi file docker compose dengan menggunakan attributes port
    - short syntax => kita bisa gunakan syntax pendek yang berisi string 
      - ```HOST:CONTAINER``` misal ````8080:80```
    - long syntax => syntax panjang yang bisa kiat buat dalam bentuk object
      ```yaml
      target: <port didalam container>
      published: <port yang digunakan di host>
      protocol: <jenis port (TCP/UDP)>
      mode: <host untuk port di tiap node, atau ingress untuk swarm mode>
      # karena kita tidak menggunakan docker swarm. jadi kita cukup gunakan nilai host
      ```

## syntax
```yaml
version: "3.18"

services:
  nginx-aria-1:
    container_name: nginx-aria-1
    image: nginx
    ports:
      - target: 80
        published: 8081
        protocol: tcp
  nginx-aria-2:
    container_name: nginx-aria-2
    image: nginx
    ports:
      - "8082:80"
```