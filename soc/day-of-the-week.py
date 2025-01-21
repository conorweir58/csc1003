#!/usr/bin/env python3

month = int(input())

day = int(input())

dayofyear = 360 - ((12 - month) * 30) - (30 - day)

n = dayofyear - 1

dayofweek = n % 7

actualdow = dayofweek + 1

print(actualdow)
