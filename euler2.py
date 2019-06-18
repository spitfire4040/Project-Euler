import sys
import os

fib = [1,1]
sum = 0

while(fib[-1] <= 4000000):
	fib.append(fib[-1] + fib[-2])
	if((fib[-1] % 2) == 0):
		sum += fib[-1]

print(sum)