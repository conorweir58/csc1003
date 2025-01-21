#!/usr/bin/env python3

n = int(input())
base = 16
output = ''
digits = '0123456789abcdef'

while n != 0:
  output = (digits[n % base]) + output
  n = n // base

print(output)
