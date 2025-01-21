#!/usr/bin/env python3

import sys


n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lower_encrypt = lower[n:] + lower[:n]
upper_encrypt = upper[n:] + upper[:n]

encrypt = []
d = {}

i = 0
while i < len(lower):
    d[lower_encrypt[i]] = lower[i]
    d[upper_encrypt[i]] = upper[i]
    i += 1

line = sys.stdin.readline().strip()
while line != "":
    encrypt = []
    i = 0
    while i < len(line):
        if line[i] in d:
            encrypt.append(d[line[i]])
        else:
            encrypt.append(line[i])
        i += 1
    print(''.join(encrypt))
    line = sys.stdin.readline().strip()
