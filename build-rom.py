#!/bin/python
import sys
import itertools
import csv

# Create a 512 list (9 bits) mapping to 5 bits of control data output
words = [0] * 512
iter = itertools.islice(sys.stdin, 2, None)

# Open csvfile
csv_reader = csv.DictReader(iter)

# write the words correctly
for row in csv_reader:
	words[int(row['ibin'], 2)] = int(row['obin'], 2)

# output ROM to stdout
print("v3.0 hex words plain")
# Need to write words in 16 byte rows hex formatted
# Why 16 bytes ? that's just the way the file works
for i in range(int(512 / 16)):
	line = ""
	for j in range(16):
		line += f'{words[i * 16 + j]:0>6x} '
	line = line[:-1]
	print(line)
