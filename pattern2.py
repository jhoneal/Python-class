"""4. Pattern

Write a program to display a pattern like this:

1
22
333
4444

Modify the program so that the user can specify what number it should go up to."""

num = int(input("Enter a number: "))

for i in range(num+1):
	for j in range(i):
		print(i,end='')
	print("\r")
