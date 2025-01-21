#!/usr/bin/env python3

total = 0

s = input()
while s != 'end':
  tokens = s.split()
  total += int(tokens[2])
  s = input()

print(total)
