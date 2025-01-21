#!/usr/bin/env python3

a = []
position = 0

s = input()
while s != 'end':
  a.append(int(s))
  s = input()

smallest = a[0]
i = 0
while i < len(a):
  if smallest > a[i] and smallest != a[i]:
    smallest = a[i]
    position = i
  i += 1

print(position)
