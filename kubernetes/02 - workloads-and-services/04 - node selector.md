# node selector
- kadang kita membuat node dengan spesifikasi dari node biasanya
  - misal node yang memiliki GPU, atau dengan hardisk SSD
  - dengan node selector, kita bisa meminta kubernetes untuk menjalankan pod pada node tertentu

## configuration
- template
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: pod-name
  spec:
    nodeSelector:
      gpu: "true" # jika ada label yang sama tidak akan jalan
    containers:
      - name: container-name
        image: image-name
        ports:
          - containerPort: 80
  ```

- example
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: nginx
  spec:
    nodeSelector:
      gpu: "true" 
    containers:
      - name: nginx
        image: nginx
        ports:
          - containerPort: 80
  ```

## command
```sh
kubectl create -f config.yaml
kubectl label node <name_node> key=value
kubectl get label --show-labels

# jika tidak ada node yang match maka akan pending
nginx                  0/1     Pending   0              3s
```