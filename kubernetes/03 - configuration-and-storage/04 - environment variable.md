# environment variable
- saat kita membuat aplikasi, sering kita butuh data konfigurasi
  - agar dinamis, disarankan konfigurasi disimpan di environment, sehingga bisa diubah ubah
  - kubernetes juga mendukung environment variable untuk Pod
  - hal ini sangat berguna untuk konfigurasi aplikasi, seperti konfigurasi database, dll

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
    containers:
      - name: container-name
        image: image-name
        ports:
          - containerPort: 80
        env:
          - name: ENV_NAME
            value: "ENV VALUE"
  ```

- example
  ```yaml
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
          - mountPath: /app/folder-from-env
            name: html
        env:
          - name: HTML_LOCATION
            value: /app/folder-from-env
  ```