# volume
- volume => docker compose juga bisa digunakan untuk membuat volume
  - kita bisa gunakan attribute volume

## syntax
```yaml
volumes:
    mongo-data1:
        name: mongo-data-1
    mongo-data-2:
        name: mongo-data-2

services:
    mongodb-1:
```

- menggunakan volume kita bisa gunakan bind mount dengan ketentuan
  - pada short cyntax kita bisa ganti source dengan nama volume
  - dan long syntax menjadi nama volume

## syntax
```yaml
volumes:
    - "mongo-data-1:/data/db"

volumes:
    - type: volume
      source: mongo-data2
      target: "/data/db"
      read_only: false
```

## contoh
```yaml
version: '3.8'

services:
  mongodb-1:
    container_name: mongodb-1
    image: mongo
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: ariafatah
      MONGO_INITDB_ROOT_PASSWORD: ariafatah
      MONGO_INITDB_DATABASE: admin
    volumes:
      - "mongo-data-1:/data/db"
  mongodb-2:
    container_name: mongodb-2
    image: mongo
    ports:
      - "27018:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: ariafatah
      MONGO_INITDB_ROOT_PASSWORD: ariafatah
      MONGO_INITDB_DATABASE: admin
    volumes:
      - type: volume
        source: mongo-data-2
        target: "/data/db"
        read_only: false

volumes:
  mongo-data-1:
    name: mongo-data-1
  mongo-data-2:
    name: mongo-data-2
```

- menghapus volume
  - saat kita menggunakan perintah docker compose down yang hanya dihapus hanyalah container dan network saja
  - volume tidak akan dihapus hal ini agar jangan samapi kita tidak sengaja menghapus volume
  - jika kita ingin menghapus volume kita bisa lakukan manual dengan perintah docker volume rm nama_volume