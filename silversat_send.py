import socket, sys

# Computer running the sender must be on the same subnet as the receiver
# If both sender and receiver are on the same computer, 127.0.0.1 will work.
UDP_IP = '127.0.0.1'

# otherwise, provide the IP address of the reciever. 
# UDP_IP = '192.168.0.100'

# Do not change this!
UDP_PORT = 19614

# the UDP_input function.  It listens for commands coming in from the Internet
#  connection. It will return with no data if it does not receive anything in
#   1 second

def UDP_input(recPort = UDP_PORT):
        sock = socket.socket(socket.AF_INET, # listen on the Internet connection
                     socket.SOCK_DGRAM) #   for UDP packets
        sock.bind((UDP_IP, UDP_PORT))
        sock.settimeout(1)   # this sets the timeout to 1 second
        try:
          data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
          data = data.decode("utf-8")
        except socket.timeout:
          data = None
          addr = None
        sock.close()
        return(data,addr)
    # UDP_send.py - sends text to a specific IP address and UDP port
# last update - 4/12/2018 DJC

import socket

# UDP_IP = socket.gethostbyname(socket.gethostname())

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

runstate = True

while runstate:
    msg = input("command - ")
    print ("Sending %s to %s:%s"%(msg,UDP_IP, UDP_PORT))
    sock.sendto(msg.encode('utf-8'), (UDP_IP, UDP_PORT))
    if msg =='q':
        runstate=False
