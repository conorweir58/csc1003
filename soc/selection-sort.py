#!/usr/bin/env python3

a = []

s = input()
while s != 'end':
  a.append(int(s))
  s = input()

i = 0
while i < len(a):
  p = i
  j = i + 1
  while j < len(a):
    if a[p] > a[j]:
      p = j
    j += 1
  tmp = a[i]
  a[i] = a[p]
  a[p] = tmp
  i += 1

x = 0
while x < len(a):
  print(a[x])
  x += 1
