#!/usr/bin/python

import sys
import os

if len(sys.argv) < 2:
	print "\t[+] Usage: ./deWeave [infile] [number of files] [block size]"
	print "\texample: ./deWeave picture.jpg 2 256"
	print "\tThis will split the input file (picture.jpg) into 2 files, 256 byte chunks at a time"
	exit()

infile = sys.argv[1]
argFiles = int(sys.argv[2])
argChunk = int(sys.argv[3])
lstItem = 0
start = 0
end = 0
container = []

file_buf = open(infile,"rb").read()

# Initialize blank array
for x in range(0, argFiles):
	blank = ""
	container.append(blank)

print "[+] Splitting file: " + infile 
print "Number of files: " + str(argFiles) 
print "Block size: " + str(argChunk) + " bytes"
print "File buffer size: " + str(len(file_buf)) + " bytes"
print "\n"
print "There should be " + str(x+1) + " output files."

# Split file into chunks
for i in range(0, len(file_buf), argChunk):
	end = start + argChunk
	container[lstItem] += file_buf[start:end]
	lstItem+=1
	start += argChunk

	if lstItem == argFiles:
		lstItem = 0


# Write output file
y = 0
for item in container:
	filename = "outfile" + str(y)
	print "[+] Written " + filename + " (Size: " + str(len(item)) + ")"
	open(filename,"wb").write(item)
	y+=1

print "[+] Done."
