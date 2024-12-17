## bind mount
- bind mount
  - kita bisa gunakan attributes volumes di services
  - kita bisa tamabahkan satu atau lebih bind mount jika perlu

## short yntax
```yaml
SOURCE:TARGET:MODE

# SOURCE => lokasi di host (bisa gunakan relative path dengan diawali titik atau absolute path)
# TARGET => lokasi di container
# MODE => mode bind mount
    # ro (read only)
    # rw (read write) default

volumes:
    - "./data:/data/db"
```

## long syntax
- kita bisa gunakan dalam bentuk nested object di volumes dengan attribute
  ```yaml
  type: volume/bind # type mount, (volume/bind)
  source: ./data # target path di container
  target: /data/db # target path di container
  read_only: false # flag read only atau tidak defaultnya false

  volumes:
      - type: bind
        source: "./data-2"
        target: "/data/db"
        read_only: false
  ```

## contoh
```yaml
version: '3.8'

services:
  mongodb-aria:
    container_name: mongodb-aria
    image: mongo
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: ariafatah
      MONGO_INITDB_ROOT_PASSWORD: ariafatah
      MONGO_INITDB_DATABASE: admin
    volumes:
      - "./data:/data/db"
  mongodb-2:
    container_name: mongodb-2
    image: mongo
    ports:
      - "27018:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: admin
      MONGO_INITDB_DATABASE: admin
    volumes:
      - type: bind
        source: "./data-2"
        target: "/data/db"
        read_only: false
```