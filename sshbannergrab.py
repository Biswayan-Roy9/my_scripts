#its not working

import socket

#need modifications 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("10.0.2.5",21))

answer = s.recv(1024)

print(answer)

s.close()
