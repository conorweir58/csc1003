#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
  if ((i + 1) % 3) + ((i + 1) % 5) == 0:
    print('fizz-buzz')
    i = i + 1
  elif ((i + 1) % 3) == 0:
    print('fizz')
    i = i + 1
  elif ((i + 1) % 5) == 0:
    print('buzz')
    i = i + 1
  else:
    print(i + 1)
    i = i + 1
