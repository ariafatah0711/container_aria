# multi container pod
- saat kita menggunakan Docker, kita selalu diajarkan bahwa 1 aplikasi adalah 1 container
  - di kubernetes sedikit berbeda, saat kita deploy aplikasi kita, maka akan disimpan dalam 1 pod
  - kenapa pod tidak container?
    - karena sebenarnya di dalam pod kita bisa menambahkan banyak container
  - ini cocok sekali jika  memang kita butuh aplikasi yang berjalan di beberapa container dan jika ingin scale, harus semua nya ikut scale

## configuration
### template
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      name: nginx
  template:
    metadata:
      name: nginx
      labels:
        name: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
        - name: nodejs-web
          image: khannedy/nodejs-web
          ports:
            - containerPort: 3000

---

apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    name: nginx
  ports:
    - port: 8080
      targetPort: 80
      name: nginx
    - port: 3000
      targetPort: 3000
      name: nodejs-web

---

apiVersion: v1
kind: Pod
metadata:
  name: curl
  labels:
    name: curl
spec:
  containers:
    - name: curl
      image: khannedy/nginx-curl
```