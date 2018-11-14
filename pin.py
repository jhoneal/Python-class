"""Basic Loops

1. PIN Number

Create an integer named [pin] and set it to a 4-digit number.
Welcome the user to your application and ask them to enter their pin.
If they get it wrong, print out "INCORRECT PIN. PLEASE TRY AGAIN"
Keep asking them to enter their pin until they get it right.
Finally, print "PIN ACCEPTED. YOU HAVE $0.00 IN YOUR ACCOUNT. GOODBYE."""


pin = 9999
num = int(input("Welcome to this application. Please enter your pin: "))

while num != pin:
	num = int(input("INCORRECT PIN. PLEASE TRY AGAIN: "))

print("PIN ACCEPTED. YOU HAVE $0.00 IN YOUR ACCOUNT. GOODBYE.")
