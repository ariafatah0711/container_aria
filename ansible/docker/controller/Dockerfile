FROM ubuntu:20.04

# Install dependencies
RUN apt update && apt install -y python3 python3-pip sshpass openssh-client nmap curl vim && \
    pip install ansible && \
    ssh-keygen -t rsa -b 2048 -f /root/.ssh/id_rsa -q -N ""

# Copy setup script
COPY setup-controller.sh /setup-controller.sh

# Run setup script
RUN chmod +x /setup-controller.sh && /setup-controller.sh
