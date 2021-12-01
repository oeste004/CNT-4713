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
    host = "0.0.0.0"

    if port > 65535 or port < 1024:
        sys.stderr.write("ERROR: Incorrect port number")
        sys.exit(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((host, port))
    sock.listen(3)
    while True:
        full_message = ' '
        messageLength = 0
        try:
            s, address = sock.accept()
            s.send(b"accio\r\n")
            data = s.recv(1024)
            print("here")
            while data:
                data = b''
                messageLength = messageLength + len(data)
                data = s.recv(10000)
                
            if (messageLength > 0):
                print(messageLength)
        except KeyboardInterrupt:
            sys.exit(0)


        
if __name__ == '__main__':
    initiate()