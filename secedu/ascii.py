#!/usr/bin/python

import re

fBuf = open('scrambled.txt', 'rb').read()

lines = fBuf.splitlines()

numbers = re.compile('[0-9]{1,3}')

# Bubble Pop
for passnum in range(len(lines)-1, 0, -1):
	for i in range(passnum):
		curr = map(int, numbers.findall(lines[i]))
		next = map(int, numbers.findall(lines[i+1]))

		if curr > next:
			temp = lines[i]
			lines[i] = lines[i+1]
			lines[i+1] = temp

# Print Result
for item in lines:
#	item = re.sub('[0-9]{1,3}', "",item)
#	print re.sub(':', "", item)
	print re.sub(':',"",re.sub('[0-9]{1,3}',"",item))
