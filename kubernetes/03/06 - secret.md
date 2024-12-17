# secret
## sensitive data
- saat kita menggunakan configmap, maka data yang ada di dalam configmap dianggap tidak sensitive
- tapi kadang konfigurasi aplikasi kita, butuh data yang sifatnya sensitive seperti username, password database, API key, secret key, dan sejenisnya
- untuk menyimpan jenis data sensitive seperti itu
  - di kubernetes kita bisa menggunakan object
  - yang disebut secret sama seperti configMap berisikan data key-value

- kubernetes menyimapn secret secara aman dengan cara hanya mendistribusikan Secret pada Node yang memang hanya membutuhkan secret tertentu
  - secret selalu disimpan di memory di Node dan tidak pernah disimapn di physical storage,
  - di master node sendiri (lebih tepatnya di etcd), secret disimpan dengan cara di encyrpt, sehingga menjadi lebih aman
  - secret sederhana, gunakan configMap untuk konfigurasi yang tidak sensitif, dan gunakan secret untuk konfigurasi yang bersifat sensitif

- env secret hanya bisa dilihat ketika masuk di container

## configuration
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: configmap-name
data:
  ENV: base64(VALUE)
stringData:
  ENV: VALUE
```

- example
  ```yaml
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: nodejs-env-config
  data:
    APPLICATION: My Cool Application

  ---

  apiVersion: v1
  kind: Secret
  metadata:
    name: nodejs-env-secret
  stringData:
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
              - secretRef:
                  name: nodejs-env-secret

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

## command
```sh
kubectl get secrets
kubectl desciribe secret <secret_name>
```