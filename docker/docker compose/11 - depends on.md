# depends
- depends on => urutan container
  - saat membuat file docker compose yang berisi banyak container
    - kadang kita membuat container yang butuh container lain sebelum berjalan
      - atau sederhananya kita ingin ada urutan contaienr berjalan
    - secara default, docker compose akan menjalankan semua container secara bersamaan,
      - tanpa ada urutan pasti
    - kita bisa membuat urutan menjalankan container dengan menggunakan attribute depends_on
    - kita bisa sebutkan pada container, bahwa container ini hanya bisa berjalan, 
      - kalo contaienr yang sudah berjalan
    - kita bisa sebutkan satu atau lebih container lainya pada attribute depends_on

## syntax
```yaml
services:
  mongodb-server: # ini
    image: mongo
  mongodb-express-web:
    container_name: mongodb-express-web
    image: mongo-express
    depends_on:
      - mongodb-server # id nya bukan name contianer
```

## contoh
```yaml
version: 3.9

services:
  mongodb-server:
    container_name: mongodb-server
    image: mongo
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: ariafatah
      MONGO_INITDB_ROOT_PASSWORD: ariafatah
      MONGO_INITDB_DATABASE: admin
    networks:
      - net-mongo
  mongodb-express-web:
    container_name: mongodb-express-web
    image: mongo-express
    port:
      - "8081:8081"
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: ariafatah
      ME_CONFIG_MONGODB_ADMINPASSWORD: ariafatah
      ME_CONFIG_MONGODB_SERVER: mongodb-server
    networks:
      - net-mongo
    depends_on:
      - mongodb-server

networks:
  nat-mongo:
    name: net-mongo
    driver: bridge
```