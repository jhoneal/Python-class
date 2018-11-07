import random

def a1():

	a = random.randint(0,9)
	b = random.randint(0,9)
	
	print("What is {} + {}?".format(a,b))
	
	answer = int(input("Enter number:"))
	
	print(answer==a+b)
		
a1()
