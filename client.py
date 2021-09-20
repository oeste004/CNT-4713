import socket
import sys
import os

class client:

    command = sys.argv
    host = command[1]
    port = int(command[2])
    fileName = command[3]

    # if port number is outside the valid range for TCP
    if port > 65535 or port < 1025:
        sys.stderr.write("ERROR: Invalid port number.")
        sys.exit(1)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to host and exits if not successful
    try:
        s.connect((host, port))
        s.settimeout(2)
        print("Connection succeeded.")
    except:
        sys.stderr.write("ERROR: Cannot connect.")
        sys.exit(1)

    # receive data in chunks and shows error if not received properly
    message = ""
    try:
        message = s.recv(1024)
    except:
        sys.stderr.write("ERROR: ")
        sys.exit(1)

    print(message.decode())

    file_size = os.path.getsize(fileName)

    file = open(fileName, 'rb')

    s.send(b"Content-Disposition: attachment; filename=")
    s.send(f"{fileName}".encode())
    s.send(b"\r\n")
    s.send(b"Content-Type: application/octet-stream\r\n")
    s.send(b"Content-Length: ")
    s.send(f"{file_size}".encode())
    s.send(b"\r\n")
    s.send(b"\r\n")

    line = file.readline(file_size)
    while line:
        #print("sending...")
        #print(line)
        s.send(line)
        line = file.readline(file_size)

    file.close()
    s.close()
    exit(0)
