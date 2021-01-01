#!/usr/sbin/python3

#using docker to contain asterisk 
echo $(sudo docker pull andrius/asterisk:lts)

# running docker image 
echo $(sudo docker run -h "asterisk" -p 5060:5060 -it /bin/bash )
