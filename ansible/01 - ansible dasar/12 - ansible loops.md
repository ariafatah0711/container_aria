# ansible loops
- terkadang ada task di dalam playbook yang sifatnya redundan atau duplikat
  - hanya beda sedikit di bagian tertentu saja
- contohnya kita ingin menginstall php8.2, php8.2-cli, dan php-8.2-curl
  - secara teori seharusnya kita membuat 3 task untuk menginstall package tersebut
- agar konfigurasi yaml kita lebih rapi, sebisa mungkin kita menghindari task yang redundan atau duplikat 
  - caranya adalah kita dapat menggunakan [loops](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_loops.html) di ansible

## loops vs with
- umumnya ketika kita menggunakan loops, kita dapat menggunakan element **loop:** atau **with_<lookup>:** di file playbook
- secara fungsi kedua element tersebut sama, hal mendasar yang membedakanya adalah
  - **loop:** => untuk sesuatu yang static
  - **with_<lookup>:** => untuk sesuatu yang dinamis
- tapi hal tersebut masuk ke materi advance
  - kita akan menggunakan materi **with_<lookup>:** untuk di materi ini

## template
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

## example
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

## command
```bash
ansible-playbook 06\ -\ playbook-php_loops.yaml

# if error in add repo
ansible-playbook 06\ -\ playbook-php_loops.yaml --skip-tags add_repo_php
```