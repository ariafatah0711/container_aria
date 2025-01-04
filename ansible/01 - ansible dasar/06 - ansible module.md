# ansible module
- di sebelumnya kita selalu menggunakan option ```-m ping```
- option yang kita gunakan tersebut namanya adalah module
- [module](https://docs.ansible.com/ansible/latest/module_plugin_guide/modules_intro.html#introduction-to-modules) => merupakan unit code untuk menjalankan suatu tugas tertentu
- ansible [memiliki banyak module](https://docs.ansible.com/ansible/latest/collections/index_module.html#index-of-all-modules) secara langsung seperti itu namanya adalah [ad hoc command](https://docs.ansible.com/ansible/latest/command_guide/intro_adhoc.html#introduction-to-ad-hoc-commands)
  - hal seperti ini cocok untuk menjalankan perintah-perintah yang tidak berulang

## module
```bash
ansible [pattern] -m [module] -a "[module options]"

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
```

## module argument / paramter
- setiap module dapat memiliki argument untuk kebutuhan dari module itu sendiri
- argument ini juga sering disebut sebagai paramter
- kebanyakan format dari argument / paramter adalah key-value pair,
  - meskipun ada beberapa yang tidak
- pemisah antar argument / paramter adalah spasi

### command
```bash
cat > data.txt << EOF
aria fatah anom
....
EOF

ansible node_docker -m command -a "date"
ansible node_docker -m copy -a "src=./data.txt dest=/tmp/" # src, dest => adalah argument/parameter
ansible node_docker -m command -a "cat /tmp/data.txt"
```