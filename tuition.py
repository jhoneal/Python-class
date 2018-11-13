"""Suppose that the tuition for a university is $10,000 this
year and tuition increases 7% every year. In how
many years will the tuition be doubled?"""



year = 0 
tuition = 10000

while tuition < 20000:

	tuition = tuition * 1.07
	year+=1
	
print(year)
