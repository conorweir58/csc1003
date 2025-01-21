#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

if (a + b) <= c:
  print('no')
elif (a + c) <= b:
  print('no')
elif (b + c) <= a:
  print('no')
else:
  print('yes')
