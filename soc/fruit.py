#!/usr/bin/env python3

import sys

words = sys.stdin.read().split()

a = 'apple pear orange banana cherry'.split()
fruit = {}

i = 0
while i < len(a):
  fruit[a[i]] = True
  i += 1

i = 0
while i < len(words):
  word = words[i]
  if word in fruit:
    print(translation[word])
  i += 1
