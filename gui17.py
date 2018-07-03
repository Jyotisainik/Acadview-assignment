#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
import tkinter
from tkinter import *
root=Tk()
import sys
root.title("MyApp")
root.geometry("250x250")
root.resizable(False,False)
root.minsize(200,200)
root.maxsize(300,300)
label=Label(root,text='hello world',fg='blue',bg='white')
label.pack()
b=Button(text='exit',width=25,command='exit',borderwidth=5)
b.place(x=40,y=100)
root.mainloop()

#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.
root=Tk()
root.title("MyApp")
def DIS():
    label2 = Label(root, text='JYOTI'fg='blue', bg='white')
    label2.place(x=40,y=50)
root.geometry("250x250")
root.resizable(False,False)
root.minsize(200,200)
root.maxsize(300,300)
label=Label(root,text='HELLO',fg='blue',bg='white')
label.place(x=40,y=0)
b=Button(text='show',width=25,command=DIS,borderwidth=5)
b.place(x=40,y=100)
root.mainloop()


#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
root=Tk()
def show():
    label = Label(f1, text='show', fg='blue', bg='white')
    label.grid(row=3,column=1)
f1=Frame(root)
f1.grid(row=0,column=1)
root.title("MyApp")
root.geometry("250x250")
root.resizable(False,False)
root.minsize(200,200)
root.maxsize(300,300)
b=Button(f1,text="click",width=20,command=show)
b.grid(row=0,column=1)
b1=Button(f1,text="exit",width=20,command=exit)
b1.grid(row=0,column=2)
root.mainloop()



#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.
#entry
def show():
    t1=entry.get()
    label = Label(root, text=t1, fg='blue', bg='white')
    label.place(x=40,y=100)
root=Tk()
root.geometry("250x250")
entry=Entry(root,width=20)
entry.pack()
b=Button(root,text="click",width=20,command=show)
b.place(x=40,y=150)
root.mainloop()


