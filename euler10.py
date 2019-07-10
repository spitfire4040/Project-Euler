"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""



import sys
import os
import time

start_time = time.time()


def function():
	total = 0
	for x in reversed(range(2,2000001)):
		flag = False
		for y in range(2,x+1):
			if x != y and x % y == 0:
				flag = True
		if flag == False:
			print(x)
			total += x

	print(total)
	print(primes)


def main(argv):
	if len(argv) < 2 or len(argv) > 2:
		print("Usage: <euler7.py><endingNumber>")
		sys.exit()
	else:
		var = sys.argv[1]

	function()
	print("Program took %s seconds to run." % (time.time() - start_time))

if __name__ == '__main__':
	main(sys.argv)