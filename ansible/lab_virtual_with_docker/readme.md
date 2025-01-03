```bash
docker compose up -d

docker exec -it ansible-controller bash -c "ssh-copy-id root@node11"
docker exec -it ansible-controller bash -c "ssh-copy-id root@node12"

docker compose down
```