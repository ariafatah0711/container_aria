FROM ubuntu:20.04

# Install dependencies
RUN apt update && apt install -y openssh-server expect && service ssh start && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \
    service ssh restart

# Copy setup script
COPY setup-node.sh /setup-node.sh

# Run setup script
RUN chmod +x /setup-node.sh && /setup-node.sh
CMD service ssh start && tail -f /dev/null