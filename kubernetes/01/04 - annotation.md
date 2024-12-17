# annotation
- mirip dengan label, hanya saja tidak dapat di filter seperti label
  - biasanya digunakan untuk menambahkan informasi tambahan dalam ukuran besar
  - annotation bisa menampung informasi sampai 256k

## configuration
- template
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: pod-name
    labels:
      label-key1: label-value1
    annotations:
      annotation-key1: annotation-value
      annotation-key2: veri long annotation value, bla bla bla bla bla bla
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
  kind: Pod
  metadata:
    name: nginx-with-annotation
    labels:
      team: production
      version: 1.0.1
      environment: production
    annotations:
      description: ini adalah aplikasi yang dibuat oleh tim production
      apapun: apapaun itu...
  spec:
    containers:
      - name: nginx
        image: nginx
        ports:
          - containerPort: 80
  ```

# command
## show
```bash
kubectl get pods
kubectl describe pod nginx-with-annotation
```

## menambahakan annotation
```bash
kubectl annotate pod <namapod> key=value
kubectl annotate pod <namapod> key=value --overwrite
```