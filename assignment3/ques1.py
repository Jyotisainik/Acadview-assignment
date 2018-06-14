#Create a list with user defined inputs.
l=[2,3,4,6]
l[0]=int(input("enter a number"))
l[1]=int(input("enter a number"))
l[2]=int(input("enter a number"))
l[3]=int(input("enter a number"))
print(l)

#Add the following list to above created list:['google",apple",facebook",microsoft",tesla'].
l1=["google","apple","facebook","microsoft","tesla"]
l2=[2,3,4,6]
l=(l1+l2)
print(l)

l=[1,3,5,6,6,1,3,4]
print(l.count(6))

#create a list with numbers and sort it in ascending order
l=[5,3,6,7,8,9]
l.sort()
print(l)

a=[2,5,3,4,6]
b=[5,6,8,3,2]
a.sort()
b.sort()
print(a)
print(b)
c=a+b
c.sort()
print(c)


l1=[]
l1.append(int(input("enter any no:")))
l1.append(int(input("enter any no:")))
l1.append(int(input("enter any no:")))
print(l1)
print("stack")
l1.pop()
print(l1)
print("queue")
del l1[0]
print(l1)
l1.append(int(input("enter any no:")))
l1.append(int(input("enter any no:")))
print(l1)
print("stack")
l1.pop()
print(l1)
print("queue")
del l1[0]
print(l1)

v=0
n=0
q=[3,4,5,6,7]
print("liset",q)
for a in range(0,5):
	if q[a]%2==0:
	   v=v+1
	if q[a]%2!=0:
	   n=n+1
print("the odd no is in list",n)
print("the even no is in list",v)










