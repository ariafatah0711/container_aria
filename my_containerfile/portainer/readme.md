# Portainer
- Portainer adalah GUI berbasis web untuk mengelola Docker containers, images, volumes, dan networks.

## run
```bash
docker run -d -p 9091:9000 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer-ce

# remove
docker rm -f portainer
```