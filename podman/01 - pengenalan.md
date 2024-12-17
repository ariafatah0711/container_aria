# podman => alternatif docker
- perbedaan podman dan docker
  - docker
    - docker di manage dengan daemon
    - docker harus berjalan root mode
  - podman
    - podman berjalan tanpa harus ada daemon
    - podman menggunakan rootles mode
    - podman memiliki concept pod

## snytax dasar
```bash
podman --help
podman --version
man podman / man podman-<subcommand>

podman search <search_term>
podman search httpd --filter=is-official

podman pull docker.io/library/httpd

podman ps
podman ps -a

podman inspect -l # lattest
podman inspect <container/image/any>

podman logs -l
podman top -l

podman start
podman stop -l

podman rm -l
```

## run
```bash
podman run -dt -p 8080:80/tcp docker.io/library/httpd
# -d detached (berjalan di latar belakang)
# -t tty (terminal)
```

## image
```bash
podman images ls -a
```

## container
```bash
podman container ls -a
```

## checkpoint
```bash
sudo podman container checkpoint <container_id>
sudo podman container restore <container_id>
```

## migrate
- checkpoint
  ```bash
  sudo podman container checkpoint <container_id> -e /tmp/checkpoint.tar.gz
  scp /tmp/checkpoint.tar.gz <destination_system>:/tmp
  ```
- restore
  ```bash
  sudo podman container restore -i /tmp/checkpoint.tar.gz
  ```

## pod
```bash
podman pod -h
podman pod ps
podman pod create

podman run -dt --pod pod-1 nginx #tidak bisa menggunakan publish port

podman run -dt --pod new:ngix-pod --name nginx-1 -p 10081:80 nginx #new:nginx-pod membuat pobaru agar bisa publish port


podman generate kube <podid> > pod.yml
kubectl apply -f {script}.yml
```

## infra podman
```bash
82c0d1bc30f1  localhost/podman-pause:4.6.1-1692961697                        2 minutes ago   Up 37 seconds                        07f6b0c7ce91-infra
76815ad9e52a  docker.io/library/nginx:latest           nginx -g daemon o...  37 seconds ago  Up 37 seconds                        angry_leakey
```