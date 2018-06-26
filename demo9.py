#1.
a=3
if  a<4:
    a=a/(a-3)
print(a)
# #errorname=ZeroDivisionError: division by zero

#
try:
	a=3
	if a<4:
		a=a/(a-3)
except Exception:
	print("Expextion")
 #output=exception



#Q.2- Name and handle the exception occurred in the following program:
l=[1,2,3]
print(l[3])
l=[1,2,3]
print(l[3])
 #errorname=IndexError: list index out of range

 #2.
try:
    l=[1,2,3]
    print(l[3])
except Exception:
    print("exception")


 #3.
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not
 #output=NameError: Hi there
 #raise NameError("Hi there")  # Raise Error
 #An exception

 #4.
 #Function which returns a/b
# def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

 # Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

 #output=-5.0
 #a/b result in 0

#Q.5- Write a program to show and handle following exceptions:
#1. Import Error
#2. Value Error
#3. Index Error
#import error
try:
    import abc
    print("import error")
except Exception as e:
    print(e)

#index error
try:
    l=[1,2,3,4]
    print(l[5])
except Exception:
    print("index error")

 #value error
try:
    z=int("abcd")
except Exception as a:
   print(a)



#4.Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
#  The code must keep taking input till the user enters the appropriate age number(less than 18).
class AgeTooSmallError(Exception):
    pass
while True:
        try:
            age = int(input("enter any age"))
            if (age<=18):
                print("age is too small")
            else:
                raise AgeTooSmallError("enter an age above 18")
        except Exception as q:
            print(q)













