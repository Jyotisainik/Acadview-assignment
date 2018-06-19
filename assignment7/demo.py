#1.
def circle(r):
    area=3.14*r*r
    return (area)
area=circle(4)
print("area of the circle",area)

#2.
p=[]
def perfect():
	for x in range(1,1000):
		li=[]
		sum=0
		for y in range(1,x):
			if(x%y==0):
				li.append(y)
		for a in li:
			sum=sum+a
		if(sum==x):
			p.append(x)
perfect()
print(p)

#3.
n=12
i=1
def mul(n,i):
    if  (i>10):
        return 0
    else:
        print("%d*%d=%d"%(n,i,n*i))
        mul(n,i+1)

mul(n,i)

#4.
def power(b,p):
	s=1
	if p==1:
		return b
	else:
		s=b*power(b,p-1)
		return s
print(power(5,3))

#5.
def fact(x):
	if x==1:
		return 1
	else:
		x=x*fact(x-1)
		return x
n=int(input("enter the number :"))
f=fact(n)
print(f)
d={}
d[n]=f
print(d)








