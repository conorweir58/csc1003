#!/usr/bin/env python3

n = int(input())

prev = 0
curr = 1

i = 0
while i < n - 1:
  if i == 0:
    print(prev)
    print(curr)
  else:
    total = prev + curr

    print(total)

    prev = curr
    curr = total
  i = i + 1
