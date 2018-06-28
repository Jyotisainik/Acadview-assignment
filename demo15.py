#Q.1- Write a Python program to read last n lines of a file.
c=0
count_line=0
n=int(input("enter the no of lines"))
f=open('demotest.txt','r')
for line in f:
    count_line=count_line+1
m=count_line-n
f.seek(0)
for line in f:
    c+=1
    if c>m:
        print(line)


#Q.2- Write a Python program to count the frequency of words in a file.
f=open('demotest.txt','r')
d={}
for word in f.read().split():
    if word not in d:
        d[word]=1
    else:
        d[word]+=1
for i,j in d.items():
    print(i,j)


#Q.3- Write a Python program to copy the contents of a file to another file
with open('demotest.txt','r')as f1:
    with open('demo1test.txt','w')as f2:
        for line in f1:
             f2.write(line)


#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

with open('dimtest.txt','r') as f1:
    c1=f1.readlines()
with open('dim1test.txt','r') as f1:
    c2=f1.readlines()
i=0
for a in c1:
    print(c1[i]+c2[i])
    i=i+1



#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import random
with open('dimtest.txt','w') as f:
    for x in range(10):
        n = random.randint(0,9)
        f.write(str(n))
        f.write("\n")

with open('dimtest.txt','r') as f:
    l = f.readlines()

l.sort()

with open('dim1test.txt','w') as f:
    for n in l:
        f.write(n)
        f.write("\n")

