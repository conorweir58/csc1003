#!/usr/bin/env python3

import sys

line = sys.stdin.read().split()
d = {}

i = 0
while i < len(line):
  d[line[i]] = 0
  i += 1

i = 0
while i < len(line):
  if line[i] in d:
    d[line[i]] += 1
  i += 1

i = 0
while i < len(line):
  word = line[i]
  if d[word] == 1:
    print(word)
  i += 1
