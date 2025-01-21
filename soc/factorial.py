#!/usr/bin/env python3

n = int(input())
total = 1

i = 0
while i < n:
  total = total * (i + 1)
  i = i + 1

print(total)
