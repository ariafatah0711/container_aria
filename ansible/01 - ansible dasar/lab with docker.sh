# network
docker network create ansible_net

# manage controler node
# docker run -dit --name ansible-controller --hostname ansible-controller --network ansible_net ubuntu:20.04
docker run -dit --name ansible-controller --hostname ansible-controller --network ansible_net \
-v /mnt/c/Users/ariaf/OneDrive/Dokumen/github_aria/container_aria/ansible/:/ansible_aria:Z ubuntu:20.04

# manage node
docker run -dit --name node1 --hostname node1 --network ansible_net ubuntu:20.04
docker run -dit --name node2 --hostname node2 --network ansible_net ubuntu:20.04

## setup controler node
docker exec -it ansible-controller bash
apt update && apt install -y python3 python3-pip sshpass openssh-client && pip install ansible

## setup node
docker exec -it node1 bash
apt update && apt install -y openssh-server expect && service ssh start # 6,35
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
service ssh restart
expect << EOF
spawn passwd root
expect "New password:"
send "123\r"
expect "Retype new password:"
send "123\r"
expect eof
EOF

docker exec -it node2 bash
apt update && apt install -y openssh-server expect && service ssh start # 6,35
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
service ssh restart
expect << EOF
spawn passwd root
expect "New password:"
send "123\r"
expect "Retype new password:"
send "123\r"
expect eof
EOF

## generate ssh key
ssh-keygen -t rsa -b 2048 # controler
ssh-copy-id root@node1
ssh-copy-id root@node2

# ssh
ssh node1
ssh node2