from pwn import *

r = remote("0", 9007)
print r.read()

def coins_amount():
	string = r.readline()
	print "\nTASK:", string

	return int(string.split(' ')[0][2:])

def weight(indexes):
	r.sendline(' '.join(str(x) for x in indexes))

	recv = r.recvline()

	if recv.find("Correct") != -1:
		print recv
		return -1
	else:
		return int(recv)

while True:
	try: 
		N = coins_amount()
	except:
		r.interactive()

	b,e = 0,N
	counter = 0

	while e - b > 1:
		mean = (e - b) / 2

		w = weight(range(b + mean, e))
		counter += 1

		print "%d: (%d, %d) - %d" %(counter, b,e,w)

		if w % 10 == 0:
			e -= mean
		else:
			b += mean

	if weight(range(b,e)) != -1:
		weight(range(b+1, e+1))