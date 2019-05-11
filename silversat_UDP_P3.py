#!/usr/bin/python

import socket, sys
import RPi.GPIO as GPIO
import time
from gnc import GNC

UDP_IP = '192.168.0.105' # the ip address of the recieving computer
UDP_PORT = 19614

LIGHT = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT, GPIO.OUT)

mygnc = GNC()

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

if __name__ == "__main__":

# THE MAIN PROGRAM STARTS HERE. 

    print("Listening on port %s, socket %4.0f" % (UDP_IP,UDP_PORT))

    runLoop = True
    while runLoop:
            data, addr = UDP_input();
            #print(data,addr)
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
            if data == 'j': # code so that when i receive a j, print hi
                print('Hi')
            if data == 'Zuri':
                print('yummy tummy')
            if data == 'on':
                GPIO.output(LIGHT, True)
            if data == 'off':
                GPIO.output(LIGHT, False)
            if data == 'head':
                print (mygnc.orientation())
            if data == 'position':
                if mygnc.ready():
                        print (mygnc.position())
                else:
                        print ('not ready')
                
