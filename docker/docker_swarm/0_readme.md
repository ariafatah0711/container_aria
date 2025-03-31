# list command
```bash
docker swarm init
docker swarm join
docker service create
docker service inspect
docker service scale
docker service update
docker node ls
docker node update
docker node promote/demote
```

# Panduan Lengkap Docker Swarm

## 1. Apa Itu Docker Swarm?
Docker Swarm adalah alat orkestrasi container yang memungkinkan manajemen beberapa container dalam cluster secara otomatis. Dengan Swarm, kita bisa melakukan deployment, scaling, dan manajemen service dengan lebih mudah dibandingkan menjalankan container satu per satu secara manual.

## 2. Instalasi Docker Swarm
Sebelum memulai, pastikan Docker sudah terinstal pada semua node (master dan worker). Jika belum, bisa menginstalnya dengan perintah berikut:

```bash
git update && sudo apt install docker.io -y
```

Setelah Docker terinstal, kita bisa menginisialisasi Docker Swarm.

## 3. Setup Cluster Docker Swarm

### 3.1. Inisialisasi Swarm pada Master Node
Jalankan perintah berikut di node utama (master):

```bash
docker swarm init
```

Perintah ini akan menghasilkan token yang digunakan untuk menambahkan worker ke dalam cluster. Untuk mendapatkan kembali token ini jika diperlukan, gunakan perintah berikut:

```bash
docker swarm join-token worker
```

### 3.2. Menambahkan Worker Node
Pada setiap worker node, jalankan perintah berikut dengan mengganti `TOKEN` dan `IP_MANAGER` sesuai yang didapat dari perintah sebelumnya:

```bash
docker swarm join --token TOKEN IP_MANAGER:2377
```

Untuk memverifikasi apakah worker sudah tergabung dalam cluster:

```bash
docker info | grep -i Swarm
docker node ls
```

## 4. Mengelola Service dalam Docker Swarm

### 4.1. Membuat Service
Pada master node, kita bisa membuat service baru dengan perintah berikut:

```bash
docker service create --name web --replicas 2 -p 80:80 nginx
```

Perintah di atas akan membuat service bernama `web` dengan dua replika menggunakan image Nginx dan memetakan port 80 dari container ke host.

Untuk melihat daftar service yang berjalan:

```bash
docker service ls
```

Untuk melihat detail service:

```bash
docker service inspect --pretty web
docker service ps web
```

### 4.2. Scaling Service
Kita bisa menambah atau mengurangi jumlah replika dengan perintah berikut:

```bash
docker service scale web=3
```

Untuk menghapus service:

```bash
docker service rm web
```

### 4.3. Rolling Update
Untuk memperbarui container dengan image baru, gunakan perintah berikut:

```bash
docker service update --image nama-image-baru web
```

Untuk memastikan update berhasil:

```bash
docker service inspect web --pretty
```

## 5. Drain Mode (Memindahkan Service ke Node Lain)
Jika ingin menonaktifkan sementara salah satu worker node dan memindahkan service ke node lain:

```bash
docker node update --availability drain worker1
```

Dengan mode `drain`, node tersebut tidak akan menerima tugas baru. Untuk mengaktifkan kembali:

```bash
docker node update --availability active worker1
```

## 6. Promosi dan Demosi Node
Kita bisa mengubah peran worker menjadi manager dengan perintah berikut:

```bash
docker node promote worker1
```

Untuk menurunkan peran manager kembali menjadi worker:

```bash
docker node demote worker1
```

## 7. Menghadapi Node yang Down
Jika salah satu node down, Swarm akan secara otomatis mengalokasikan ulang container ke node yang masih aktif. Jika leader node down dan kita memiliki beberapa manager, maka Swarm akan memilih manager lain sebagai leader baru.

## Kesimpulan
Docker Swarm sangat berguna untuk mengelola cluster container dengan lebih efisien, mempermudah deployment, scaling, dan rolling update. Dengan memahami cara kerja Swarm, kita dapat dengan mudah mengatur dan mengelola infrastruktur berbasis container secara optimal.