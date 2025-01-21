#!/usr/bin/env python3

import sys

transaltion = {}

words = sys.stdin.readline()
while 0 < len(words):
  tokens = words.split()
  transaltion[tokens[0]] = tokens[1]
  words = sys.stdin.readline()

s = input()
if s in transaltion:
  print(transaltion[s])
  s = input()
