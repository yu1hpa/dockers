```
$ docker build -t crypto-docker .
$ docker run -it --rm -v `pwd`:/usr/src crypto-docker /bin/bash
root@91f3ff0a5a67: cd /usr/src
root@91f3ff0a5a67:/usr/src# python3 sample.py
```
