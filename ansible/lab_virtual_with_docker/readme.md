```bash
docker compose up -d

docker exec -it ansible bash -c "ssh-copy-id root@node1"
docker exec -it ansible bash -c "ssh-copy-id root@node2"

docker exec -it ansible bash -c "mkdir -p /ssh_node && \
ssh-keygen -t rsa -f /ssh_node/id_rsa -q -N '' && \
cp /ssh_node/id_rsa /ssh_node/private.key && \
ssh-copy-id -i /ssh_node/id_rsa.pub root@node1 && \
ssh-copy-id -i /ssh_node/id_rsa.pub root@node2 && \
ssh-copy-id -i /ssh_node/id_rsa.pub root@node3 && \
export ANSIBLE_CONFIG=./ansible.cfg"

docker compose down
docker compose down --rmi all
```