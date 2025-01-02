# deployment
## bagaimana cara update aplikasi
- sekarang kita sudah tau bagaimana cara mem package aplikasi kita di Pod
  - menggunakan volume
  - menggunakan konfigurasi configmap dari secret
  - mengakses Pod
  - membuat Pod bisa berkomunikasi dengan Pod lain menggunakan service
  - sekarang pertanyaanya, bagaimana jika kita ingin mengupdate aplikasi kita?

- update aplikasi secara manual bukanlah hal bijak
  - kesalahan kecil yang kita lakukan update secara manual, bisa menyebabkan downtime,
  - sehingga aplikasi kita tidak bisa diakses
- kubernetes memiliki fitur Deployment, 
  - yaitu resource untuk melakukan deployment aplikasi dan update aplikasi secara deklaratif menggunakan file konfigurasi
- saat kita membuat Deployment, secara otomatis kuberntes akan membuat ReplicaSet, 
  - yang mana ReplicaSet akan secara otomatis membuat Pod
- membuat Deployment hampir sama seperti membuat ReplicationSet

## configuration
### template
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deployment-name
  labels:
    label-key1: label-value1
  annotations:
    annotation-key1: annotation-value1
spec:
  replicas: 3
  selector:
    matchLabels:
      label-key1: label-value1
  template:
    metadata:
      name: pod-name
      labels:
        label-key1: label-value1
    spec:
      containers:
      - name: container-name
        image: image-name
        ports:
        - containerPort: 80
        readinessProbe:
          httpGet:
            path: /health
            port: 80
          initialDelaySeconds: 0
          periodSeconds: 10
          failureThreshold: 3
          successThreshold: 1
          timeoutSeconds: 1
```

### example
```yaml
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
```

## command
```sh
kubectl apply -f deployment.yaml
kubectl get deployments
kubectl describe deployment <name_deployment>
kubectl delete deployment <name_deployment>
```