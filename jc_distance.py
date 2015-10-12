# compare 2 seqs, return their JC distance
def calc_jc(seq1, seq2):
	diff = 0
	ignore = 0
	for i in range(0, len(seq1)):
		if seq1[i] != seq2[i]:
			if seq1[i] == '-' or seq2[i] == '-':
				ignore += 1
			else:
				diff += 1
	P = float(diff) / (float(len(seq1) - ignore))
	jc = round(-0.75 * math.log(1 - (4.0 / 3.0) * P), 4)
	return jc

# add key(seq names), values (seqs) to dict
def make_dict(file1):
	myDict = collections.OrderedDict()
	key = ''
	for line in file1:
		line = line.strip() 
    		if '>' in line:
        		key = line.strip(">")
        		myDict[key] = ''
        	else:
        		myDict[key] += line
	return myDict
	file1.close()

import sys
import collections
import math

file1 = open(sys.argv[1], 'r')
myDict = make_dict(file1)

# loop through keys, compare seqs, and print jc scores
for i, key in enumerate(myDict.keys()):
	for nextkey in myDict.keys()[i+1:]:
		print key, nextkey, calc_jc(myDict[key], myDict[nextkey])
