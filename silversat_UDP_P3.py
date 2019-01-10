import socket, sys

UDP_IP = ' '
UDP_PORT = 19614


def UDP_input(recPort = UDP_PORT):
    sock = socket.socket(socket.AF_INET,
                socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    sock.settimeout(1)
    try:
        data, addr = sock.recvfrom(1024)
        data = data.decode("utf-8")
    except socket.timeout:
        data = None
        addr = None
    sock.close()
    return(data,addr)

if _name_ == "_main_":

    print("Listening on port %s, socket %4.0f" % (UDP_IP, UDP_PORT))

    runLoop = True
    while runLoop:
        data, addr = raw_UDP_input();
        if data:
                print("\nrecieved message from %s: %s \n" % (addr, data))

        else:
                sys.stdout.write('.')
                sys.stdout.flush()

        if data == 'q':
                runLoop = False  
