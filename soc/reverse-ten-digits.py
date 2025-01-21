#!/usr/bin/env python3

output = 0
total = 0

i = 0
while i < 10:
  n = int(input())
  total = total + n * (10 ** i)
  i = i + 1

x = 0
while x < 10:
  o = total // (1000000000 - 10 ** (x + 1))
  print(o)
  x = x + 1
