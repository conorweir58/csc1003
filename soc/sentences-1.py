#!/usr/bin/env python3

import sys

s = []

a = sys.stdin.read().split()

lines = (' '.join(a) + ' ')

i = 0
j = 0
while i < len(lines):
   if lines[i] == ' ':
      if (lines[i - 1] == '.' or lines[i - 1] == '!' or lines[i - 1] == '?'):
         s.append(lines[j:i])
         j = i + 1
   i += 1

print('\n'.join(s))
