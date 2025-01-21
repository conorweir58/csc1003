#!/usr/bin/env python3

x = 0
y = 0
total = ''

j = 0
while j < 10:
  i = 0
  s = input()
  while s[i] != '+' and i < len(s):
    i = i + 1

  if i < len(s):
    x = int(s[:i])
    y = int(s[i:])
    a = str(x)
    b = str(y)
    total = str(x + y)
    print(total)
  j = j + 1
