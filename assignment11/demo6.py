#1.
import threading
from threading import Thread
import time
def display():
		time.sleep(5)
		print("hello world")
t=Thread(target=display)
t.start()	

#2.
import threading 
from threading import Thread
import time
def table():
	for i in range(1,11):
		t.join()
		print(i)
		time.sleep(1)
t1=Thread(target=table)
t1.start()

#3.
l=[1,2,3,4,5]
def dis():
	for i in l:
		t1.join()
		j=2
		print(i)
		time.sleep(j)
		j=j+2
t2=Thread(target=dis)
t2.start()		

#4.
def fact():
	n=int(input("enter any number"))
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	print(fact)
t3=Thread(target=fact)
t3.start()
	
	
	
		



