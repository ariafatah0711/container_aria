# playbook variables
- terkadang ada beberapa bagian konfigurasi yang merujuk hal sama
  - contohnya task 1 kita membuat folder AAA, dan task 2 mencopy kan sesuatu ke folder AAA
  - daripada kita mendefinisikan nama folder AAA berulang di task 1 dan 2
  - kita dapat membuatnya sebagai [variables](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html)
    - agar nantinya cukup mendefinisikan 1 kali saja

## example
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

## run
```bash
ansible-playbook 03\ -\ playbook-wevserver_vars.yaml

ssh -i /ssh_node/private.key node1 ls -la /var/www/html/index.html
# -rw-r--r-- 1 ansibleweb ansibleweb 435 Jan  4 06:33 /var/www/html/index.html

ansible node_docker -m command -a "ls -la /var/www/html/index.html"
# node1 | CHANGED | rc=0 >>
# -rw-r--r-- 1 ansibleweb ansibleweb 435 Jan  4 06:33 /var/www/html/index.html
# node2 | CHANGED | rc=0 >>
# -rw-r--r-- 1 ansibleweb ansibleweb 435 Jan  4 06:33 /var/www/html/index.html
# node3 | CHANGED | rc=0 >>
# -rw-r--r-- 1 ansibleweb ansibleweb 435 Jan  4 06:33 /var/www/html/index.html
```

# list
- karena playbook menggunakan format yaml
  - sebenernya kita dapat mendefinisikan variable dalam bentuk boolean, list, dictionary jika dibutuhkan

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