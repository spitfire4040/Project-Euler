sumList = set()

for x in range(0,1000):
	for y in range(0,1000):
		product = x * y
		if product not in sumList:
			sumList.add(product)
			if product == max(sumList):
				forward = str(product)
				reverse = forward[::-1]
				if forward == reverse:
					print(x,y,product)