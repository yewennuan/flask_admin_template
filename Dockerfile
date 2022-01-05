FROM dipcode/centos7-python36
ADD . /feng-docker-build
RUN mkdir /feng-admin
WORKDIR /feng-card

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' >/etc/timezone  \
    && yum -y install epel-release nginx  \
    && cp /feng-docker-build/nginx.conf /etc/nginx/ \
    && cd /feng-docker-build \
    && pip install -r requirements.txt \




