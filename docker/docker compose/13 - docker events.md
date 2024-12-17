# docker event
- monitor docker events => untuk melihat kerjadian apa saja yang terjadi di docker secara realtime, kita bisa menggunakan perintah docker events
  - contohnya kita bisa memonitoring kerjadian yang terjadi pada sebuah container dengan perintah
    ```bash
    docker events --filter 'container=nama'
    ```

## syntax
```yaml
docker events

docker events --filter 'container=nama'
```