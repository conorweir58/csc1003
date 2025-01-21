#!/usr/bin/env python3

prev = int(input())

i = 0
while i < 5:
  curr = int(input())
  if prev == curr:
    print('equal')
    prev = curr
  elif curr > prev:
    print('higher')
    prev = curr
  elif prev > curr:
    print('lower')
    prev = curr
  i = i + 1
