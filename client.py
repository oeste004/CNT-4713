import socket
import sys
import os

class client:

    command = sys.argv
    host = command[1]
    port = int(command[2])
    fileName = command[3]

    # if port number is outside the valid range for TCP
    if port > 65535 or port < 1:
        sys.stderr.write("ERROR: ")
        sys.exit(1)

    nameLen = len(fileName)

    if fileName[nameLen-1] != 't' or fileName[nameLen-2] != 'x' or fileName[nameLen-3] != 't':
        sys.stderr.write("ERROR: ")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to host and exits if not successful
    try:
        s.connect((host, port))
        s.settimeout(10)
        print("Connection succeeded.")
    except:
        sys.stderr.write("ERROR: ")
        sys.exit(1)

    # receive data in chunks and shows error if not received properly
    message = ""
    data = ''
    try:
        message = s.recv(1024)
        if data:
            message = message + data
    except:
        sys.stderr.write("ERROR: ")
        sys.exit(1)

    print(message)

    file_size = os.path.getsize(fileName)

    s.send(b"Content-Disposition: attachment; filename = \r\n")
    s.send(fileName.encode())
    s.send(b"Content-Type: application/octet-stream\r\n")
    s.send(b"Content-Length: \r\n")
    #s.send(file_size)
    #s.send("\r\n")

    file = open(fileName, 'rb')
    lines = file.readlines()
    for line in lines:
        s.send(line)

    s.close()


