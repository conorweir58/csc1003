#!/usr/bin/env python3

import sys

total = 0

i = 1
while i < len(sys.argv):
  file_name = sys.argv[i]
  with open(file_name) as f:
    a = f.readlines()
    j = 0
    while j < len(a):
      total += int(a[j])
      j += 1
  i += 1

print(total)
