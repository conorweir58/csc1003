#!/usr/bin/env python3

class Horse(object):

	def __init__(self):
		self.prices = {}
		previous_price = 1000
		for horse in (range(100,0,-1)):
			self.prices[horse] = previous_price
			previous_price = previous_price * 1.1


	def display(self, rank):
		if rank == -1:
			for horse in range(1,101):
				print(f"Rank: {horse}, Price: {self.prices[horse]:.2f}")
		elif rank not in (range(1,101)):
			print(f"A horse with rank {rank} was not found!")
		else:
			print(f"Rank: {rank}, Price {self.prices[rank]:.2f}")


# COMMENTED OUT FOR OTHER CLASS TESTING
# horse = Horse()

# rank = int(input("Please enter a horses rank to find their price: "))
# while rank:
# 	horse.display(rank)
# 	rank = int(input("Please enter a horses rank to find their price: "))


def sqrnums(numbers):
	sqrd_numbers = []
	for n in numbers:
		sqrd_numbers.append(n ** 2)
	return sqrd_numbers

# print(sqrnums([1, 2, 3, 4]))

def reverse_and_upper(words):
	changed_words = []
	for word in words:
		word = word.upper()
		word = word[::-1]
		changed_words.append(word)
	return changed_words

# print(reverse_and_upper(["hello", "goodbye"]))

class BankAccount():

	def __init__(self, fname, sname, idnum, phonenum):
		self.__fname = fname
		self.__sname = sname
		self.__idnum = idnum
		self.__phonenum = phonenum
		self.balance = 0

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= balance

	def get_balance(self):
		return self.balance

bnk = BankAccount("Conor", "Weir", 234345, 187524638)

class CurrentAccount(BankAccount):

	def __init__(self):
