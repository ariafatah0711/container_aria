# run
```bash
# docker run -d --name prometheus -p 9090:9090 prom/prometheus
docker run -d --name prometheus -p 9090:9090 --add-host=host.docker.internal:host-gateway prom/prometheus

# docker run -d --name grafana -p 3030:3030 -e "GF_SERVER_HTTP_PORT=3030" grafana/grafana
docker run -d --name grafana -p 3030:3030 -e "GF_SERVER_HTTP_PORT=3030" --add-host=host.docker.internal:host-gateway grafana/grafana
```

# setup
```bash
docker exec -it prometheus sh
vi /etc/prometheus/prometheus.yml
---
- job_name: "jenkins"                                                        
  metrics_path: /prometheus/                                                
  static_configs:                                                            
     - targets: ["host.docker.internal:8080"]
---

docker restart prometheus
```