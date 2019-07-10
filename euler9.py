"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


import sys
import os
import time
import math

start_time = time.time()

def function():
	for x in range(0,1000):
		for y in range(0,1000):
			for z in range(0,1000):
				if x + y + z == 1000 and x < y < z and (x*x) + (y*y) == (z*z):
					print(x*y*z)
					quit()
				if x > 332:
					quit()



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