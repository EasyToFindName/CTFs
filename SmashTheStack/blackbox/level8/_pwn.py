#!/usr/bin/python2

from pwn import *

s = 'U[[ZRcWfcXVM$l"#'

s = ''.join([b + a for a,b in zip(s[::2], s[1::2])])

for i in xrange(256):
	r = chr(i)
	
	for j in s:
		r += chr((ord(j)-90 + ord(r[-1])) % 256)
	
	print i, `r`
