# restart
- restart
  - secara default, saat container mati, maka docker tidak akan menjalankan lagi containernya
    - kita harus menjalankan lagi containernya secara manual
  - kita bisa memaksa sebuah contaienr untuk selalu melakukan restart jika misal terjadi masalah pada contaienr
    - kita bisa tambahkan attribute restart, dengan beberapa value

## syntax
```yaml
restart: <option>

# option
no #default nya tidak pernah restart
always # selalu restart jika container berhenti
on-failure # restart jika container error dengan indikasi error ketike exit
unless-stopped # selalu restart container ketika dihentikan manual
```

## example
```yaml
version: "3.18"

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
      - net-mongo-restart
  mongodb-express-web:
    container_name: mongodb-express-web
    image: mongo-express
    ports:
      - "8081:8081"
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: ariafatah
      ME_CONFIG_MONGODB_ADMINPASSWORD: ariafatah
      ME_CONFIG_MONGODB_SERVER: mongodb-server
    networks:
      - net-mongo-restart
    depends_on:
      - mongodb-server
    restart: always

networks:
  net-mongo-restart:
    name: net-mongo-restart
    driver: bridge
```