#!/usr/bin/python
import os.path

if not os.path.isfile("cipher.txt"):
	print "\n\t!!! Please store ciphertext in file cipher.txt !!!\n"
	exit()

cipher = open("cipher.txt","rb").read()

print "\n[*] Cipher:"
print cipher

print "\n[*] My Hips Don't Lie..."
rot = input("How many rotations? : ")

print "\n[*] Rotations:"
plaintext = ""

for x in range(1,int(rot)+1):
	for y in range(len(cipher)):
		ans = ord(cipher[y]) + x
		z = x
		#Check if the rotation goes over Z, then go back to A
		if ans > 90:
			z = x - 26
		plaintext += chr(ord(cipher[y])+z)
	print "\n[" + str(x) +"] "+plaintext
	plaintext = ""
