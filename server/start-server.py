import socket,sys,os,threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(os.gethostname(),5600)
s.listen(5)
while True:
  s.accept()
