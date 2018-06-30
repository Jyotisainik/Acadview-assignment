#welcoming the user.
x="welcome"
print(x)
import time
#wait for one second.
time.sleep(1)
print("loading...")
time.sleep(5)
print("start gusseing")

import random
l=['JYOTI','RADHIKA','AANCHAL','HARMAN']
random.shuffle(l)
answer=l[0]
comp_answer=list(answer)  #typecast str to list
print("guess the any girls name:")

d=[]
d.extend(comp_answer)
count=0
count2=0
for i in range(len(d)):
    d[i]=" - "
print("".join(d))

while count<len(comp_answer):
    if count2 < 10:
        print("chances left:",10-count2)
        count2 += 1
        guess=input("guess a letter:")
        guess=guess.upper()
        for i in range (len(comp_answer)):
            if comp_answer[i]==guess:
                d[i]=guess        #insertion
                count+=1
        print("".join(d)) #typecas
    else:
        print("you loose")
        exit(0)
print("you won")
