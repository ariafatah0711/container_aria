# tags
- terkadang kita hanya ingin menjalankan task-task tertentu yang ada di suatu playbook
- contohnya misal task 1 menginstall web server dan task 2 mencopy file html
  - kita sudah tahu bahwa web server sudah terinstall di semua host,
  - jadi kita hanya ingin menjalankan task 2 untuk menghemat waktu
- untuk mengatasi masalah ini kita dapat menggunakan [tags](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tags.html#tags)
  - nantinya setiap task bisa memiliki beberapa tag

## template
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

## example
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

- untuk menjalankan task tertentu kita dapat menggunakan ```--tags <tag1>,<tag2>```
- untuk menjalankan task selain yang ditentukan dapat menggunakan option ```--skip-tags <tag1>,<tag2>```

## command
```bash
ansible-playbook <nama_file.yaml> --check --tags copy_file
ansible-playbook <nama_file.yaml> --tags copy_file,create_user
ansible-playbook <nama_file.yaml> --skip-tags install

ansible-playbook 05\ -\ playbook_webserver_tags.yaml --tags copy_file
ansible-playbook 05\ -\ playbook_webserver_tags.yaml --tags copy_file,create_user
```