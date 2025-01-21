#!/usr/bin/env python3

import sys

position = int(sys.argv[1])
cities = []

s = input()
cities.append(s)

i = 0
start = 0
while i < position:
  while cities[0][start] != ',':
    start += 1
  start += 1
  i += 1

end = start
j = 0
while j < len(cities[0][start:]) and cities[0][end] != ',':
  end += 1
  j += 1

if j < len(cities[0][start:]):
  print(cities[0][start:end])
else:
  print(cities[0][start:])
