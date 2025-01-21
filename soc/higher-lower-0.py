#!/usr/bin/env python3

curr = int(input())
prev = 0
prev = curr
if curr != 0:
  curr = int(input())
while curr != 0:
  if curr > prev:
    print('higher')
  elif prev > curr:
    print('lower')
  else:
    print("equal")
  prev = curr
  curr = int(input())
