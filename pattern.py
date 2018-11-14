"""4. Pattern

Write a program to display a pattern like this:

1
22
333
4444"""

for i in range(1,5):
	for j in range(i):
		print(i,end='')
	print("\r")
