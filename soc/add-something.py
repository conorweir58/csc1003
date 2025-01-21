#!/usr/bin/env python3

a = []

s = input()
while s != 'end':
  m = int(s)
  a.append(m)
  s = input()

n = int(input())
i = 0
while i < len(a):
  add = a[i] + n
  print(add)
  i = i + 1
