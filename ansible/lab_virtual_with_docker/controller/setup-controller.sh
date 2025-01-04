#!/bin/bash

# Generate SSH key for root user
if [ -f /root/.ssh/id_rsa ]; then
    rm -f /root/.ssh/id_rsa
fi
ssh-keygen -t rsa -f /root/.ssh/id_rsa -q -N ""

echo "export ANSIBLE_CONFIG=./ansible.cfg" >> ~/.bashrc