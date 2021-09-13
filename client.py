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

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to host and exits if not successful
    try:
        s.connect((host, port))
        s.settimeout(10)
        print("Connection succeeded.")
    except:
        print("Connection refused.")
        sys.exit(1)

    # receive data in chunks and shows error if not received properly
    message = ""
    data = ''
    try:
        message = s.recv(1024)
        if data:
            message = message + data
    except:
        print("error")
        sys.exit(1)

    print(message)

    file_size = os.path.getsize(fileName)


    s.sendall(b"Content-Disposition: attachment; filename = \r\n")
    s.sendall(fileName)
    s.sendall(b"Content-Type: application/octet-stream\r\n")
    s.sendall(b"Content-Length: \r\n", file_size)
    s.sendall("\r\n")

    s.close()

