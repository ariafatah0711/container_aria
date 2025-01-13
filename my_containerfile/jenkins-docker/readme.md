# run
```bash
docker network create jenkins

docker run \
  --name jenkins-docker \
  --detach \
  --privileged \
  --network jenkins \
  --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 2376:2376 \
  --publish 3000:3000 --publish 5000:5000 \
  --restart always \
  docker:dind \
  --storage-driver overlay2

# --name: Menentukan nama Docker container yang akan digunakan untuk menjalankan image.
# --detach: Menjalankan Docker container di background. Meski begitu, instance ini dapat dihentikan nanti dengan menjalankan perintah docker stop jenkins-docker.
# --privileged: Menjalankan dind (docker in docker alias docker di dalam docker) saat ini memerlukan privileged access (akses istimewa) agar bisa berfungsi dengan baik. Persyaratan ini bisa jadi tak diperlukan dengan versi kernel Linux terbaru.
# --network jenkins: Ini berhubungan dengan network yang dibuat pada langkah sebelumnya.
# --network-alias docker: Membuat Docker di dalam Docker container tersedia sebagai hostname docker di dalam jenkins network.
# --env DOCKER_TLS_CERTDIR=/certs: Mengaktifkan penggunaan TLS di Docker server. Ini direkomendasikan karena kita menggunakan privileged container. Environment variable ini mengontrol root directory di mana Docker TLS certificates dikelola.
# --volume jenkins-docker-certs:/certs/client: Memetakan direktori /certs/client di dalam container ke Docker volume bernama jenkins-docker-certs.
# --volume jenkins-data:/var/jenkins_home: Memetakan direktori /var/jenkins_home di dalam container ke Docker volume bernama jenkins-data. Ini akan memungkinkan Docker container lain dikelola oleh Docker container’s Docker daemon ini untuk mount data dari Jenkins.
# --publish 2376:2376: Mengekspos Docker daemon port pada mesin host (komputer Anda). Ini berguna untuk mengeksekusi Docker command (perintah Docker) pada mesin host (komputer Anda) dalam mengontrol inner Docker daemon.
# --publish 3000:3000 --publish 5000:5000: Mengekspos port 3000 dan 5000 dari dind (docker in docker) container
# --restart always: memastikan container restart dan tetap menyala tidak hanya saat ada kegagalan tetapi juga setelah server yang digunakan juga restart.
# docker:dind: Ini adalah image dari docker:dind itu sendiri. Image ini bisa diunduh sebelum dijalankan menggunakan perintah docker image pull docker:dind.
# --storage-driver overlay2: Storage driver untuk Docker volume. Lihat halaman "Docker Storage drivers” untuk berbagai opsi yang didukun

cat > Dockerfile << EOF
FROM jenkins/jenkins:2.426.2-jdk17
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean:1.27.9 docker-workflow:572.v950f58993843" 
EOF

docker build -t myjenkins-blueocean:2.426.2-1 .

docker run \
  --name jenkins-blueocean \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  --volume "$HOME":/home \
  --restart=on-failure \
  --env JAVA_OPTS="-Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true" \
  myjenkins-blueocean:2.426.2-1 
```

## Menyiapkan Jenkins Wizard
- Buka browser Anda dan jalankan http://localhost:8080. Tunggu hingga halaman Unlock Jenkins muncul.
- salin password di docker logs
  ```bash
  docker logs jenkins-blueocean
  # Jenkins initial setup is required. An admin user has been created and a password generated.
  # Please use the following password to proceed to installation:
  
  1fb5e900d96a41b6a8028dcb943a512a

  # This may also be found at: /var/jenkins_home/secrets/initialAdminPassword
  ```
- Install suggested plugins
- create user
- save and finish