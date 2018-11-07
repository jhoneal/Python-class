

def main():
	
	print("Please enter the following information so I can sell it for a profit!")
	print("First name: ")
	fname = input()
	print("Last name: ")
	lname = input()
	print("Grade (9-12)")
	grade = input()
	print("Student ID: ")
	id = input()
	print("Login: ")
	login = input()
	print("GPA (0.0-4.0)")
	gpa = input()
	
	print("Your Information:")
	print("Login:", login)
	print("ID:", id)
	print("Name:", lname + fname)
	print("GPA:", gpa)
	print("Grade:", grade)

main()
