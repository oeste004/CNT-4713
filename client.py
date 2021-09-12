import socket
import sys

class client:

    command = sys.argv
    host = command[1]
    port = int(command[2])
    #fileName = command[3]



    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        print("Connection succeeded.")
    except:
        print("Connection refused.")
