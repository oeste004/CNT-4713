import socket
import sys

command = sys.argv

host = command[1]
port = command[2]
#fileName = command[3]

success = False

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((host, port))
    success = True
except:
    success = False

print(success)