#!/usr/bin/env python3

n = int(input())

if n == 3 or n == 2:
  print('prime')
elif n % 2 == 0 or n == 1:
  print('not prime')
elif n % 3 == 1 or n % 3 == 2:
  print('prime')
else:
  print('not prime')
