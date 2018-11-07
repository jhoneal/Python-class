

def main():

	amt = eval(input("Enter the monetary amount: "))
	
	con = amt * 100
		
	dollar = con // 100
	change = con % 100
	
	quarter = change // 25
	change = con % 25
	
	dime = change // 10
	change = con % 10
	
	nickel = change // 5
	change = con % 5
	
	print("Dollars =",int(dollar))
	print("Quarters =",int(quarter))
	print("Dimes =",int(dime))
	print("Nickles =",int(nickel))
	print("Pennies =",int(change))
	
	
main()
