#1.what is time tuple.
import time
print(time.localtime())
#index		Attributes	values             
 #1          tm_mon      1 to 12
 #2          tm_mday     1 to 31
 #3          tm_hour     0 to 23
 #4          tm_min      0 to 59
 #5          tm_sec      0 to 61
 #6          tm_wday     0 to 6 
 #7          tm_yday     1 to 366
 #8          tm_isdst    -1,0,1

#2.write a program to get formatted file.
import time
print(time.asctime(time.localtime(time.time())))

#3.extract month from the time.
import datetime
d=(datetime.date.today())
print(d.month)

#4.extract day from the time.
from datetime import datetime
d=datetime.now()
print("day",d.strftime("%A"))

#5. Extract date (ex : 11 in 11/01/2021) from the time. 
import datetime
#from datetime import date
d=datetime.date.today()
print(d.day)

#6- Write a program to print time using local time method.
import time
print(time.localtime())

#7.find the factorial of a function input by user using math package function.
n=int(input("enter any number"))
import math
print(math.factorial(n))

#8.find the GCD of the number input by user using math package function.
n=int(input("enter any number"))
m=int(input("enter any number"))
import math
print(math.gcd(m,n))

#9- Use OS package and do the following tasks: 
#1. Get current working directory.
#2. Get the user environment.
import os
print(os.getcwd())
print(os.environ)

