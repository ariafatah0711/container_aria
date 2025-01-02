# manage kubernetes object
- sebelumnya kita sudah tahu cara untuk membuat object di kubernetes menggunakaan perintah
  ```kubectl create -f config.yaml```
- sebenernya ada perintah lain untuk melakukan management kubernetes object seperti mengupdate, atau menghapus

## command
```yaml
# create object
kubectl create -f namafile.yaml

# replace object => namun hanya beberapa aja yang bisa
## kaya upgrade image, dll
kubectl replace -f namafile.yaml

# get object
kubectl get -f namafile.yaml -o yaml/json

# remove object
kubectl delelte -f namafile.yaml
```

# declarative management
- yang lagi banyak dipakai dibanding create
  ```bash
  # membuat atau mengupdate kubernetes object
  kubectl apply -f namafile.yaml
  ```

- saat menggunakan declarative management, file konfigurasi akan disimpan di dalam annotations object
  - hal ini sangat bermanfaat saat menggunakan object Deployment
  - rata rata sekarang kebanyakan Declarative Management lebih sering digunakan dibandingkan imperative management
- ketika kita apply nantinya datanya di simpen di annations
- fungsinya kita bisa ngelakuin rollback / update dengan lebih mudah