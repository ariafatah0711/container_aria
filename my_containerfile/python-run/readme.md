# run
```bash
docker build . -t pyton-run

docker run python-runner -c  'print("hello")'
# => hello

docker run python-runner --version
# => Python 3.11.2

docker run -p 8000:8000 python-runner -m http.server
# => 172.17.0.1 - - [17/Dec/2024 16:19:36] "GET / HTTP/1.1" 200 -

docker run -p 8000:8000 python-runner a.py
```