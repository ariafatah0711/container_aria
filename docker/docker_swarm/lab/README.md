# setup using compose
```bash
# cara ini masih gagal
docker-compose up -d

docker exec -it swarm-manager sh
# docker swarm init --advertise-addr swarm-manager

docker exec -it swarm-manager docker node ls
```

# setup manual
## master
```bash
docker swarm init

docker swarm join-token worker
# copy the url to worker
# docker swarm join --token SWMTKN-1-07y8hfbu8lb7qgjvmmcziokuht45ne7xc5fnvu8gntq2amgqe8-63pt2m2xmbdw8agz7mkkzxobi manager:2377
```

## worker1
```bash
docker swarm join --token SWMTKN-1-07y8hfbu8lb7qgjvmmcziokuht45ne7xc5fnvu8gntq2amgqe8-63pt2m2xmbdw8agz7mkkzxobi manager:2377
docker info | grep -i Swarm
```

## worker2
```bash
docker swarm join --token SWMTKN-1-07y8hfbu8lb7qgjvmmcziokuht45ne7xc5fnvu8gntq2amgqe8-63pt2m2xmbdw8agz7mkkzxobi manager:2377
docker info | grep -i Swarm
```

# service (membuat service)
## manager
```bash
docker service create --name web --replicas 2 -p 80:80 nginx
docker service ls

docker service inspect --pretty web
docker service ps web
```

# scale (scalingg untuk mau berapa node gitu)
```bash
docker service scale web=3
docker service ls
docker service ps web
docker service rm web
```

# rolling update (update container)
```bash
docker service create --name web --replicas 2 -p 80:80 nginx
docker service update --image ariafatah/linktree web

docker service inspect web --pretty
```

# drain mode (memindahkan service ke node lain) drain: nonaktifkan
```bash
docker service ps web
docker service ps web | grep -i running

docker node ls
docker node update --availability drain swarm-worker1
# jadi node / worker 1 bakal nonaktif

# ketika buatt service baru node 2 tidak akan di assign
docker service create --name web1 --replicas 3 -p 81:80 ariafatah/linktree
docker service ps web1 #namun kalo dilihat nanti ada yang duplikat agar replica memnuhi 3

docker node update --abailability active
# maka akan balik lagii kalo rolling updata atau membuat service baru
```

# promote demote node (membuatt multi manager)
```bash
# bisa dengan menjoinkan sebuah node dengan inian worker bukan manager

# cara kedua bisa menggunakan promote demote
docker node promote swarm-worker1
docker node promote swarm-worker2

docker node ls
docker node demote swarm-worker2
```

## ketika salah satu down
- misal si worker 2 berhenti maka nantinya worker 1 akan aktif dengan sisa replica yang masih bisa
- ketika kita promote 2 node yang berarti ada 3 manager
  - dan ketika yang manager leader down maka
  - maka nanti leadernya akan pindah ke node yang lain gitu