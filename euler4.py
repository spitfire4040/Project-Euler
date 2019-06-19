palindromes = {}

for x in range(100,1000):
	for y in range(100,1000):
		print(x,y)
		product = x * y
		forward = str(product)
		reverse = forward[::-1]
		if forward == reverse:
			palindromes.update({product:[x,y]})

print(palindromes)

largest = 0
first = 0
second = 0

for item in palindromes:
	if item > largest:
		largest = item
		first = palindromes[item][0]
		second = palindromes[item][1]


print(palindromes)
print(' ')
print(largest,first,second)