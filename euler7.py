# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import sys
import os

temp = []
primes = []

def find_primes(end):
	x = 2
	while len(temp) < int(end):
		flag = False
		for y in range(2,x):
			if x % y == 0:
				flag = True
		if flag == False:
			temp.append(x)

		x += 1

def main(argv):
	if len(argv) < 2 or len(argv) > 2:
		print("Usage: <euler7.py><endingNumber>")
		sys.exit()
	else:
		end = sys.argv[1]
	find_primes(end)
	print(temp)

if __name__ == '__main__':
	main(sys.argv)