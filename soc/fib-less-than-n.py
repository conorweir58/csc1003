#!/usr/bin/env python3

n = int(input())

prev = 0
curr = 1
total = 0

i = 0
while total < n:
  if i == 0:
    print(prev)
    print(curr)

    total = prev + curr
  else:
    total = prev + curr

    print(total)

    prev = curr
    curr = total
  i = i + 1
