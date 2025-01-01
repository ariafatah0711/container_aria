# Rollback Deployment
- saat terjadi masalah ketika deploy aplikasi terbaru menggunakan deployment
  - cara paling mudah agar tidak terjadi error terlalu lama adalah rollback ke deployment sebelumnya
- cara manualnya
  - bisa dilakukan dengan mengupdate menggunakan deployment baru, namun versi aplikasinya di set ke versi sebelumnya
- atau ada cara yang lebih mudah, secara otomatis menggunakan fitur rollout kubernetes untuk rollback ke versi sebelumnya

## kubernetes Rollout
```bash
kubectl rollout history <object> <name>
kubectl rollout pause <object> <name>
kubectl rollout resume <object> <name>
kubectl rollout restart <object> <name> 
kubectl rollout status <object> <name>
kubectl rollout undo <object> <name>

# object yang bisa dipakai
*  deployments
*  daemonsets
*  statefulsets

kubectl rollout undo deployment <name_deployment>
```

## deployment v3
```bash
## deployment-update-again.yaml
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
          image: khannedy/nodejs-web:3
          ports:
            - containerPort: 3000
```

- before after
  ```bash
  image: khannedy/nodejs-web:2

  image: khannedy/nodejs-web:3
  ```

## example
```bash
kubectl rollout history deployment nodejs-web
# deployment.apps/nodejs-web
# REVISION  CHANGE-CAUSE
# 1         <none>
# 2         <none>

kubectl rollout status deployment nodejs-web
# deployment "nodejs-web" successfully rolled out

kubectl create -f deployment-update-again.yaml
curl http://192.168.49.2:30001/
# Application 3.0

kubectl rollout undo deployment/nodejs-web
# deployment.apps/nodejs-web rolled back
kubectl rollout status deployment/nodejs-web
# deployment "nodejs-web" successfully rolled out
curl http://192.168.49.2:30001/
# Application 2.0

# jika di undo lagi akan kembali menjadi versi 3 lagi
```