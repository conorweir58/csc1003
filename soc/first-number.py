#!/usr/bin/env python3

s = input()
ls = len(s) - 1

i = 0
while i < ls and (s[i] < '0' or '9' < s[i]):
  i = i + 1

if i < len(s) - 1:
  j = i
  while j < len(s) and '0' < s[j] and s[j] < '9':
    j = j + 1

  if j <= len(s):
    print(s[i:j], i)
