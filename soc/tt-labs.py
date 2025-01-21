#!/usr/bin/env python3

s = input()
while s != 'end':
  tokens = s.split()
  if 1 < int(tokens[2]):
    print(' '.join(tokens))
  s = input()
