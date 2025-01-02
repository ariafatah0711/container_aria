# update deployment
- untuk update deployment caranya sangat mudah, kita hanya tinggal gunakan perintah apply lagi
  - untuk mengupdate Deployment terbaru
- saat Deployment terbaru di eksekusi, secara otomatis Deployment akan membuat Replication Set baru
  - lalu menyalakan Pod baru, setelah Pod siap, Deployment akan menghapus Pod lama secara otomatis
- ini membuat proses update berjalan seamless, dan tidak terjadi downtime

## configuration
- example
  ```yaml
  ## deployment pertama
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: nodejs-web
    labels:
      name: nodejs-web
  spec:
    replicas: 3
    selector:
      matchLabels:
        name: nodejs-web
    template:
      metadata:
        name: nodejs-web
        labels:
          name: nodejs-web
      spec:
        containers:
          - name: nodejs-web
            image: khannedy/nodejs-web:1
            ports:
              - containerPort: 3000

  ---

  apiVersion: v1
  kind: Service
  metadata:
    name: nodejs-web-service
  spec:
    type: NodePort
    selector:
      name: nodejs-web
    ports:
      - port: 3000
        targetPort: 3000
        nodePort: 30001


  ## deployment ke 2
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: nodejs-web
    labels:
      name: nodejs-web
  spec:
    replicas: 3
    selector:
      matchLabels:
        name: nodejs-web
    template:
      metadata:
        name: nodejs-web
        labels:
          name: nodejs-web
      spec:
        containers:
          - name: nodejs-web
            image: khannedy/nodejs-web:2
            ports:
              - containerPort: 3000
  ```

## command
```sh
kubectl apply -f 01\ -\ deployment.yaml
kubectl apply -f 02\ -\ deployment\ update.yaml
```