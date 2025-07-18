#!/bin/bash

sudo yum install java-17
sudo yum install docker java-17 maven git -y
sudo systemctl start docker

docker pull docker pull akhilanilkumar10/java-web-app
docker run docker pull -p 8080:8080 akhilanilkumar10/java-web-app