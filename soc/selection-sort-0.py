#!/usr/bin/env python3

a = []

s = input()
while s != 'end':
  a.append(int(s))
  s = input()

smallest = a[0]
i = 0
while i < len(a):
  if smallest > a[i]:
    smallest = a[i]
  i += 1

print(smallest)
