#Q.1- Extract the user id, domain name and suffix from the following email addresses.
#emails = "zuck26@facebook.com" "page33@google.com"
#"jeff42@amazon.com"
import re
a="zuck26@facebook.com"
b="page33@google.com"
c="jeff42@amazon.com"
print(re.findall(r'(.+)@(.+)\.(.+)',a),end="")
print(re.findall(r'(.+)@(.+)\.(.+)',b),end="")
print(re.findall(r'(.+)@(.+)\.(.+)',c),end="")


#Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
import re
s="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
p=re.compile(r"b[a-z]+")
result=p.findall(s)
for r in result:
    print(r)

s = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
p = re.compile(r"B[a-z]+")
result = p.findall(s)
for r in result:
    print(r)

# Q.3- Split the following irregular sentence into words
#sentence = "A, very very; irregular_sentence"
#desired_output = "A very very irregular sentence.
import re
s="A, very very; irregular_sentence"
p=re.sub(r","," ",s)
p=re.sub(r";"," ",p)
p=re.sub(r"_"," ",p)
print (p)



#optional Q.1- Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
# tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
# desired_output = 'Good advice What I would do differently if I was learning to code today'
import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
p=re.sub(r"! RT @TheNextWeb:"," ",tweet)
p=re.sub(r"http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"," ",p)
print(p)


