#!/usr/bin/env python3

import sys

message = sys.argv[2:]
file_name = sys.argv[1]

with open(file_name, "w") as f:
  i = 0
  while i < len(message):
    f.write(message[i] + '\n')
    i += 1
