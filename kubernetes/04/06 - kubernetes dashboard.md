# kubernetes dashboard
- sebelumnya kita selalu menggunakan terminal untuk memanage object di kubernetes
- di kenyataanya mungkin nanti kita akan menggunakan Cloud Provider untuk managee object di kubernetes
  - dimana cloud Provider sudah menyediakan web user interface untuk manage object kubernetes
- atau jika kita menginstall kubernetes di datacenter sendiri,
  - kita juga bisa menginstall web user interface untuk manage object di kubernetes
  - namanya adalah kubernetes dashboard
- kubernetes dashboard adalah aplikasi opensource yang digunakan untuk manage object di kubernetes menggunakan web

[kubernetes](https://github.com/kubernetes/dashboard)

## minikube dashboard
```bash
minikube addons enable dashboar
kubectl get all --namespace kubernetes-dashboard
minikube dashboard
```