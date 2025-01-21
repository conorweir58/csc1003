#!/usr/bin/env python3

import sys

german = 'eins zwei drei vier funf sechs sieben acht neun zehn'.split()
english = 'one two three four five six seven eight nine ten'.split()

words = sys.stdin.read().split()

transaltion = {}

i = 0
while i < len(english):
  transaltion[english[i]] = german[i]
  i += 1

i = 0
while i < len(words):
  word = words[i]
  if word in english:
    print(transaltion[word])
  i += 1
