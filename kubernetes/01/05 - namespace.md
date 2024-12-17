# namespace
- kapan menggunakan namespace
  - ketika resource di kubernetes sudah terlalu banyak
  - ketika butuh memisahkan resource untuk multi-telnant, team atau environment
  - nama resource bisa sama jika beberapa di namespace berbeda
- kesimpulan: bisa create nama resource yang sama namun harus di namespace yang berbeda
  - pod dengan nama yang sama boleh berjalan asalkan namespace yang berbeda
  - namespace bukanlah cara untuk mengisolasi resource
  - walaupun berbeda namespace, pod akan tetap bisa saling berkomunikasi dengan pod lain di namespace yang berbeda
- default namespace yang digunakan kubernetes adalah namespace default

## configuration
- template
  ```yaml
  apiVersion: v1
  kind: Namespace
  metadata:
    name: nama-namespace
  ```

- example
  ```yaml
  apiVersion: v1
  kind: Namespace
  metadata:
    name: finance
  ```

# command
## get namespace
```bash
kubectl get (namespaces|namespace|ns)
kubectl get pod --namespacae <namaspace>

kubectl get pods --namespace kube-system
```

## create namespace
```bash
kubectl create -f config.yaml --namespace <namespace>

# example
```

## delate namespace
```bash
# delete namespace beserta resource
# harus create namespace dulu pakae config.yaml, baru bisa masukin pod ke namespace
kubectl create -f config.yaml --namespace <namespac/e>
kubectl delete namespace <namespace>

# delete namespace without delete namespace
kubectl delete pod --all --namespace <namespace>
```