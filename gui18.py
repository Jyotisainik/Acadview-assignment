#Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.
import tkinter
from tkinter import *
d={9584958498:'Jyoti',8675848586:'Harman',4637728383:'Radhika',3748596234:'Aanchal',8697853482:'Tammana'}
root=Tk()
root.geometry("200x50")
mylist=Listbox(root,yscrollcommand=Scrollbar.set)
mylist.pack(side=RIGHT,fill=BOTH)
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=mylist.yview)
for i in d:
    mylist.insert(END,d[i])
root.resizable(False,False)
root.mainloop()


#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.
#entry

d={9584958498:'Jyoti',8675848586:'Harman',4637728383:'Radhika',3748596234:'Aanchal',8697853482:'Tammana'}
root=Tk()
root.geometry("300x300")
mylist=Listbox(root,yscrollcommand=Scrollbar.set)
mylist.place(x=50,y=50)
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=mylist.yview)
for i in d:
    mylist.insert(END,d[i])
entry1=Entry(root,width=20)
entry1.place(x=40,y=230)
entry2=Entry(root,width=20)
entry2.place(x=40,y=250)
root.resizable(False,False)
def show():
    k=entry1.get()
    v=entry2.get()
    d[k]=v
    mylist.insert(END,k)
b=Button(root,text="click",width=20,command=show)
b.place(x=20,y=270)
root.mainloop()