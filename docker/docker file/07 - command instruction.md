# coommand instruction
- command instruction => instruksi yang digunakan ketika docker container berjalan
  - command tidak akan dijalankan ketika pada proses build
  - kita bisa menambahkan lebih dari satu container
    - tapi hanya instrucsion yang terakhir saja yang dapat dijalankan

## format
```js
CMD command param param
CMD ["executable", "param", "param"]
CMD ["param", "param"] => akan menggunakan executable ENTRY POINT. yang akan di bahasa di chapter terpisah
```

## run
```bash
docker build -t ariafatah/app-1 app-1
docker image inspect ariafatah/app-1

docker container create --name command ariafatah/app-1
docker container logs command
```