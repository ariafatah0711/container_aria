# ansible inventory
- seperti yang kita bahas di awal ansible mengetahui server mana yang yang harus di managed dengan menggunakan file inventory
- ansible mendukung banyak sekali format penulisan file inventory,
  - namun umumnya yang sering digunakan adalah format INI dan yaml
- dalam materi ini kita akan menggunakan format INI dalam membuat file inventory
- umumnya ketika membuat file inventory, nama filenya adalah ```hosts atau inventory```
  - walaupun memang kita bisa terserah penamaanya

## plugin pada inventory
### 1
```INI
[inventory]
enable_plugins = host_list, script, auto, yaml, ini, toml
```

### 2
```INI
[inventory]
enable_plugins = host_list, script, auto, yaml, ini, toml, namespace.collection_name.inventory_plugin_name
```

### 3
```INI
[inventory]
enable_plugins = host_list, script, auto, yaml, ini, toml, my_plugin
```

## membuat ansible inventory
- siapkan satu folder untuk praktik ini
- silakan buat file dengan nama inventory, lalu masukan list ip atau domain server di file tersebut
- selanjutnya coba jalankan command berikut ini
  ```bash
  ansible <IP_SERVER> -m ping
  ```
- seharusnya ketika menjalankan perintah tersebut akan ada warning / error message seperti gambar dibawah

```bash
cat > inventory << EOF
node1 # ip 1
node2 # ip 
EOF

ansible node1 -m ping
# [WARNING]: No inventory was parsed, only implicit localhost is available
# [WARNING]: provided hosts list is empty, only localhost is available. Note that the
# implicit localhost does not match 'all'
# [WARNING]: Could not match supplied host pattern, ignoring: node1
```

## hirarki pembacaan inventory
- error sebelumnya dikarenakan secara default ansible akan membaca file inventory
  - yang berada di ```/etc/ansible/hosts``` sehingga file yang kita buat sebelumnya tidak terbaca
- agar file inventory yang kita buat terbaca, kita dapat menambahkan option -i <file_inventory>
- seharusnya kita berhasil membaca file inventory,
  - namun kita akan mendapatkan error yang menunjukan bahwa ansible tidak dapat konek ke server yang kita definisikan

```bash
ansible node1 -i inventory -m ping
node1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

### menggunakan ssh key di inventory
- jika terdapat error permission denied public key itu terjadi 
  - karena ansible sudah berhasil terhubung ke server namun public key atau passwordnya salah
- sebelumnya kita sudah membuat ssh key untuk server kita berhasil mencopykan / mengirimkan public key ke server
- agar kita dapat menggunakan private key untuk auntentikasi, 
  - kita dapat menambahkan parameter ```ansible_ssh_private_key_file``` dan ```ansible_user``` di inventory

```INI
node1 ansible_user=root ansible_ssh_private_key_file=~/.ssh/id_rsa
node2 ansible_user=root ansible_ssh_private_key_file=/ssh_node2/private.key
```

- seharusnya ketika sudah mendefinisikan ssh_private_key seharusnya sudah berhasil

# membuat group name dan groups variables
- didalam satu file inventory kita bisa memiliki banyak list IP/Domain dari server kita
  - agar server server tersebut dapat terorganisir dengan baik kita dapat [mengelompokanya ke sebuah group](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#inventory-basics-formats-hosts-and-groups)
- bahkan paramater yang kita buat sebelumnya itu "sangat tidak clean"
  - karena kita mendefinisikan sesuatu yang sama secara berulang
  - untuk mengatasi masalah ini kita membuat group [variables](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#assigning-a-variable-to-many-machines-group-variables)
- ketika kita menggunakan command yang sama seperti sebelumnya hasilnya akan sama tapi konfigurasi kita jauh lebih bersih

### ex 1
```INI
mail.example.com

[webservers]
foo.example.com
bar.example.com

[dbservers]
one.example.com
two.example.com
three.example.com
```

### ex 2
```INI
[atlanta]
host1
host2

[atlanta:vars]
ntp_server=ntp.atlanta.example.com
proxy=proxy.atlanta.example.com
```

## example
```INI
[node_docker]
node1
node2
node3

[node_docker:vars]
ansible_user=root
ansible_ssh_private_key_file=/ssh_node/private.key
```

### run
```bash
ansible node1 -i 03\ -\ inventory_group_var -m ping
# node1 | SUCCESS => {}
```

## pattern
- command yang sebelumnya kita gunakan sebenernya formatnya adalah seperti ini
  ```ansible <pattern> <options>```
- -m atau -i adalah options
- [pattern](https://docs.ansible.com/ansible/latest/inventory_guide/intro_patterns.html#patterns-targeting-hosts-and-groups) => merupakan target hosts / group yang di inginkan 
- ada beberapa penulisan [pattern](https://docs.ansible.com/ansible/latest/inventory_guide/intro_patterns.html#common-patterns)

```bash
ansible <pattern> -m <module_name> -a "<module options>"

ansible node_docker -i 03\ -\ inventory_group_var -m ping
# node1 | SUCCESS => {}
# node2 | SUCCESS => {}
# node3 | SUCCESS => {}
```