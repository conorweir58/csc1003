#!/usr/bin/env python3

n = int(input())

n = (n % 10000)

n = (n // 100)

n = (n * 10)

o = (n % 100)

m = (n // 100)

print(o + m)
