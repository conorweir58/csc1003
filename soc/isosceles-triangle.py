#!/usr/bin/env python3

a = int(input())

b = int(input())

c = int(input())

print((a == b != c) or (a == c != b) or (b == c != a) or (a == b == c))
