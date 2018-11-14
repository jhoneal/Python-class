"""2. All Even Numbers

Create a loop that will print out all even numbers between 1 and a specified integer."""

num = int(input("Please enter a number: "))

for i in range(num+1):
	if i %2 == 0:
		print(i)
