# digital ocean
- salah satu cloud provide yang populer, dan memiliki fitur docker registry bernama contaienr registry
  - free version untuk ukuran 500mb
  - berbeda dengan docker hub kita tidak perlu login untuk melakukan push
  - kita hanya perlu menggunakan docker config untuk mengirim image ke digital ocean container registy

## docker push
- ubah nama file docker-config.json menjadi config.json
- .docker/config.json
  ```bash
  docker --config .docker push <image> #ingat nama folder bukan nama config.json
  # dan nama imagenya harus nama image repository digital ocean bukan nama user/image

  docker tag web-server registry.digitalocean.com/web-server
  docker --config .docker-digital.ocean push registry.digitalocean.com/web-server
  ```

## docker pull
```bash
docker --config .docker-digital.ocean pull registry.digitalocean.com/web-server
```