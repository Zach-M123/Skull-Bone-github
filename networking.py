#!/usr/sbin/python3
import socket

# basic code
local_hostname = socket.gethostname()
local_ipaddr = socket.gethostbyname(local_hostname)
print("Local Hostname: %s" %local_hostname + "\n" + "Local Ip addr: %s" %local_ipaddr)

# generate remote server ip address using gethkostbyname()
remote_server = "google.com"
remote_ipaddr = socket.gethostbyname(remote_server)
print("Remote Server: %s" %remote_server + '\n' + "Remote Ipaddress: %s" %remote_ipaddr)

