#!/usr/bin/env python3

tpos = 0
tneg = 0

i = 0
while i < 5:
  n = int(input())
  if n < 0:
    tneg = tneg + n
  else:
    tpos = tpos + n
  i = i + 1

print(tneg, tpos)
