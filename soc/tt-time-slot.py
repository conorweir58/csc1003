#!/usr/bin/env python3

s = input()
while s != 'end':
  tokens = s.split()

  if 1 < int(tokens[2]):
    n = int(tokens[2]) - 1
    tokens[2] = int(tokens[1]) + n
  else:
    tokens[2] = tokens[1]

  a = int(tokens[1])

  tokens[2] = str(tokens[2])
  tokens[2] = (tokens[2] + ':50')
  tokens[1] = (tokens[1] + ':00')

  if a < 10:
    tokens[1] = tokens[1][1:]
    tokens[2] = tokens[2][1:]

  print(' '.join(tokens))
  s = input()
