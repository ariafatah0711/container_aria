# network
- default network
  - saat kita menajalnkan file menggunakan docker compose
    - secara default semua container akan dihubungkan dalam sebuah network bernama nama-project_default
    - jadi sebenernya kita tidak perlu membuat network secara manual
  - silakan inspect container yang sudah berjalan menggunakan docker compose,
    - lalu lihat pada bagian network

- membuat network
  - kita bisa buat 1 network atau lebih

## syntax
```yaml
networks:
    network-harbas:
        name: network-harbas
        driver: bridge/host/none # type network 
```

## menggunakan network
  - setelah membuat network jika kita ingin menggunakan network tersebut
  - kita bisa menggunakan attribute networks, dan sebutkan satu atau lebih network yang ingin kita gunakan

## syntax
```yaml
mongodb-harbas:
    networks:
        - network-harbas
```