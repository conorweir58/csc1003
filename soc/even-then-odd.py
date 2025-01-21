#!/usr/bin/env python3

a = []

s = input()
while s != 'end':
  n = int(s)
  if n % 2 == 0:
    print(n)
  else:
    a.append(n)
  s = input()

i = 0
while i < len(a):
  print(a[i])
  i = i + 1
