# sharing volume
- karena di dalam pod kita bisa membuat lebi dari 1 container
  - maka, volume di pod pun bisa kita sharing ke beberapa container
- hal ini sangat cocok ketika kita butuh sharing direktori antar container,
  - misal container pertama membuat file, container kedua memperoses file

## configuration
### example
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
      volumes:
        - name: html
          emptyDir: {}
      containers:
        - name: nodejs-writer
          image: khannedy/nodejs-writer
          volumeMounts:
            - mountPath: /app/html
              name: html
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
          volumeMounts:
            - mountPath: /usr/share/nginx/html
              name: html

---

apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  selector:
    name: nginx
  ports:
    - port: 8080
      targetPort: 80
      nodePort: 30001
```