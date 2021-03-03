#!/usr/sbin/python3
import socket

#getting ip address of host machine by name
def print_machine_info():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    print("Hostname: %s" %hostname + "\n" + "IP address: %s" %ip_addr)

if __name__ == '__main__':
    print_machine_info()

#getting remote server ip address by name
def server_machine_info():
    server = "google.com"
    ip_addr = socket.gethostbyname(server)
    print("Name Server: %s" %server + "\n" + "Ip address: %s" %ip_addr)

if __name__ == '__main__':
    server_machine_info()


