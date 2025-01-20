# example
```
tasks:
  - name: run command on remote devices
    routeros_command:
      commands: /system routerboard print

  - name: run command and check to see if output contains routeros
    routeros_command:
      commands: /system resource print
      wait_for: result[0] contains MikroTik

  - name: run multiple commands on remote nodes
    routeros_command:
      commands:
        - /system routerboard print
        - /system identity print

  - name: run multiple commands and evaluate the output
    routeros_command:
      commands:
        - /system routerboard print
        - /interface ethernet print
      wait_for:
        - result[0] contains x86
```

ansible rb1 -m ping