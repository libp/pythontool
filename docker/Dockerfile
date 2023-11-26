FROM alpine:3.18

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories

RUN apk update ;\
    apk add --no-cache ca-certificates ;\
    apk add --no-cache curl bash tree tzdata busybox-extras;\
    cp -rf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN apk add --no-cache python3 py3-pip

CMD tail -f /dev/null
WORKDIR /opt/
EXPOSE 80

