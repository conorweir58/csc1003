#!/usr/bin/env python3

import sys

cap = int(sys.argv[1])

total = 0
f = 0
s = 1
while f < cap:
    if f % 2 == 0:
        total += f
    tmp = s + f
    f = s
    s = tmp

print(total)
