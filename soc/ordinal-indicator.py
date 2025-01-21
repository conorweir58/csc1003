#!/usr/bin/env python3

n = int(input())

a = n % 100
m = n % 10

if a == 11 or a == 12 or a == 13:
  print('th')
elif m == 1:
  print('st')
elif m == 2:
  print('nd')
elif m == 3:
  print('rd')
else:
  print('th')
