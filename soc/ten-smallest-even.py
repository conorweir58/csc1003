#!/usr/bin/env python3

tmp = 0

i = 0
while i < 10:
  n = int(input())
  if n % 2 == 0 and n != 0:
    if i == 0:
      tmp = n
    elif tmp > n:
      tmp = n
  i = i + 1

print(tmp)
