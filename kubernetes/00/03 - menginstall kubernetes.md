# install kubectl for kubernetes master
## kubectl
- digunakan untuk berinteraksi dengan cluster
- install 
  ```bash
  sudo snap install kubectl
  ./kubectl version
  ```

# install kubenetes node
## minkube
- minikube on wsl => https://github.com/dubeytapan12/RunK8sOnWSL
  ```bash
  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  sudo install minikube-linux-amd64 /usr/local/bin/minikube
  minikube start --driver=docker
  ```

- minikube on vm
- https://github.com/kubernetes/minikube
  ```bash
  # comming soon
  ```

## kind (kubernetes in docker)
- https://kind.sigs.k8s.io/docs/user/quick-start/
  ```bash
  curl -Lo ./kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
  sudo install -o root -g root -m 0755 kind /usr/local/bin/kind

  kind create cluster
  ```

## k3s
- installation
  ```bash
  curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash
  k3d cluster create mycluster
  ```