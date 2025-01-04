# ansible conditionals
- terkadang setiap task / tugas yang kita definisikan di playbook harus berjalan di kondisi tertentu
  - contohnya ketika menginstall nginx di debian kita menggunakan module ```ansbile.builtin.apt```
  - tapi untuk alpine menggunakan community.general.apk
- ansible memiliki kemampuan untuk membuat semacam if-else di pemograman yang bernama [conditional](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_conditionals.html#conditionals)
- sama seperti if conditionals pada umumnya kita dapat menggunakan operasi logical operator
  - seperti AND, OR, NOT, dan comperision operator (>=, <=, ==)

# ansible facts
- secara default saat kita menjalankan playbook
  - ansible akan mengambil informasi dari server tujuan terlebih dahulu sebelum menjalankan task yang ada
- informasi-informasi yang diambil dan akan disimpan dalam sebuah variable
  - variable-variable yang dibuat tersebut dinamakan facts
- jika kita ingin mengecek facts secara manual untuk melihat informasi anda bisa gunakan perintatah
  ```ansible <pattern/host> -m ansible.builtin.setup```
- atau menggunakan yaml akan jadi seperti ini
  ```gather_facts: true # defaultnya memang true```

## variblae in gather_facts
```bash
ansible node_docker -m setup
ansible node_docker -m setup | grep family
#         "ansible_os_family": "Debian",

ansible node_docker -m setup | grep processor_core
#        "ansible_processor_cores": 6,

ansible node_docker -m setup | less
# /memory
# "ansible_memory_mb": {
#             "real": {
#                "total": 7563
#            },....},
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