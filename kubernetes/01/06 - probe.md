# probe
- sebelum fokus Replication Controler, Replication set
- 3 kali pengecekan

## pengecekan
- liveness
  - mengecek kapan perlu merestart pod
  - misal saat liveness probe pada pod tidak meresponse kubelet akan otomatis me restart pod
- readiness
  - mengecek apakah pod siap menerima trafic 
  - jika liveness melakukan restart jika gagal
    - kalo readines akan stop pod jika gagal / tidak siap menerima trafic
- startup probe
  - melakukan pengecekan hanya saja di awal saja
  - startup probe cocok untuk pod yang membutuhkan proses startup lama
    - ini dapat diguanakn untuk memastikan pod tidak mati oleh kubelet sesbelum sesuai berjalan sempurna

## mekanisme pengecekan probe
- HTTP get (untuk web)
- TCP Socket (untuk tcp)
- command exec (menggunakan exec)

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
        # probe
        livenessProbe:
          httpGet:
            path: /health
            port: 80
          initialDelaySeconds: 0
          periodSeconds: 10
          timeoutSeconds: 1
          successThreshold: 1
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 0
          periodSeconds: 10
          timeoutSeconds: 1
          successThreshold: 1
          failureThreshold: 3
        startupProbe:
          httpGet:
            path: / 
            port: 80
          initialDelaySeconds: 0
          periodSeconds: 10
          timeoutSeconds: 1
          successThreshold: 1
          failureThreshold: 3
  ```

- example
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: nginx-with-probe
  spec:
    containers:
      - name: nginx
        image: nginx
        ports:
          - containerPort: 80
        # probe
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 0
          periodSeconds: 10
          timeoutSeconds: 1
          successThreshold: 1
          failureThreshold: 4
  ```

## penjelasan
- option
  - initialDelaySeconds => waktu tunggu sebelum pengecekan / setelah container jalan (defaultnya 0)
  - periodSeconds => periode / seberapa sering waktu pengecekan dilakukan (default 10)
  - timeoutSeconds => waktu timeout ketika pengecekan gagal (default 1)
  - successTreshold => minimum dianggap sukses setelah berstatus failure (default 1)
  - failureTreshold => minimun dianggap gagal (default 3)

# command
## show kubectl probe
```bash
kubectl describe pod
Liveness:       http-get http://:80/ delay=0s timeout=1s period=10s #success=1 #failure=4

# setelah pengecekan 5 kali dan error trus maka akan crashLoopBackOff
WSL at   bash  ~/kube_aria/dasar ❯  kubectl get pods
NAME                   READY   STATUS             RESTARTS     AGE
nginx-with-probe       1/1     Running            0            8m26s
nginx-with-probe-err   0/1     CrashLoopBackOff   4 (5s ago)   3m30s
```