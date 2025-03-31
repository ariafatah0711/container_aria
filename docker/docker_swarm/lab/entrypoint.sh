#!/bin/sh
sleep 10
TOKEN=$(docker -H tcp://swarm-manager:2376 swarm join-token -q worker)
docker swarm join --token $TOKEN swarm-manager:2377
exec "$@"