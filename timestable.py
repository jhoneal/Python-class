#Write a program that uses nested  for loops to print a multiplication table

for i in range(1,10):
	for j in range(1,10):
		print("{} x {} = ".format(i,j),i*j)
