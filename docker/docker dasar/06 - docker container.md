# docker container
- docker container => aplikasi hasil installernya
  - satu docker image bisa digunakan untuk beberapa docker container
  - asalkan nama docker containernya berbeda (ex: redis1, redis2)
    - jika kita sudah membuat docker container, maka docker image yang digunakan tidak bisa dihapus
  - jika ingin hapus docker container maka harus hapus docker container terlebih dahulu

- status container
  - setalah kita membuat container kita perlu menajalnkan containernya
  - jika tidak containernya tidak akan bisa berjalan

## command
```bash
docker container ls -a # semua container
docker container ls # hanya container yang sedang berjalan
```

## membuat container
```bash
docker container create --name namacontainer namaimage:tag

docker container create --name redis-app redis:latest # membuat container
```

## menjalankan docker container
```bash
docker container start containerID
docker container start nama-container
```

## menghentikan docker container
```bash
docker container stop nama-container
```

## menghapus docker container
```bash
docker container rm nama-container
```