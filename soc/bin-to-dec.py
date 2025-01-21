#!/usr/bin/env python3

s = input()
base = 2
dec = 0

i = 0
while i < len(s):
  dec = dec + int(s[len(s) - i - 1]) * (base ** i)
  i = i + 1

print(dec)
