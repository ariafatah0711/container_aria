# cron job
- cron job => aplikasi untuk penjadwalan yang biasanya ada di sistem operasi unix
  - dengan menggunakan cronjob kita bisa menjadwalkan aplikasi berjalan sesuai jadwal yang kita inginkan
  - kubernetes mendukung resource cron job, dimana cara kerjanya mirip job, 
    - hanya saja bisa berulang kali sesuai jadwal yang kita inginkan
  - cron job juga bisa memungkinkan kita untuk menjalankan aplikasi dengan waktu yang telah di tentukan

- contoh penggunaan cronjob
  - aplikasi untuk membuat laporan harian
  - aplikasi untuk backup data secara berkala
  - aplikasi untuk mengirim data tqgihan tiap bulan ke pihak lain
  - aplikasi untuk menarik dana pinjaman yang jatuh tempo bulanan

- cronjob expresion => https://crontab.guru/

## configuration
- template
  ```yaml
  apiVersion: batch/v1beta1
  kind: CronJob
  metadata:
    name: cron-job-name
  spec:
    schedule: "* * * * *"
    jobTemplate:
      spec:
        selector:
          matchLabels:
            label-key1: label-value1
        template:
          metadata:
            name: pod-name
            labels:
              app: pod-la
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
  kind: CronJob
  metadata:
    name: nodejs-cronjob
    labels:
      name: nodejs-cronjob
  spec:
    schedule: "* * * * *"
    jobTemplate:
      spec:
        template:
          metadata:
            name: nodejs-cronjob
            labels:
              name: nodejs-cronjob
          spec:
            restartPolicy: Never
            containers:
              - name: nodejs-cronjob
                image: khannedy/nodejs-job
  ```

- ketika gunakan cronjob kita perlu namabahins scedhuler dan jobTemplates

## command
```sh
kubectl get cronjobs
kubectl delete cronjobs <name_cronjobs>
```