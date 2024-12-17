# pod
- unit terkecil yang bisa kita deploy di kubernetes cluster
- pod berisi satu atau lebih container
- secara sederhana pod adalah aplikasi kita yang running di kubernetes cluster
  - pod hanya bisa di deploy di 1 node tidak bisa dibagi bagi
- jika kita langsung menggunakan container. nanti kita hanya bisa pake satu spesifik container saja seperti docker makanya kita butuh pod
  - seperti kita ingin scalling aplikasi ke aplikasi yang lainya

# command
## create pod with configuration file
- template
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: pod-name
  spec:
    containers:
      - name: container-name
        image: image-name
        ports:
          - containerPort: 80
  ```

- example
  ```yaml
  apiVersion: v1
  kind: pod
  metadata:
      name: nginx
  spec:
      containers:
          - name: nginx
            image: nginx
            ports:
              - containerPort: 80
          # - name: nginx
          #   image: nginx
          #   ports:
          #     - containerPort: 80
  ```

## get pod
```bash
kubectl get pod
kubectl describe pod <nama_pod>
```

# create Pod, akses Pod, delete Pod
## create pod
```bash
kubectl create -f filepod.yaml
kubectl create -f filepod.json

# Create a pod based on the JSON passed into stdin
cat pod.json | kubectl create -f -

# Edit the data in registry.yaml in JSON then create the resource using the edited data
kubectl create -f registry.yaml --edit -o json
```

## akses pod
```bash
kubectl port-forward <namapod> portLocal:portRemote
kubectl port-forward nginx 8881:80
```

## delete pod
```bash
kubectl delete pod <namapod>
kubectl delete pod pod1 pod2
kubectl delete pod <namapod> --namespace <namespace>
kubectl delete pod -l key=value
```