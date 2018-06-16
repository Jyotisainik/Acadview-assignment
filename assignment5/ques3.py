#1.Take an input year from user and decide wheather it is a leap year or not.
n=int(input("enter any number"))
if (n%4!=0):
	print(" not leap year")
else:
	print("leap year")
	
	
#2.Take lenght and breadth input from user and cheack wheather the dimensions are of square and rectangle.
l=input("enter a lenght")
b=input("enter a breadth")
if  l==b:
	print("dimension of square")
else:
	print("dimension of rectangle")
	
	
#3.Take the input age of 3 people and determine oldest and youngest among them.
#for oldest.
a=input("enter any number")
b=input("enter any number")
c=input("enter any number")
if((a>b)and(a>c)):
		print("a is oldest")
elif((b>a)and(b>c)):
	print("b is oldest")
else:
	print("c is oldest")

#for youngest.
a=input("enter any number")
b=input("enter any number")
c=input("enter any number")
if((a<b)and(a<c)):
		print("a is youngest")
elif((b<a)and(b<c)):
	print("b is youngest")
else:
	print("c is youngest")
	

#4.
n=int(input("enter any number between 1-200"))
j1="no prize"
j2="wooden dog"
j3="book"
j4="chocolate"
if 	((n>=1)and(n<50)):
	print("sorry! no prize this time")
elif ((n>151)and(n<=150)):
		print("congratulations!you have won %s"%(j2))
elif (n>=151)and(n<=180):
		print("congratulations!you have won %s"%(j3))
elif (n>=181)and(n<=200):
		print("congratulations!you have won %s"%(j4))
else:
	print("enter correct number")
	
	
#5.
q=int(input("enter the units"))
q1=q*100
if (q1>1000):
	dis=((10/q)*100)
	q1=q1-dis
	print("total cost is %d"%(q1))
else:
		print("no discount")


	
	
	
	
	
		
		