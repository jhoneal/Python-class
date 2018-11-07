

def main():

	print("Enter three numbers: ")
	first = eval(input("What is your first number?"))
	second = eval(input("What is your second number?"))
	third = eval(input("What is your third number?"))
	
	total = (first + second + third) / 2
	
	print("{} + {} + {} /2 is...".format(first, second, third))
	print(total)
	
	
main()
