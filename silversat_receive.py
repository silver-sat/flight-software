#!/usr/bin/python

import socket, sys, os
import RPi.GPIO as GPIO
import time
from gnc.gnc import GNC

# UDP_IP = '192.168.1.232' # the ip address of the recieving computer
UDP_IP = ''
UDP_PORT = 19614

LIGHT = 18
ALED = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT, GPIO.OUT)
GPIO.setup(ALED, GPIO.OUT)

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

    usestdin = False
    if len(sys.argv) > 1 and sys.argv[1] == "-":
        usestdin = True
        sys.argv.pop(1)
        print("Waiting for commands on stdin...")
    else:
        print("Listening on port %s" % (UDP_PORT,))

    while True:

            if usestdin:
                data = sys.stdin.readline().strip()
                addr = "stdin"
            else:
                data, addr = UDP_input();

            #print(data,addr)
            # If the program received something, print it. If not, print a dot.
  
            if data:    
                    print ("\nreceived command from %s: %s" % (addr,data))
            else:
                    sys.stdout.write('.')
                    sys.stdout.flush()
                    continue
  
            #  This is where any other commands would go.  Each command would consist of
            #    an 'if' statement (if data == 'something':), followed by the action the
            #    program should take.
  
            # if the program received a 'q', quit

            if data == 'q':
                    break;
            elif data == 'j': # code so that when i receive a j, print hi
                    print('Hi')
            elif data == 'Zuri':
                    print('yummy tummy')
            elif data == 'on':
                    GPIO.output(LIGHT, True)
                    GPIO.output(ALED, True)
            elif data == 'off':
                    GPIO.output(LIGHT, False)
                    GPIO.output(ALED, False)
            elif data == "photo":
                    print ("Photo started...!")
                    os.system("cd /home/pi/flight-software/payload; python3 VGAcamera.py")
                    if os.path.exists('/home/pi/Desktop/image.jpg') and os.path.getsize('/home/pi/Desktop/image.jpg') > 0:
                        print ("Photo taken!")
                    else:
                        print ("Photo failed...")
            elif data == 'head':
                    print (mygnc.orientation())
            elif data == 'accel':
                    print (mygnc.acceleration())
            elif data == 'position':
                    if mygnc.ready():
                            print (mygnc.position())
                    else:
                            print ('GPS not ready')
            else:
                    print ("Bad request: "+data)
