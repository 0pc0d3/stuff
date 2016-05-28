#!/usr/bin/python

print "\n[*] Ciphertext.\nThis is the text we need to decode.\n"
ciphertxt = raw_input("Please enter ciphertext: ")
icase = "y"

set1 = "abcdefghijklmnopqrstuvwxyz"
set2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

print "\n[*] Character Sets."
print "This set will be used to derive the base position of the chracters in the ciphertext. You can choose the basic alphabet set below or enter your own custom set.\n"
print "[1] Basic: " + set1 + " (case insensitive)"
print "[2] Upper and Lower: " + set2
print "[3] Custom...\n"

set_ans = input("Choose character set: ")

if set_ans == 1:
	charset = set1
elif set_ans == 2:
	charset = set2
elif set_ans == 3:
	charset = raw_input("Please enter your custom character set: ")
	icase = raw_input("Case insensitive? [Y]es [N]o: ")
else:
	print "\n[-] Choice unknown. Exiting...\n"
	exit()

print "\n[*] Key. \nThis is the key text used to decode the ciphertext.\n"
key = raw_input("Enter Key: ")
plaintext = ""

for letter in ciphertxt:
	if "y" in icase.lower():
		if letter.lower() in charset.lower():
			plaintext += key[charset.index(letter)]
		else:
			plaintext += letter
	else:
		if letter in charset:
			plaintext += key[charset.index(letter)]
		else:
			plaintext += letter

print "\n\n[+] Decoded Plain Text: " + plaintext + "\n"
