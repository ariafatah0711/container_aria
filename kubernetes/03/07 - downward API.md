# donward API
- konfigurasi yang kita set secara manual bisa ditangani dengan baik menggunakan configMap dan secret
  - namun bagaimana dengan konfigurasi yang dinamis? seperti informasi Pod dan Node?
  - kuberntes memiliki downward API. Downward API bisa memungkinakan kita mengambil informasi seputar Pod dan Node melalui environment variable
- jangan bingung dengan kata API, Downward API sendiri bukan RESTful API
  - ini hanya cara untuk mendapatkan informasi seputar Pod dan Node

## metadata
- requests.cpu => jumlah CPU yang di request
- requests.memory => jumlah Memory yang di request
- limits.cpu => jumlah limit maksimal CPU
- limits.memory => jumlah limit maksimal Memory

- metadata.name => nama pod
- metadata.namespace => namespace pod
- metadata.uid => id pod
- metadata.labells['<KEY>'] => label pod
- metadata.annotations['<KEY>'] => anotation pod

- status.podIP => ip address pod
- spec.serviceAccountName => name service account pod
- spec.nodeName => nama Node
- status.nostIP => ip address node

## configuration
- example
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nodejs-env-config
data:
  APPLICATION: My Cool Application
  VERSION: 1.0.0

---

apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nodejs-env
spec:
  replicas: 3
  selector:
    matchLabels:
      name: nodejs-env
  template:
    metadata:
      name: nodejs-env
      labels:
        name: nodejs-env
    spec:
      containers:
        - name: nodejs-env
          image: khannedy/nodejs-env
          ports:
            - containerPort: 3000
          envFrom:
            - configMapRef:
                name: nodejs-env-config
          env:
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
            - name: POD_IP
              valueFrom:
                fieldRef:
                  fieldPath: status.podIP
            - name: POD_NODE
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
            - name: POD_NODE_IP
              valueFrom:
                fieldRef:
                  fieldPath: status.hostIP
---

apiVersion: v1
kind: Service
metadata:
  name: nodejs-env-service
spec:
  type: NodePort
  selector:
    name: nodejs-env
  ports:
    - port: 3000
      targetPort: 3000
      nodePort: 30001
```