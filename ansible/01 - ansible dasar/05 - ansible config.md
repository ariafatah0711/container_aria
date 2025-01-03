# ansible config
- [ansible config](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings) => digunakan untuk mengkonfigurasi ansible saat kita menjalankan perintah-perintah ansible
- sama halnya dengan inventory ansible config ini memiliki hirarki dalam pembacaanya
- ansible config ditulis dengan format INI dengan nama ansible.cfg
- penulisan konfigurasi di ansible config dikelompokan dalam sebuah section

## urutan pembacaan file
- ANSIBLE_CONFIG (environment variable if set)
- ansible.cfg (in the current directory)
- ~/.ansible.cfg (in the home directory)
- /etc/ansible/ansible.cfg

- format ini
  ```INI
  section:     [defaults]
  key:          key1=value
                key2=value
  ```

## membuat ansibe config
- di command yang kita gunakan sebelumnya kita selalu mendifinisikan option -i <file_inventory> saat memanggil file inventory
  - kita dapat sederhanakan hal ini dengan menambahkan key_inventory di section defaults
- satu hal lagi yang cukup penting adalah menambahkan host_key_checking 
  - yang fungsinya adalah menghindari host key checking saat pertama kali connect ke server baru
- sekarang kita cukup menggunakan command ```ansible node_docker -m ping```

```bash
cat > ansible.cfg << EOF 
[defaults]
inventory=./inventory/04 - inventory_range
host_key_checking=False
EOF

ansible node_docker -m ping
```

dan jika tidak berhasil coba export env terlebih dahulu

```bash
export ANSIBLE_CONFIG=./ansible.cfg
```

```bash
cat > ~/ansible.cfg << EOF
[defaults]
inventory=/ansible_aria/ansible_lab/hosts
host_key_checking=False
EOF

ansible node1 -m ping
# node1 | SUCCESS => {}
```