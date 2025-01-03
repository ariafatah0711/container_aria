## command
```bash
ansible <pattern> -m <module_name> -a "<module options>" -i <inventory_path>
ansible webservers -m service -a "name=httpd state=restarted" -i inventory
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