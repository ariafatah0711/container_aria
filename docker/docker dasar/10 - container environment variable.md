# container env
- container env var => teknik konfigurasi agar aplikasi bisa diubah secara dinamis
  - dengan menggunakan ini kita bisa mengubah konfigurasi aplikasi tanpa harus mengubah kode aplikasinya lagi
  - docker container memiliki parameter yang bisa kita gunakan untuk mengirim environment variable ke aplikasi yang terdapat dalam container
  - kaya variable user passsword, dll

## env var
```bash
docker container create --name naamcontainer -env KEY="value" ---env KEY2="value" image:tag
# --env / -e => environment variable
```

- hub.docker/mongo db
- lalu cek environement nya
  ```yaml
  # Use root/example as user/password credentials
  version: '3.1'

  services:

    mongo:
      image: mongo
      restart: always
      environment:
        MONGO_INITDB_ROOT_USERNAME: root
        MONGO_INITDB_ROOT_PASSWORD: example

    mongo-express:
      image: mongo-express
      restart: always
      ports:
        - 8081:8081
      environment:
        ME_CONFIG_MONGODB_ADMINUSERNAME: root
        ME_CONFIG_MONGODB_ADMINPASSWORD: example
        ME_CONFIG_MONGODB_URL: mongodb://root:example@mongo:27017/
        ME_CONFIG_BASICAUTH: false
  ```

## contoh
```bash
docker container create --name mongodb-app --publish 27017:27017 --env MONGO_INITDB_ROOT_USERNAME=aria --env MONGO_INITDB_ROOT_PASSWORD:aria  mongo:latest
```