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

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    exit(0)

while True:
    sock = ""

    try:
        signal.signal(signal.SIGINT, handler)
        signal.signal(signal.SIGTERM, handler)
        time.sleep(1)
        sock, address = s.accept()
        print("Accepted connection from:", address)
        sock.send(b"\r\n'accio\r\n")
        full_message = ""
        bit = ' '
        while len(bit) > 0:
            bit = sock.recv(1)
            full_message = full_message + bit.decode("utf-8")
        print(full_message)
        messageLength = len(full_message.encode('utf-8'))
        print("message length: " + str(messageLength))
    except KeyboardInterrupt:
        sock.close()
        break

s.close()
exit(0)