# install kubernetes node with minikube
## installation on wsl
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start --driver=docker
```

## restart after reboot
```bash
./minkube start
```

- update: https://github.com/kubernetes/minikube

## upgrade minikube
```bash
# update, jika ada versi terbaru silakan download di website resminya gitunya: https://github.com/kubernetes/minikube
minikube update-check

# stop, hapus
minikube stop
minikube delete 

# menjalankan minikube
minikube start --vm-driver=(virtualbox|docker)
minikube start --vm-driver=virtualbox --cpus=2 --memory=2g --disk-size=20g

# ip
minikube ip
```

## service
```bash
minikube service <name-service>
minikube service list
```

## addons
```bash
minikube addons list
minikube addons enable ingress

kubectl get pod --namespace kube-system # versi lama 
kubectl get all --namespace ingress-nginx # versi baru
```