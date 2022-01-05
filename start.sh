#!/bin/bash

# 启动 nginx
/usr/sbin/nginx

# kids-ops
cd /feng-card/card/instance || exit
ln -f config_dev.py config.py
sed -i 's/127.0.0.1:27017/mongo:27017/g' config.py
sed -i 's/localhost/redis/g' config.py


cd /feng-card || exit
ln -f card/instance/settings_dev.py settings.py



cd /feng-card || exit
nohup python run.py 12345 >> /feng-card/feng-card.log 2>&1 &


/bin/bash