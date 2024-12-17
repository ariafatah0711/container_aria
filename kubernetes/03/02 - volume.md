# volume
- berkas-berkas di dalam container itu tidak permanent
  - akan terhapus seiring dihapusnya pod atau container
  - volume => sebuah direktori yang bisa diakses yang ada di dalam pod

## jenis
- empetyDir => direktori kosong
- hostPath => diguanakn untuk mensharing direktori di Node ke pod 
- gitRepo => direktori yang dibuat pertama kali dengan menclone git repository
- nfs => network file system
- dll

## configuration
- template
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
        volumeMounts:
          - mountPath: /app/volume
            name: volume-name
  ```

- example
  ```yaml
  # example
  apiVersion: v1
  kind: Pod
  metadata:
    name: nodejs-writer
    labels:
      name: nodejs-writer
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
  ```