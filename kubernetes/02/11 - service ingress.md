# ingress
- masalah saat mengekspose service
  - jika menggunakan NodePort
    - maka semua node harus di expose ke public
    - client harus tau semua ip address semua node
  - jika menggunakan load balancer
    - maka semua load balancer harus terekspose ke public
    - client harus tau ip address semua load balancer

- ingress => salah satu yang bisa digunakan untuk expose service
  - berbeda dengan LoadBalancer atau NodePort,
    - jika menggunakan ingress, client hanya butuh tahu satu ip address ingress
  - ketika client melakukan request ke ingress, pemilihan service nya ditentukan menggunakan hostname dari request
    - artinya bisa menggunakan <host>/serviceA
  - ingress hanya mendukung protokol http
  - sebenernya ingress ini adalah nginx

## configuration
```yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: ingress-name
  labels:
    label-key1: label-value1
spec:
  rules:
    - host: sub.domain.com
      http:
        paths:
          - path: /
            backend:
              serviceName: service-name
              servicePort: 80
```

- example
  ```yaml
  apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    name: nginx
  spec:
    replicas: 3
    selector:
      matchLabels:
        name: nginx
    template:
      metadata:
        name: nginx
        labels:
          name: nginx
      spec:
        containers:
          - name: nginx
            image: nginx
            ports:
              - containerPort: 80

  ---

  apiVersion: v1
  kind: Service
  metadata:
    name: nginx-service
  spec:
    selector:
      name: nginx
    ports:
      - port: 80
        targetPort: 80

  ---

  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    name: nginx-ingress
    labels:
      name: nginx-ingress
  spec:
    ingressClassName: nginx
    rules:
      - host: nginx.aria.local
        http:
          paths:
            - path: /
              pathType: Prefix
              backend:
                  service:
                    name: nginx-service
                    port:
                      number: 80
  ```

# command
## add addons, and check addons
```sh
minikube addons list
minikube addons enable ingress

kubectl get pod --namespace kube-system
kubectl get all --namespace ingress-nginx

kubectl get ingress
```

## test ingress
```sh
kubectl create -f config.yaml

minikube ip
kubectl get ingress

echo "192.168.49.2    nginx.aria.local" >> /etc/hosts 

curl nginx.aria.local

kubectl delete ingress --all
kubectl delete all --all
```