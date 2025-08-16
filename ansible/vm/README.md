# lab ansible 2 (vagrant)
## setup
```bash
vagrant up
```

## use
```bash
ansible -i hosts clients -m ping
ansible -i hosts clients -a whoami
```
