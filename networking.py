#!/usr/sbin/python3
import socket

# create a fucntion() for Local machine info
def local_info():
    local_host = socket.gethostname()
    local_ipaddr = socket.gethostbyname(local_host)
    print("Local Hostname: %s" %local_host + '\n' + "Local Ip addr: %s" %local_ipaddr)

if __name__ == "__main__":
    local_info()

# create a function() for remote server info
def server_machine():
    remote_server = "google.com"
    remote_ipaddr = socket.gethostbyname(remote_server)
    print("Google Server: %s" %remote_server + '\n' + "IP address: %s" %remote_ipaddr)

if __name__ == "__main__":
    server_machine()

# create a function() for remote using notion of try and except
def get_remote_server():
    remote_server = "cisco.com"
    try:
        print("Cisco Server: %s" %remote_server + '\n' + "IP address: %s" %socket.gethostbyname(remote_server))
    except socket.error + err_msg:
        print("%s: %s" %remote_server + err_msg)

if __name__ == "__main__":
    get_remote_server()

