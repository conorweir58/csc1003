#!/usr/bin/env python3

month = int(input())

day = int(input())

dayofyear = 360 - ((12 - month) * 30) - (30 - day)

print(dayofyear)
