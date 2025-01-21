#!/usr/bin/env python3

import sys

gender = {}

with open('boys.txt') as b:
  boy_name = b.read().split()
  i = 0
  while i < len(boy_name):
    gender[boy_name[i]] = 'boy'
    i += 1

with open('girls.txt') as g:
  girl_name = g.read().split()
  i = 0
  while i < len(girl_name):
    if girl_name[i] in gender:
      gender[girl_name[i]] = 'either'
    else:
      gender[girl_name[i]] = 'girl'
    i += 1

name = sys.stdin.readline().strip()
while name != '':
  print(name, gender[name])
  name = sys.stdin.readline().strip()
