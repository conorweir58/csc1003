#!/usr/bin/env python3

s = input()
c = input()
v = input()

n = len(s)
m = len(c)
b = len(v)

if n > m and n > b:
  print(s)
elif m > n and m > b:
  print(c)
else:
  print(v)
