# docker build
- docker build => perintah yang digunakan untuk membuat docker image
  - saat membuat docker image dengan docker build
    - nama image secara otomatis akan dibuat random, 
  - jika ingin menambahkan nama/tag pada imagenya, 
    - kita bisa mengubahnya dengan menambahkan perintah -t

## command
```bash
docker build -t ariafatah/app:1.0.0 folder-dockerfile
docker build -t ariafatah/app:1.0.0 -t ariafatah/app:latest folder-dockerfile

# ariafatah/app => nama-image
# 1.0.0 => tag
# folder-dockerfile => file / folder docker file

# :latest => ini agar tag latest bakal terupdate yang baru gitu
```