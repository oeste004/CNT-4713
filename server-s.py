
import socket
import sys
import os
import time
import signal
import threading
from _thread import *

lock = threading.Lock()
messageLength = 0

def initiate():
    command = sys.argv
    port = int(command[1])
    host = "0.0.0.0"

    if port > 65535 or port < 1024:
        sys.stderr.write("ERROR: Incorrect port number")
        sys.exit(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((host, port))
    sock.listen(10)
    #not_stopped = False
    while True:
        try:
            s, address = sock.accept()
            time.sleep(1)
            with s:
                #print("Accepted connection from:", address)
                s.send(b"accio\r\n")
                lock.acquire()
                newThread = start_new_thread(threads, (s, ))
        except KeyboardInterrupt:
            sock.close()

def threads(s):
    #print(s)
    #s.send(b"accio\r\n")
    while True:
        try:
            data = s.recv(1024)
            if not data:
                sys.stderr.write("ERROR: Nothing received from server.")
                lock.release()
                sys.exit(0)
            else:
                full_message = full_message + data.decode("utf-8")
                messageLength = messageLength + len(data)
        except KeyboardInterrupt:
             lock.release()
             sys.exit(1)  
        s.close()
        
if __name__ == '__main__':
    initiate()
    