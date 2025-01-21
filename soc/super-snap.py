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
while i < len(line) and d[line[i]] != 2:
  i += 1

if i < len(line):
  print('snap:', line[i])
