#!/usr/bin/env python3

tpos = 0
tneg = 0

n = int(input())
while n != 0:
  if n < 0:
    tneg = tneg + n
  else:
    tpos = tpos + n
  n = int(input())

print(tneg, tpos)
