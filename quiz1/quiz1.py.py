#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
l=[]
for x in range(2000,3200):
	if  (x%7==0)and(x%5!=0):
		l.append(str(x))
print(','.join(l))	

#Write a program which accepts a sequence of comma-separated 
#numbers from console and generate a list and a tuple 
#which contains every number.
import random 
for i in range(6):
	n=random.randint(0,6)
	l.sort(str(i))
n=int(input("enter any number"))
print(','.join(1))

	




