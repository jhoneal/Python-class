def main():

	print("Welcome to the BMI calculator.")
	
	age = int(input("Please enter your age:"))
	
	if age < 16:
		print("Sorry, your age is too low to give an accurate reading.")
		
	else:
		
		weight = eval(input("Enter your weight (in kg): "))
		height = eval(input("Enter your height (in m): "))
	
		bmi = weight / (height**2)
		
		print(bmi)
		
		if bmi >= 30:
			print("Category: Obese")
		elif bmi >= 25 and bmi < 30:
			print("Category: Overweight")
		elif bmi >= 18.5 and bmi < 25:
			print("Category: Normal")
		else:
			print("Category: Underweight")
	
main()
