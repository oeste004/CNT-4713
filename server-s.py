
import socket
import sys
import os
import time
import signal
import threading
from _thread import *

lock = threading.Lock()
isProcessing = False

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
    count=0
    #not_stopped = False
    isProcessing = False
    while True:
        try:
            time.sleep(1)
            s, address = sock.accept()
            isProcessing = True
            count += 1
            print(count)
            time.sleep(1)
            s.send(b"accio\r\n")
            lock.acquire()
            
            newThread = start_new_thread(threads, (s, ))
        except KeyboardInterrupt:
            print("CLOSED")

def threads(s):
    full_message = ' '
    messageLength = 0
    while True:
        try:
            s.settimeout(10)
            data = s.recv(1024)
            if not data:
                sys.stderr.write("ERROR: Nothing received from client.")
                lock.release()
                #sys.exit(0)
                break
            else:
                full_message = full_message + data.decode("utf-8")
                messageLength = messageLength + len(data)
        except KeyboardInterrupt:
             lock.release()
             sys.exit(1) 
        print(messageLength)
    s.close()
        
if __name__ == '__main__':
    initiate()
    