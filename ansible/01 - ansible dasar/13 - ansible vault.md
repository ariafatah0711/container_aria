# ansible vault
- di beberapa file playbook sebelumnya kita gunakan
  - sebelumnya ada task yang tugasnya membuat user-baru
- dan jika kita lihat disitu ada paramter password yang dimana itu
  - merupakan password dari user yang akan dibuat nantinya
- menulis informasi yang sensitif secara plain text bukanlah hal yang bagus
  - untuk memproteksi hal yang sifatnya sensitif kita dapat menggunakan [vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html#protecting-sensitive-data-with-ansible-vault) di ansible
- dengan kita menggunakan vault maka informasi yang sifatnya sensitif akan di enkripsi sehingga jauh lebih aman

## membuat encrypt file
- kita perlu membuat encrypted file terlebih dahulu untuk menyimpan informasi sensitif sebelumnya
- ketika membuat encrypted files, kita akan diminta untuk memasukan password
  - yang dimana password tersebut digunakan sebagai kunci untuk encrypt dan decrypt
- setelah memasukan password akan terbuka di teks editor
  - yang dimana kita bisa memasukan informasi sensitif disitu
  - contohnya dalam praktik ini kita akan membuat variable yang nantinya dapat dipanggil di playbook
- ketika kita save maka akan terbuat file dengan nama yang kita definisikan
  - dan isi kontenya adalah semacam angka acak

### command
```bash
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

## parsing variable file
- setelah kita mendefinisikan variable di encrypted file yang kita buat sebelumnya
  - selanjutnya adalah memanggil variable tersebut di file playbook kita
- agar variable dapat digunakan di playbook, kita perlu melakukan parsing variable tersebut
  - dengan module **ansible.builtin.include_vars**
- dan kita juga bisa gunakan paramter ini ```--ask-vault-pass``` saat kita menggunakan ansible-playbook

## example
```yaml
---
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

## command
```bash
ansible-playbook 07\ -\ playbook-vault.yaml # gagal
ansible-playbook 07\ -\ playbook-vault.yaml --ask-vault-pass
# Vault password: 123

ssh -i /ssh_node/private.key node1
su user01
# Password: pass123
```

## mengedit dan melihat file encrypt file
- ada kalanya kita perlu mengedit atau melihat isi dari file yang enkripsi
  - caranya adalah menggunakan ansible-vault **view/edit**

```bash
ansible-vault edit <nama_file>
ansible-vault view <nama_file>

ansible-vault view secret-user.yaml
# Vault password: 123
# user_pass: pass123

ansible-vault edit secret-user.yaml
# Vault password: 123
```