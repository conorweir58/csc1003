#!/usr/bin/env python3

import sys

a = sys.stdin.read().split()

i = 0
while i < len(a):
   a[i] = a[i].split('/')
   print(a[i][len(a[i]) - 1])
   i += 1
