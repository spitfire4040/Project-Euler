# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import sys
import os

counter = 1

def findSmallest():
	global counter

	for x in range(sys.maxsize**10):
		if x != 0:

			flag = True

			for y in range(1,21):
				if x % y != 0:
					flag = False

			if flag == True:
				return x


def main(argv):
	print(argv)
	result = findSmallest()
	print(result)

if __name__ == '__main__':
	main(sys.argv)