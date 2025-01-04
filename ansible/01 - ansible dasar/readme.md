- [list module](https://docs.ansible.com/ansible/latest/collections/index_module.html#index-of-all-modules)
- [module ad hoc command](https://docs.ansible.com/ansible/latest/command_guide/intro_adhoc.html#introduction-to-ad-hoc-commands)
- [ansible playbook](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html#ansible-playbooks)
- [ansible playbook vars](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html)
- [conditional](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_conditionals.html#conditionals)
- [tags](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tags.html#tags)
- [loops](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_loops.html)
- [vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html#protecting-sensitive-data-with-ansible-vault)

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
ansible-playbook <playbook.yaml> --check # only check the module not execute
ansible-playbook <playbook.yaml> --ask-vault-pass # with vault file encrypt
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
# forks => task pararel
[defaults]
inventory=./inventory/hosts
host_key_checking=False

forks = 30
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

### 02 - playbook-webserver.yaml
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
        enabled: true
```

## 02 - playbook vars
```yaml
# list
region:
  - northeast
  - southeast
  - midwest

## mamnggil list
region: "{{ region[0] }}"

# dictionary
foo:
  field1: one
  field2: two

## memanggil dictionary
{{ foo['field1'] }}
{{ foo.field1 }}

# merged list
merged_list: "{{ list1 + list2 }}"

# merged dict
merged_dict: "{{ dict1 | ansible.builtin.combine(dict2) }}"
```

### 03 - playbook_webserver_vars
```yaml
---
- name: Playbook setup web server
  hosts: node_docker
  become: true
  vars: # mendefinisikan variable
    user_app: ansibleweb
  tasks:
    - name: Install nginx
      ansible.builtin.apt:
        name: nginx
        state: present
    - name: Buat user {{ user_app }}
      ansible.builtin.user:
        name: "{{ user_app }}"
        password: belajaransible
        shell: /bin/bash
    - name: Copy file html
      ansible.builtin.copy:
        src: ./web/
        dest: /var/www/html/
        mode: '644'
        owner: "{{ user_app }}"
        group: "{{ user_app }}"
```

## 03 - playbook conditional
```bash
tasks:
  - name: Configure SELinux to start mysql on any port
    ansible.posix.seboolean:
      name: mysql_connect_any
      state: true
      persistent: true
    when: ansible_selinux.status == "enabled"
```

### 04 - playbook-webserver_when.yaml
```yaml
---
- name: Playbook setup web server
  hosts: node_docker
  become: true
  # gather_facts: true # defaultnya memang true
  vars: # mendefinisikan variable
    user_app: ansibleweb
  tasks:

    ## Install nginx
    - name: Install nginx (Debian)
      ansible.builtin.apt:
        name: nginx
        state: present
      when:
        - ansible_os_family == "Debian"
        - ansible_processor_cores >= 1 or ansible_memory_mb.real.total >= 512
    - name: Install nginx (Alpine)
      community.general.apk:
        name: nginx
        state: present
      when:
        - ansible_os_family == "Alpine"
        - ansible_processor_cores >= 1 or ansible_memory_mb.real.total >= 512

    ## Buat user
    - name: Buat user (Debian) {{ user_app }}
      ansible.builtin.user:
        name: "{{ user_app }}"
        password: belajaransible
        shell: /bin/bash
      when:
        - ansible_os_family == "Debian"
    - name: Buat user (Alpine) {{ user_app }}
      ansible.builtin.user:
        name: "{{ user_app }}"
        password: belajaransible
        shell: /bin/sh
      when:
        - ansible_os_family == "Alpine"

    ## Copy file html
    - name: Copy file html (Debian)
      ansible.builtin.copy:
        src: ./web/
        dest: /var/www/html/
        mode: '604'
        owner: "{{ user_app }}"
        group: "{{ user_app }}"
      when:
        - ansible_os_family == "Debian"
    - name: Copy file html (Alpine)
      ansible.builtin.copy:
        src: ./web/
        dest: /usr/share/nginx/html
        mode: '604'
        owner: "{{ user_app }}"
        group: "{{ user_app }}"
      when:
        - ansible_os_family == "Alpine"
```

## 03 - playbook tags
```yaml
tasks:
- name: Install the servers
  ansible.builtin.yum:
    name:
    - httpd
    - memcached
    state: present
  tags:
  - packages
  - webservers

- name: Configure the service
  ansible.builtin.template:
    src: templates/src.j2
    dest: /etc/foo.conf
  tags:
  - configuration
```

### 05 - playbook-webserver_tags.yaml
```yaml
---
- name: Playbook setup web server
  hosts: node_docker
  become: true
  gather_facts: true # defaultnya memang true
  vars: # mendefinisikan variable
    user_app: ansibleweb
  tasks:

    ## Install nginx
    - name: Install nginx (Debian)
      ansible.builtin.apt:
        name: nginx
        state: present
      when:
        - ansible_os_family == "Debian"
        - ansible_processor_cores >= 1 or ansible_memory_mb.real.total >= 512
      tags:
        - install
    - name: Install nginx (Alpine)
      community.general.apk:
        name: nginx
        state: present
      when:
        - ansible_os_family == "Alpine"
        - ansible_processor_cores >= 1 or ansible_memory_mb.real.total >= 512
      tags:
        - install

    ## Buat user
    - name: Buat user (Debian) {{ user_app }}
      ansible.builtin.user:
        name: "{{ user_app }}"
        password: belajaransible
        shell: /bin/bash
      when:
        - ansible_os_family == "Debian"
      tags:
        - setup
        - create_user
    - name: Buat user (Alpine) {{ user_app }}
      ansible.builtin.user:
        name: "{{ user_app }}"
        password: belajaransible
        shell: /bin/sh
      when:
        - ansible_os_family == "Alpine"
      tags:
        - setup
        - create_user

    ## Copy file html
    - name: Copy file html (Debian)
      ansible.builtin.copy:
        src: ./web/
        dest: /var/www/html/
        mode: '604'
        owner: "{{ user_app }}"
        group: "{{ user_app }}"
      when:
        - ansible_os_family == "Debian"
      tags:
        - setup
        - copy_file
    - name: Copy file html (Alpine)
      ansible.builtin.copy:
        src: ./web/
        dest: /usr/share/nginx/html
        mode: '604'
        owner: "{{ user_app }}"
        group: "{{ user_app }}"
      when:
        - ansible_os_family == "Alpine"
      tags:
        - setup
        - copy_file
```

## 04 - playbook loops
```yaml
# 1 with_items
with_items:
  - 1
  - [2,3]
  - 4

loop: "{{ [1, [2, 3], 4] | flatten(1) }}"
loop: "{{ lookup('fileglob', '*.txt', wantlist=True) }}"
with_fileglob: '*.txt'

# 2 loop
- name: Add several users
  ansible.builtin.user:
    name: "{{ item }}"
    state: present
    groups: "wheel"
  loop:
     - testuser1
     - testuser2

# 3 loop
- name: Add several users
  ansible.builtin.user:
    name: "{{ item.name }}"
    state: present
    groups: "{{ item.groups }}"
  loop:
    - { name: 'testuser1', groups: 'wheel' }
    - { name: 'testuser2', groups: 'root' }

# 4 with list
- name: with_list
  ansible.builtin.debug:
    msg: "{{ item }}"
  with_list:
    - one
    - two
``` 

### 06 - playbook-php_loops.yaml
```yaml
---
- name: Playbook setup PHP
  hosts: node_docker
  become: true
  gather_facts: true # defaultnya memang true
  vars:
    # taget_php_version: 8.2
    taget_php_version: Null
  tasks:
    - name: Add repository for PHP
      ansible.builtin.apt_repository:
        repo: 'ppa:ondrej/php'
        state: present
      tags:
        - prepare
        - add_repo_php

    - name: Update repo
      ansible.builtin.apt:
        update_cache: true
      tags: prepare

    - name: Install php {{ taget_php_version }}
      ansible.builtin.apt:
        name: "{{ item }}"
        state: present
      with_items:
        - php{{ taget_php_version }}
        - php{{ taget_php_version }}-cli
        - php{{ taget_php_version }}-common
        - php{{ taget_php_version }}-imap
        - php{{ taget_php_version }}-redis
        - php{{ taget_php_version }}-xml
        - php{{ taget_php_version }}-zip
        - php{{ taget_php_version }}-mbstring
        - php{{ taget_php_version }}-curl
        - php{{ taget_php_version }}-gd
        - php{{ taget_php_version }}-bcmath
        - php{{ taget_php_version }}-gmp
        - php{{ taget_php_version }}-mysqli
      tags:
        - install
```

# ansible vault
## create encrypt file
```yaml
ansible-vault create <nama_file>
ansible-vault create secret-user.yaml
# New Vault password: # 123 (example)
# Confirm New Vault password: # 123 (example)

# text editor =======
user_pass: pass123
#===================

cat secret-user.yaml
# $ANSIBLE_VAULT;1.1;AES256
# 38303762303065326161333033633365613733666232353235626365346465663963613463653233...
```

## view / edit encrypt file
```yaml
ansible-vault edit <nama_file>
ansible-vault view <nama_file>

ansible-vault view secret-user.yaml
# Vault password: 123
# user_pass: pass123

ansible-vault edit secret-user.yaml
# Vault password: 123
```

### 07 - playbook-vault.yaml
```yaml
- name: Playbook buat user baru
  hosts: node_docker
  become: true
  gather_facts: true # defaultnya memang true
  vars: # mendefinisikan variable
    user_app: user01
  tasks:

    - name: Parsing variable dari secret file
      ansible.builtin.include_vars:
        file: secret-user.yaml

    - name: Add new user
      ansible.builtin.user:
        name: "{{ user_app }}"
        # password: belajaransible # gak secure kita ganti pake Ansible Vault

        password: "{{ user_pass | password_hash('sha512') }}" # ambil value dari variable lalu lakukan hash
        shell: /bin/bash
      when:
        - ansible_os_family == "Debian"
```