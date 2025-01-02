# Computational Resources
- jadi saat membuat Pod secara default kita akan menggunakan resource yang dimiliki oleh Node dimana Pod berada
- kadang kita ada kebutuhan membatasi jumlah resource yang digunakan oleh pod 
  - hal ini dilakukan agar tidak terjadi perebutan resource antar pod
- jangan sampai jika ada pod yang sibuk membuat semua pod di Node yang sama menjadi lambat karena resource nya terpakai penuh oleh Pod yang sibuk

## Request Limit
- Request dan Limit => adalah mekanisme kubernetes untuk mengontrol mekanisme penggunaan memory dan CPU
- Request => apa yang container digaransi didapatkan.
  - jika sebuah container me-request resource, maka kubernetes hanya akan menjalankan di Node yang memiliki resource tersebut
- limit => adalah untuk memastikan bahwa container tidak akan pernah melewati resource tersebut.
  - container hanya boleh menggunakan resource sampai lmit, tidak boleh lebih

## template
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-name
  labels:
    label-key1: label-value1
    label-key2: label-value2
    label-key3: label-value3
spec:
  volumes:
    - name: volume-name
      emptyDir: {}
  containers:
    - name: container-name
      image: image-name
      ports:
        - containerPort: 80
      resources:
        requests:
          # milli core
          cpu: 1000m
          # mebibyte
          memory: 250Mi
        limits:
          # milli core
          cpu: 2000m
          # mebibyte
          memory: 500Mi
```

## example
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
          image: khannedy/nodejs-web
          ports:
            - containerPort: 3000
          resources:
            requests:
              cpu: 1000m
              memory: 1000Mi
            limits:
              cpu: 1000m
              memory: 1000Mi

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

## run
```bash
kubectl apply -f 06\ -\ computational\ resource.yaml

# penjelasan
1000m => 1000m (milicore) => 1 core
250m => 0.25 core
1000Mi => 1 Mi(mebibyte) => 1.04 mb(megabyte)
```