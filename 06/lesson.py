"""
with open('test.txt', 'r') as fopen:
    lines = fopen.readlines()

for l in range(len(lines)):
    print("Line " + str(l,), lines[l])
"""

import os
check = os.stat('empty.txt').st_size == 0
if check == True:
    print("File is empty")
else:
    print("File not empty")

