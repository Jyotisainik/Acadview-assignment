#Take 10 integer from user and print it on screen.
x=[]
z=[]
n=int(input("enter any number"))
for i in range (10):
	x.append(z)
for i in x:
	print("i")
	
	
#2.write an infinite loop.an infinite loop never ends.condition is always true.
#i=0
#while i<=10
	#print("c")
	
	
#3.create a list of element by user input.make a new list which will store square of elements of previous list.
li=[]
sq=[]
for i in range(10):
	z=int(input("enter a number"))
	li.append(z)
	s=z*z
	sq.append(s)
print(li)
print(sq)


#4.from a list containing ints,strings and float,make three list to store them seprately.
li=[1,2,'a','b',7,7.0,6,'q']
i1=[]
f=[]
c=[]
for i in li:
	if(type(i)==int):
		i1.append(i)
	elif(type(i)==float):
		f.append(i)
	else:
		c.append(i)
print(li)
print(i1)
print(f)
print(c)

#5.using range (1,101) make a list containing even and odd numbers.
li=[]
li2=[]
for i in range(1,101):
	if((i%2)==0):
		c=i
		li.append(c)
	else:
		d=i
		li2.append(d)
print("even numbers are   ")
print(li)
print("odd numbers are  ")
print(li2)


#6.print the patterns.
for i in range (0,4):
    #inner loop to handle the number of columns
	for a in range (0,i+1):
		#printing stars
		print('*',end='')
	#ending line after each row
	print('\r')
	



#7.create a user defined dictionary and gets key corresponding to the value using for loop.
d={}
name=""
marks=""
for i in range(5):
	key=int(input("enter value "))
	value=(input("enter key "))
	d[key]=value
print(d)


#8.Take input from user to make a list.again take one input from user and search it in the list and delete that element,if found.itrate over list using for loops.
li=[]
n=int(input("enter the number of values u want to enter"))
for i in range(0,n):
	j=input("enter the value : ")
	li.append(j)
print(li)
j=input("enter the value u want to search  ")
for i in range(0,n):
	if(j==li[i]):
		print("element found ")
		li.remove(j)
		print("element deleted")
print(li)
	
	

		
		

	