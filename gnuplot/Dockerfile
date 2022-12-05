FROM ubuntu:20.04

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && \
    apt install -y gnuplot && \
    apt install -y build-essential && \
    rm -rf /var/lib/apt/lists/*
