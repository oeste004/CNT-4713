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
        s.settimeout(10)
        s.connect((host, port))
        print("Connection succeeded.")
    except Exception as e:
        sys.stderr.write("ERROR: Could not connect to server")
        s.close()
        sys.exit(1)

    # receive data in chunks and shows error if not received properly
    message = ""
    try:
        s.settimeout(10)
        message = s.recv(1024)
    except:
        sys.stderr.write("ERROR: Nothing received from server.")
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


    chunk = file.readline(file_size)
    line = ' '
    while len(line) > 0:
        line = file.readline(file_size)
        chunk += line

    s.send(chunk)
    file.close()
    s.close()
    exit(0)
