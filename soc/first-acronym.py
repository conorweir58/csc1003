#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) - 1 and 'a' <= s[i] and s[i] <= 'z' or s[i] == ' ':
  i = i + 1

if i < len(s) - 1:
  j = i
  while j < len(s) and 'A' <= s[j] and s[j] <= 'z':
    j = j + 1

  if j <= len(s):
    print(s[i:j], i)
