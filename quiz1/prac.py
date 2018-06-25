#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
l=[]
for x in range(2000,3200):
	if  (x%7==0)and(x%5!=0):
		l.append(str(x))
print(','.join(l))	

#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
def show(fact)

