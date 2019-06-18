import sys
import os

num = 600851475143
factors = []
templist = set()
for x in range(1, num):
	if num % x == 0:
		factors.append(x)
		print(x)
for element in factors[::-1]:
	for factor in factors:
		if element % factor == 0 and element != factor and factor != 1:
			templist.add(element)

for entry in templist:
	if entry in factors:
		factors.remove(entry)


print(factors)
print(templist)