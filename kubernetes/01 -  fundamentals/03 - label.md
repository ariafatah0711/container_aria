# label
- digunakan untuk memberi tanda pada pod, mengorganisir pod
  - memberi informasi tambahan pada pod
  - label tidak hanya digunakan untuk pod, tapi pada semua resources di kubernetes
    - seperti Replication Controler, Replication Set, service
- masukin label harus sederhana tidak boleh ada spasi

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
```

- example
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-with-label
  labels:
    team: finance
    version: 1.4.5
    environment: production
spec:
  containers:
    - name: nginx
      image: nginx
      ports:
        - containerPort: 80
```

## command
- show pod label
  ```bash
  kubectl get pods --show-labels
  ```

- menambahkan atau mengubah label di pod
- namun tidak disarankan karena nanti beda sama configuration filenya
  ```bash
  # add label
  kubectl label pod nginx env=prod

  # change label
  kubectl label pod nginx env=dev --overwrite
  ```

- mencari label di pod
```bash
kubectl get pods -l key
kubectl get pods -l key=value
kubectl get pods -l '!key'
kubectl get pods -l 'key!=value'
kubectl get pods -l 'key in (value1, value2)'
kubectl get pods -l 'key notin (value1, value2, value3)'
kubectl get pods -l key, key1=value1
```