import sys
import os
import time

start_time = time.time()

def function():
	pass

def main(argv):
	if len(argv) < 2 or len(argv) > 2:
		print("Usage: <euler7.py><endingNumber>")
		sys.exit()
	else:
		var = sys.argv[1]

	print(function())
	print("Program took %s seconds to run." % (time.time() - start_time))

if __name__ == '__main__':
	main(sys.argv)