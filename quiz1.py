# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
l=[]
for x in range(2000,3200):
	if  (x%7==0)and(x%5!=0):
		l.append(str(x))
print(','.join(l))

# Write a program which accepts a sequence of comma-separated
# numbers from console and generate a list and a tuple
#which contains every number.
var1,var2,var3=input("enter three no separated by comma:").split(",")
l=[var1,var2,var3]
print(l)
print(tuple(l))



# write a program that accept a sentence and calculate the number of upper case and lower case letters.
import re

count = 0
s = "Hello world"
p = re.compile(r"[A-Z]")
result = p.findall(s)
print(result)
for i in result:
    count+= 1
print(count)

c=0
s = "Hello world"
p = re.compile(r"[a-z]")
result = p.findall(s)
print(result)
for i in result:
    c+= 1
print(c)


#4.
n=8
def rec(x):
    if(x==1 or x==0):
        return 1
    else:
        f=x*rec(x-1)
        return f
print(rec(n))


#write a python program to check an entered string is a python keyword or not,if it is keyword print with a message and if it is not it  will display all the keywords of python.
n=int(input("enter any number"))
import keyword
k=keyword.kwlist
print(k)
for i in k:
	if i==n:
		print("keyword")
	else:
		print(k)
		
	
	
	