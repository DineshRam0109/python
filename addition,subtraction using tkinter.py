from tkinter import *

s=Tk()
s.geometry("400x400")
y=Frame(s)
y.pack(pady=55)
x=Label(y,text="First Number",font=50,anchor=CENTER)
x.pack(padx=20,side=LEFT)
a=Entry(y,selectbackground="red")#############FIRST ENTRY
a.pack(padx=20,side=LEFT)
c=Frame(s)
c.pack()
x=Label(c,text="Second Number",font=50)
x.pack(pady=10,padx=5,side=LEFT)
b=Entry(c)############SECOND ENTRY
b.pack(padx=10,side=LEFT)
d=Frame(s)
d.pack(padx=10,pady=20)
def add():
    num1=int(a.get())
    num2=int(b.get())
    i.insert(0,str(num1+num2))
def subtract():
    num1=int(a.get())
    num2=int(b.get())
    i.insert(0,str(num1-num2))

e=Button(d,text="ADD",width=5,activeforeground="yellow",activebackgroun="red",command=add)
e.pack(padx=40,side=LEFT)
f=Button(d,text="SUBSTRACT",width=9,activeforeground="yellow",activebackground="red",command=subtract)
f.pack(pady=10,side=LEFT)
g=Frame(s)
g.pack()
h=Label(g,text="Result",font=50)
h.pack()
i=Entry(g,width=25)###THIRD ENTRY
i.pack()


