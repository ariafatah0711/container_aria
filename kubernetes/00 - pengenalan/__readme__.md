# kubectl
```bash
# info
kubectl version

# create pod, namespace, etc
kubectl create -f (filepod.yaml|filepod.json)

# get
kubectl get (nodes|node|no)
kubectl get (pods|pod)
kubectl get pod --all-namespace
kubectl get pod -o (wide|yaml)
kubectl get pods --show-labels
kubectl get (namespaces|namespace|ns)

kubectl get rc
kubectl get rs
kubectl get daemonsets
kubectl get job
kubectl get configmaps
kubectl get secrets

kubectl get all
kubectl get all --namespace <namespace>

# delete
kubectl delete pod <namapod> | kubectl delete pod pod1 pod2
kubectl delete pod <namapod> --namespace <namespace>
kubectl delete pod -l key=value

kubectl delete rc <name_rc>
kubectl delete rs <name_rs>
kubectl delete daemonsets <name_daemonsets>
kubectl delete job <name_job>
kubectl delete configmaps <name_configmap>

kubectl delete namespace <namespace>
kubectl delete pod --all --namespace <namespace>

kubectl delete all
kubectl delete all --all --namespace <namespace>

# describe
kubectl describe node <nama_node>
kubectl describe pod <nama_pod>
kubectl describe configmap <name_configmap>
## rs|rc|daemonsets

# logs
kubectl logs <name_pod>

# port forwarding (hanya di development jika prod tidak digunakan)
kubectl port-forward <namapod> portLocal:portRemote
```

# label, annotation, namespace
## pod bisa diganti dengan ()
```bash
# add label, changem and find label
kubectl label pod <nama_pod> env=prod
kubectl label pod <nama_pod> env=dev --overwrite

kubectl get all
kubectl get pods -l key
kubectl get pods -l key=value
kubectl get pods -l '!key'
kubectl get pods -l 'key!=value'
kubectl get pods -l 'key in (value1, value2)'
kubectl get pods -l 'key notin (value1, value2, value3)'
kubectl get pods -l key, key1=value1

# annotation
kubectl annotate pod <nama_pod> key=value --overwrite
```

## namespace
```bash
kubectl get (namespaces|namespace|ns)
kubectl get pod --namespace <namespace> | kubectl get pod -n <namespace>

# delete namespace beserta resource
# harus create namespace dulu pakae config.yaml, baru bisa masukin pod ke namespace
kubectl create -f config.yaml --namespace <namespac/e>
kubectl delete namespace <namespace>

# delete namespace without delete namespace
kubectl delete pod --all --namespace <namespace>
```

# service
```bash
kubectl get service
kubectl delete service <name_servive>

# mengakses service di dalam port
kubectl exec <name_pod> -it -- /bin/sh
curl http://cluster-ip:port

# mengakses service
## with env
kubectl exec <name_pod> -it -- env | grep -i NGINX
NGINX_SERVICE_SERVICE_PORT=80
NGINX_SERVICE_SERVICE_HOST=10.98.205.79

curl $NGINX_SERVICE_SERVICE_HOST:$NGINX_SERVICE_SERVICE_PORT

## with dns
nama-service.nama-namespace.svc.cluster.local
curl http://nginx-service.default.svc.cluster.local

## nodePort
kubectl get node -o wide
NAME       STATUS   ROLES           AGE     VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION                       CONTAINER-RUNTIME
minikube   Ready    control-plane   3d10h   v1.31.0   192.168.49.2   <none>        Ubuntu 22.04.4 LTS   5.15.153.1-microsoft-standard-WSL2   docker://27.2.0

kubectl get service
NAME            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
kubernetes      ClusterIP   10.96.0.1        <none>        443/TCP        5m18s
nginx-service   NodePort    10.111.219.184   <none>        80:30001/TCP   5m9s

curl 192.168.49.2:30001
```

# deployment
```bash
kubectl apply -f namafile.yaml
kubectl get deployments
kubectl describe deployment <name_deployment>
kubectl delete deployment <name_deployment>

kubectl rollout history <object> <name>
kubectl rollout pause <object> <name>
kubectl rollout resume <object> <name>
kubectl rollout restart <object> <name> 
kubectl rollout status <object> <name>
kubectl rollout undo <object> <name>
```

# persistent volume
```bash
kubectl get pv
kubectl describe pv <name_pv>
kubectl get pvc # persistent volume claim
kubectl describe pvc <name_pvc>

kubectl delete pv <name_pv>
kubectl delete pvc <name_pvc>
```

# addons
## ingress
```bash
kubectl get ingress
```