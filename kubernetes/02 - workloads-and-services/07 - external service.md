# external service
- biasanya service digunakan sebagai gateway untuk internal pod
  - tapi service juga bisa digunakan sebagai gateway untuk aplikasi external yang berada di luar kubernetes cluster

- type:
  - ClusterIP (default)
  - ExternalName (external service)
  - NodePort
  - LoadBalancer

## configuration
### service-with-endpoint
```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-service
  labels:
    label-key1: label-value1
spec:
  ports:
    - port: 80

---

apiVersion: v1
kind: Endpoints
metadata:
  name: external-service
  labels:
    label-key1: label-value1
subsets:
  - addresses:
      - ip: 11.11.11.11
      - ip: 22.22.22.22
    ports:
      - port: 80
```

### service-with-domain
```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-service
  labels:
    label-key1: label-value1
spec:
  type: ExternalName
  externalName: example.com
  ports:
    - port: 80
```

### example
```yaml
apiVersion: v1
kind: Service
metadata:
  name: example-service
  labels:
    name: example-service
spec:
  type: ExternalName
  externalName: example.com
  ports:
    - port: 80

---

apiVersion: v1
kind: Pod
metadata:
  name: curl
  labels:
    name: curl
spec:
  containers:
    - name: curl
      image: khannedy/nginx-curl
```

## command
```sh
curl example-service.default.svc.cluster.local
```