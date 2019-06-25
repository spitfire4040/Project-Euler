import sys
import os

factors = []

def find_primes(10001):
	number = int(num)
	inc = 1

	while len(factors) < number:
		if inc % inc == 0:
			factors.append(x)
			print(x)
			inc += 1

	print(factors)


def main(argv):
	num = argv[1]
	find_primes(num)


if __name__ == '__main__':
	main(sys.argv)



# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?