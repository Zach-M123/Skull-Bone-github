#!/usr/sbin/python3
import socket

# basic code
local_hostname = socket.gethostname()
local_ipaddr = socket.gethostbyname(local_hostname)
print("Local Hostname: %s" %local_hostname + "\n" + "Local Ip addr: %s" %local_ipaddr)

