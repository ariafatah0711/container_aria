- [list module](https://docs.ansible.com/ansible/latest/collections/index_module.html#index-of-all-modules)
- [module ad hoc command](https://docs.ansible.com/ansible/latest/command_guide/intro_adhoc.html#introduction-to-ad-hoc-commands)
- [ansible playbook](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html#ansible-playbooks)

## install
```bash
# ansible
## linux
sudo apt install pipx

pip3 install ansible
## or
pipx install ansible-core
## or
pipx install --include-deps ansible

# ansible lint
pip3 install ansible-lint
```

## command
```bash
ansible <pattern> -m <module_name> -a "<module options>" -i <inventory_path>
ansible webservers -m service -a "name=httpd state=restarted" -i inventory

ansible [pattern] -m [module] -a "[module options]"

ansible-playbook <playbook.yaml>
```

## inventory
```bash
srv1 ansible_user=admin ansible_ssh_private_key_file=~/.ssh/id_rsa
srv2 ansible_user=madun

#==========================================================
# group
[node_docker]
node1
node2
node3

#==========================================================
# var
[node_docker:vars]
ansible_user=root
ansible_ssh_private_key_file=/ssh_node/private.key

#==========================================================
# range
[webservers]
www[01:50].example.com
# www01.example.com, www02.example.com

[databases]
db-[a:f].example.com

#==========================================================
# 
```

## config
```INI
# inventory and host_key_checking
[defaults]
inventory=./inventory/hosts
host_key_checking=False

#==========================================================
# 2
```

## module
```bash
# module
ansible.builtin.ping # Try to connect to host, verify a usable python and return pong on success
ansible.builtin.command # Execute commands on targets
ansible.builtin.copy # Copy files to remote locations
ansible.builtin.package # Generic OS package manager
ansible.builtin.package_facts # Package information as facts
ansible.builtin.pause # Pause playbook execution
ansible.builtin.pip # Manages Python library dependencies
ansible.builtin.raw # Executes a low-down and dirty command
ansible.builtin.service # Manage services
ansible.builtin.script # Runs a local script on a remote node after transferring it
ansible.builtin.reboot # Reboot a machine

# rebort server
ansible atlanta -a "/sbin/reboot"
ansible atlanta -a "/sbin/reboot" -f 10 -u username
ansible atlanta -a "/sbin/reboot" -f 10 -u username --become [--ask-become-pass]

# manage file
ansible atlanta -m ansible.builtin.copy -a "src=/etc/hosts dest=/tmp/hosts"
ansible webservers -m ansible.builtin.file -a "dest=/srv/foo/b.txt mode=600 owner=mdehaan group=mdehaan"
ansible webservers -m ansible.builtin.file -a "dest=/path/to/c mode=755 owner=mdehaan group=mdehaan state=directory" # mkdir -p
ansible webservers -m ansible.builtin.file -a "dest=/path/to/c state=absent" # delete

# Managing packages
ansible webservers -m ansible.builtin.yum -a "name=acme state=present"
...

# Managing users and groups
ansible all -m ansible.builtin.user -a "name=foo password=<encrypted password here>"
ansible all -m ansible.builtin.user -a "name=foo state=absent" # remove user

# Managing services
ansible webservers -m ansible.builtin.service -a "name=httpd state=started"
ansible webservers -m ansible.builtin.service -a "name=httpd state=restarted"
ansible webservers -m ansible.builtin.service -a "name=httpd state=stopped"

# Gathering facts =>  discovered variables about a system
ansible all -m ansible.builtin.setup

# Check mode => only check not make any changes to remote systems.
ansible all -m copy -a "content=foo dest=/root/bar.txt" -C
```

### module example
```bash
cat > data.txt << EOF
aria fatah anom
....
EOF

ansible node_docker -m command -a "date"
ansible node_docker -m copy -a "src=./data.txt dest=/tmp/" # src, dest => adalah argument/parameter
ansible node_docker -m command -a "cat /tmp/data.txt"
```

## playbook
### 01 - playbook-webserver.yaml
```yaml
---
- name: Playbook setup web server
  hosts: node_docker
  # become: yes
  # become_method: sudo
  tasks:
    - name: Update repository
      ansible.builtin.apt:
        update_cache: true
    - name: Install nginx
      ansible.builtin.apt:
        name: nginx
        state: latest
    - name: Copy file html
      ansible.builtin.copy:
        src: ./web/
        dest: /var/www/html
    - name: Start nginx
      ansible.builtin.service:
        name: nginx
        state: "started"
        enabled: True
```

### 01 - playbook-webserver.yaml
```yaml
---
- name: Playbook setup web server
  hosts: node_docker
  tasks:
    - name: Update repository
      ansible.builtin.apt:
        update_cache: true
    - name: Install nginx
      ansible.builtin.apt:
        name: nginx
        state: present
    - name: Copy file html
      ansible.builtin.copy:
        src: ./web/
        dest: /var/www/html
        mode: '644'
    - name: Start ngix
      ansible.builtin.sysvinit:
        name: nginx
        state: started
```