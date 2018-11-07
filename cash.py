

def main():


	tax = .08875
	amt = eval(input("Enter price of the item: "))
	itemTax = amt * tax
	total = itemTax + amt
	
	print("Tax: {:.2f}".format(itemTax))
	print("Total is: {:.2f}".format(total))
	
main()
