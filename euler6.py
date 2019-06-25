import sys
import os

def sum_of_squares(num1):
	total = 0
	for x in range(1,int(num1)+1):
		total += (x * x)
	return total

def square_of_sum(num2):
	total = 0
	for x in range(1,int(num2)+1):
		total += x
	result = (total * total)
	return result

def calc_result(num1, num2):
	return num2 - num1

def main(argv):
	if len(argv) < 2:
		print("usage: program_name, number")

	num = sys.argv[1]
	num1 = sum_of_squares(num)
	num2 = square_of_sum(num)
	print(calc_result(num1, num2))


if __name__ == '__main__':
	main(sys.argv)