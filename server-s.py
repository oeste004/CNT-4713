
import socket
import sys
import os
import time
import signal

command = sys.argv
port = int(command[1])
host = "0.0.0.0"

if port > 65535 or port < 1024:
    sys.stderr.write("ERROR: Incorrect port number")
    sys.exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(10)
not_stopped = False

sock = ""

try:
    sock, address = s.accept()
    print("Accepted connection from:", address)
    sock.send(b"\r\n'accio\r\n")
    full_message = sock.recv(1).decode()
    bit = ' '
    messageLength = len(full_message)
    while len(bit) > 0:
        bit = sock.recv(8)
        full_message = full_message + bit.decode("utf-8")
        messageLength = messageLength + len(bit)
    print(full_message)
    print(messageLength+50)
    time.sleep(1)
except KeyboardInterrupt:
    sock.close()

s.close()
exit(0)