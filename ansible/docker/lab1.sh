docker-compose down
docker-compose up -d

# docker exec -it ansible bash -c "mkdir -p /ssh_node && \
# ssh-keygen -t rsa -f /ssh_node/id_rsa -q -N '' && \
# cp /ssh_node/id_rsa /ssh_node/private.key && \
# ssh-copy-id -i /ssh_node/id_rsa.pub root@node1 && \
# ssh-copy-id -i /ssh_node/id_rsa.pub root@node2 && \
# ssh-copy-id -i /ssh_node/id_rsa.pub root@node3 && \
# ssh-copy-id -i /ssh_node/id_rsa.pub root@node_app && \
# export ANSIBLE_CONFIG=./ansible.cfg"

docker exec -it ansible bash -c "
mkdir -p /ssh_node && \
ssh-keygen -t rsa -f /ssh_node/id_rsa -q -N '' && \
cp /ssh_node/id_rsa /ssh_node/private.key && \
sshpass -p '123' ssh-copy-id -i /ssh_node/id_rsa.pub -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@node1 && \
sshpass -p '123' ssh-copy-id -i /ssh_node/id_rsa.pub -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@node2 && \
sshpass -p '123' ssh-copy-id -i /ssh_node/id_rsa.pub -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@node3 && \
sshpass -p '123' ssh-copy-id -i /ssh_node/id_rsa.pub -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@node_app && \
export ANSIBLE_CONFIG=./ansible.cfg"

docker exec -it ansible bash -c "export ANSIBLE_CONFIG=./ansible.cfg &&\
cd /ansible_aria/ansible_lab &&\
ansible-playbook playbook/playbook-nginx.yaml ;\
ansible-playbook playbook/playbook-haproxy.yaml"

docker exec -it ansible bash -c "curl node_app; echo;\
curl node_app; echo;\
curl node_app; echo"