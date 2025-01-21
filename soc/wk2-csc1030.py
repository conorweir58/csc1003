#!/usr/bin/env python3

import math
import time

# QUESTION 1

# The time complexity = n,
# as the for loop at the beginning of the function n times as it goes through from 0 -> n,
# and the rest of the script runs through once with no loops or changes to the time complexity, making the time complexity = n

# QUESTION 2

# This is because the script halves the amount of elements it must run throught each time it is ran ("mid = (first + last)//2"),
# until there is only one element left making it 𝑂(log𝑛).

# QUESTION 3

# The time complexity = 2n,
# as the script runs through 2 for loops, n times

# QUESTION 4

# The time complexity = log₂(n),
# as the script is halving the size of n until it reaches 0

# QUESTION 5

# The time complexity = n^2,
# as the script has a nested for loop, where the main for loop runs n times, and the sub for loop runs n times inside the main loop for each
# time the main loop runs.

# QUESTION 6

# This is because the growth rate of n doubles every time the recursive function is run.


# QUESTION 7

def log2(n):
	k = 0
	while 0 < n:
		n = n // 2
		k += 1
	return k - 1

# print(int(math.log2(100)))
# print(log2(100))

# QUESTION 8

def has_duplicate_pairs(numbers):
	# for n in numbers:
	# 	if n in (numbers[:n - 1]) or n in (numbers[n:]):
	# 		return True
	# return False
	seen = set()
	for n in numbers:
		if n in seen:
			return True
		seen.add(n)
	return False


start_time = time.perf_counter()

print(has_duplicate_pairs([1, 2, 3, 4, 5]))
print(has_duplicate_pairs([1, 2, 3, 2]))
print(has_duplicate_pairs([7, 7, 7, 7]))
print(f'Simulation Time Taken: {(time.perf_counter() - start_time) * 1000:,} milliseconds.')
