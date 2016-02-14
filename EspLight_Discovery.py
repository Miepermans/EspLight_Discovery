#!/usr/bin/python

import socket, traceback


host = ''     # Bind to all interfaces ( if no interface ip address is mentioned, some machines will respond to their own broadcast )
port = 1337   # Port to send data to

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

s.sendto("EspFind",('<broadcast>',1337))

while 1:
    try:
        message, address = s.recvfrom(8192)

        print "Got data from", address, message
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
