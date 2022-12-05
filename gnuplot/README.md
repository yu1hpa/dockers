```
docker build -t gnuplot .
```

macOS
```
docker run -it --rm -e DISPLAY=`hostname`:0 --net host -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/root/.Xauthority -v `pwd`:/usr/src gnuplot
```
