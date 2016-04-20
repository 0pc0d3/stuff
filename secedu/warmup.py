#!/usr/bin/python

cipher = "TGPRGWTADEKI HI3OYNODONAT ES4LOCIINTB} FC4LURSDTHO_ LO1IRYAEEIU_ AM{NOPBAVNT_"

output = ""

for i in range(len(cipher.partition(' ')[0])):
	for x in cipher.upper().split():
		output += x[i]

print output
