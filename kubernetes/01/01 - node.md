# node
- node => worker machine di kubernetes (disebut minion di versi lama)
- node bisa berbentuk dalam vm atau mesin fisik
- di dalam Node selalu terdapat kubelet, kubeproxy, dan container manager

## command
```bash
# melihat semua nodes yang ada pada cluster
kubectl get nodes
kubectl get node
kubectl get no # (bisa pake 2 huruf di awal)

kubectl describe node <nama_node>
kubectl describe node minikube
```