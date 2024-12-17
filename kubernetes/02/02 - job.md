# job
- sebelumnya kita hanya membahasa tentang pod yang berjalan tanpa berhenti
  - tapi ada kalanya kita butuh menjalankan perintah yang hanya berjalan sekali lalu berhenti
- job => resource di kubernetes yang digunakan untuk menjalankan pod yang hanya butuh berjalan sekali lalu berhenti
- pada replication controler, replication set dan daemon set, jika pod mati
  - maka secara otomatis pod akan dijalankan ulang
- berbeda dengan job, pod akan mati jika pekerjaanya selesai

## contoh
- aplikasi untuk backup atau resource database
- aplikasi untuk import export data
- aplikasi untuk menjalankan process batch

## configuration
- template
  ```yaml
  apiVersion: batch/v1
  kind: Job
  metadata:
    name: job-name
  spec:
    completions: 5
    parallelism: 2
    selector:
      matchLabels:
        abel-key1: label-value1
    template:
      metadata:
        name: pod-name
        labels:
          label-key1: label-value1
      spec:
        restartPolicy: Never
        containers:
          - name: container-name
            image: image-name
            ports:
              - containerPort: 80
  ```

- example
  ```yaml
  apiVersion: batch/v1
  kind: Job
  metadata:
    name: nodejs-job
  spec:
    completions: 4
    parallelism: 2
    template:
      spec:
        restartPolicy: Never
        containers:
          - name: nodejs-job
            image: khannedy/nodejs-job
  ```

## penjelasan
- completions => berapa kali pod akan aktif (default 1)
- parallelism => berapa banyak pod yang berjalan pada 1 waktu (default 1)
- restartPolicy: Never => harus never agar berhenti, jika always akan aktif terus

## command
```sh
kubectl get job
kubectl delete job <name_job>

kubectl get all
nodejs-job-8b5sg       0/1     Completed          0              84s
nodejs-job-d2dlq       0/1     Completed          0              56s
nodejs-job-dj8wr       0/1     Completed          0              84s
nodejs-job-xlxnw       0/1     Completed          0              53s
```