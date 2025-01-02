# replication set
- pada awalnya replicationn controlernya digunakan untuk menjaga jumlah replica pot dan men-rescheduler pod yang mati
  - namun sekarang sudah diganti dengan replication set
  - replication controler sudah tidak direkomendasikan
- replication set hampir mirip dengan replication controler
  - namun di replication set memiliki kemampuan label selector yang lebih expressive dibandingkan replication controler

## configuration
- template
  ```yaml
  apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    name: replica-set-name
    labels:
      label-key1: label-value1
    annotations:
      annotation-key1: annotation-value1
  spec:
    replicas: 3
    selector:
      matchLabels: # beda disinninya aja
        label-key1: label-value1
    template:
      metadata:
        name: pod-name
        labels:
          label-key1: label-value1
      spec:
        containers:
        - name: container-name
          image: image-name
          ports:
          - containerPort: 80
  ```

- example
  ```yaml
  apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    name: nginx-rs
  spec:
    replicas: 3
    selector:
      matchLabels:
        app: nginx
    template:
      metadata:
        name: nginx-rs
        labels:
          app: nginx
      spec:
        containers:
        - name: nginx
          image: nginx
          ports:
          - containerPort: 80
  ```

# command
- Replication Set
```bash
kubectl get rs
kubectl delete rs <name_rs>
```

## label selector match expression
- match expression => jika gunakan matchLabels mirip dengan kaya replication controler
  - namun ada fitur selain matchLabels ada juga seperti matchExpression
    - In => value label harus ada di value ini
    - NotIn => value label tidak boleh ada di value in
    - Exits => label harus ada
    - NotExis => label tidak boleh ada

## configuration
- template
  ```yaml
  spec:
    replicas: 3
    selector:
      matchLabels:
        label-key1: label-value1
      matchExpressions:
        - key: label-key
          operator: In
          values:
            - label-value1
            - label-value2
    template:
      metadata:
        name: pod-name
        labels:
          label-key1: label-value1
      spec:
        containers:
        - name: container-name
          image: image-name
          ports:
          - containerPort: 80
  ```

- example
  ```yaml
  apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    name: nginx-rs2
  spec:
    replicas: 3
    selector:
      # matchLabels:
      #   label-key1: label-value1
      matchExpressions:
        - key: app
          operator: In
          values:
            - nginx
            - apache2
        - key: env
          operator: In
          values:
            - dev
            - prod
            - qa
    template:
      metadata:
        name: nginx-rs2
        labels:
          app: nginx
          env: prod
      spec:
        containers:
        - name: nginx
          image: nginx
          ports:
          - containerPort: 80
  ```