import socket, sys

UDP_IP = '192.168.0.105'
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
UDP_IP = '192.168.0.105'  # fill in the receiver's IP address here.
UDP_PORT = 19614

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

runstate = True

while runstate:
    msg = input("command - ")
    sock.sendto(msg.encode('utf-8'), (UDP_IP, UDP_PORT))
    if msg =='q':
        runstate=False

        if __name__ == "__main__":

# THE MAIN PROGRAM STARTS HERE. 

            print("Listening on port %s, socket %4.0f" % (UDP_IP,UDP_PORT))

            runLoop = True
            while runLoop:
                data, addr = UDP_input();

  # If the program received something, print it. If not, print a dot.
  
            if data:    
                    print ("\nreceived command from %s: %s \n" % (addr,data))
            else:
                    sys.stdout.write('.')
                    sys.stdout.flush()
  
  #  This is where any other commands would go.  Each command would consist of
  #    an 'if' statement (if data == 'something':), followed by the action the
  #    program should take.
  
  # if the program received a 'q', quit

            if data == 'q':
                    runLoop = False
            if data == 'j':
                print('Hi')
                
            if data == 'ok':
                print('Roger that')





