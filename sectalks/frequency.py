#!/usr/bin/python
import re
import os.path

if not os.path.isfile("cipher.txt"):
        print "\n\t!!! Please store ciphertext in file cipher.txt !!!\n"
        exit()


string = open("cipher.txt","rb").read()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "ETAOINSHRDLUCMWFYGPBVKXJQZ"

counter = 0
list = []
print "Ciphertext: "
print string
for char in alphabet:
	#count the frequency of each letter in the ciphertext
	for letter in string:
		if char == letter:
			counter +=1
	if counter != 0: # Only list the letters that exist in the ciphertext
		list.append(char+':'+str(counter))
	counter = 0

#Bubble Pop!
# Use Bubble Sort to order the letters from highest frequency to lowest
numbers = re.compile('[0-9]{1,2}')

for passnum in range(len(list)-1, 0, -1):
	for i in range(passnum):
		curr = map(int, numbers.findall(list[i]))
		next = map(int, numbers.findall(list[i+1]))

		if curr < next:
			temp = list[i]
			list[i] = list[i+1]
			list[i+1] = temp
print "\n[*] Frequency:"
print list


order = ""
for item in list:
	order +=  re.sub(':',"",re.sub('[0-9]{1,2}',"",item))

print "\n[*] Key: " + key



newstring = ""
replaced = False
swaps = []
deep = input('Key Depth: ')

# Replace characters based on X depth of key
for x in range(len(string)):
	for  y in range(deep):
		if string[x] == order[y]:
			newstring += key[y]
			replaced = True
			swap = string[x]+">"+key[y] 
			if swap not in swaps:
				swaps.append(string[x]+">"+ key[y])
	if not replaced:
		newstring+=string[x]
	replaced = False
print "\n[*] Swaps: " 
print swaps

print "\n[+] Result:"
print newstring
