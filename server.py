import socket
import sys
import os
import time
import signal
import threading
from _thread import *

lock = threading.Lock()
isProcessing = False
timeoutTimer = time.time()

def initiate():
    command = sys.argv
    port = int(command[1])
    directory = command[2]

    if port > 65535 or port < 1024:
        sys.stderr.write("ERROR: Incorrect port number")
        sys.exit(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind(("0.0.0.0", port))
    sock.listen(10)
    count = 0
    while True:
        full_message = ' '
        messageLength = 0
        try:
            s, address = sock.accept()
            count += 1
            s.send(b"accio\r\n")
            data = s.recv(1024)
            while data:
                data = b''
                data = s.recv(10000000)
                messageLength = messageLength + len(data)
                
            if (messageLength > 0):
                print(messageLength)
        except KeyboardInterrupt:
            sys.exit(0)


        
if __name__ == '__main__':
    initiate()