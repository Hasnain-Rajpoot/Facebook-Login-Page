import tkinter as tk
from tkinter import *
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename,os
import random
y=tk.Tk()
y.geometry("350x500")
y.configure(bg="white")
y.title("login page")
fb=Label(y,text="facebook",fg="blue",width=9,bg="white",font="comiscansms 30 bold").pack(pady=70)
def o():
            global p
            p=""
            for i in range(5):
                a=random.randrange(1,9)
                a=str(a)
                p=a+p  
            tk.messagebox.showerror("verification cod","your OTP  "+p)
def log():
    ne1=e1.get()
    ne2=e2.get()
    f=open("fb_login_data.txt","r")
    data = f.read()
    m = []
    table = []
    sum = 0
    a = data.split("\n")
    a.pop()
    print(a)

    for i in range(0, len(a)):
        table.append(a[i].split(","))
    found=False    
    for l in range(0, len(table)):
                if ne1 ==table[l][0] and ne2==table[l][1]:
                    print(table[l])
                    tk.messagebox.showerror("congragulation","successfully login")
                    found=True
    if found==False:
        tk.messagebox.showerror("error","password or email is incorrect")
#fuctions
def new():
    x=tk.Tk()
    x.geometry("350x600")
    x.configure(bg="white")
    def sign():       
        f=open("fb_login_data.txt","a")
        n=en1.get()
        n1=en2.get()
        n2=en3.get()
        n3=en4.get()
        n4=en5.get()
        n5=en6.get()
        n6=en7.get()
        n9=e9.get()
        n9=str(n9)
        if n=="":
            tk.messagebox.showerror("error","please enter the first name")
        elif n1=="":
            tk.messagebox.showerror("error","please enter the syr name")
        elif n2=="":
            tk.messagebox.showerror("error","please enter the Emai") 
        elif n3=="":
            tk.messagebox.showerror("error","please enter the password")
        elif n4=="":
            tk.messagebox.showerror("error","please enter the day")
        elif n5=="":
            tk.messagebox.showerror("error","please enter the Month")
        elif n6=="":
            tk.messagebox.showerror("error","please enter the Year")
        elif n9=="":
            tk.messagebox.showerror("error","please enter verification code")
        elif n9 != p:
            tk.messagebox.showerror("error","please enter verification code is incorrect")            
        else:
            f.write(n2)
            f.write(",")  
            f.write(n3)
            f.write(",")
            f.write(n)
            f.write(",") 
            f.write(n1)
            f.write(",")  
            f.write(n4)
            f.write(".")  
            f.write(n5)
            f.write(".")
            f.write(n6)  
            f.write("\n")
            f.close()
            tk.messagebox.showerror("congragulation","new account successfully created")      
    #labels
    b2=Label(x,text="facebook",fg="blue",width=9,bg="white",font="comiscansms 30 bold").pack(padx=20)
    b3=Label(x,text="create a new account",fg="black",bg="white",font="comiscansms 15 bold").pack(padx=20)
    b4=Label(x,text="it,s quick and easy",fg="black",bg="white").pack()
    x.title("create New account")
#entries
    b4=Label(x,text="first name",fg="black",bg="white").pack()
    nam=StringVar()
    en1=Entry(x,textvariable=nam,width=30,bd=2)
    en1.pack(pady=4)
    b4=Label(x,text="surname",fg="black",bg="white").pack()
    name2=StringVar()
    #name2.set("password")
    en2=Entry(x,textvariable=name2,width=30,bd=2)
    en2.pack(pady=4)
    b4=Label(x,text="mobile number or Email",fg="black",bg="white").pack()
    mail=StringVar()
    #mail.set("Email")
    en3=Entry(x,textvariable=mail,width=30,bd=2)
    en3.pack(pady=4)
    b4=Label(x,text="New password",fg="black",bg="white").pack(anchor="n")
    password2=StringVar()
    #password2.set("password")
    en4=Entry(x,textvariable=password2,width=30,bd=2)
    en4.pack(pady=4)
#date of birth
    b4=Label(x,text="Date of Birth?",fg="black",bg="white").pack()
    day=StringVar()
    en5=Entry(x,textvariable=day,width=4,bd=2)
    en5.place(x=80,y=340)
    b4=Label(x,text="day",fg="black",bg="white").place(x=50,y=340)
    month=StringVar()
    en6=Entry(x,textvariable=month,width=4,bd=2)
    en6.place(x=180,y=340)
    b4=Label(x,text="month",fg="black",bg="white").place(x=130,y=340)
    year=StringVar()
    en7=Entry(x,textvariable=year,width=4,bd=2)
    en7.place(x=260,y=340)
    b4=Label(x,text="year",fg="black",bg="white").place(x=220,y=340)

    #gender
    t2=IntVar()
    t3=IntVar()
    b4=Label(x,text="Gender?",fg="black",bg="white").place(x=130,y=380)
    female=Checkbutton(x,text="female",variable=t2,bg="white").place(x=80,y=410)
    male=Checkbutton(x,text="male",variable=t3,bg="white").place(x=220,y=410)
    b4=Label(x,text="verfication code",fg="black",bg="white").place(x=130,y=440)
    otp=IntVar()
    e9=Entry(x,textvariable=otp,width=30,bd=2)
    e9.place(x=80,y=460)
    signup=tk.Button(x,text="sign up",bg="green",fg="white",width=15,command=sign).place(x=50,y=490)
    ot=tk.Button(x,text="get OTP",bg="green",fg="white",width=15,command=o).place(x=190,y=490)    
#enteries

email=StringVar()
email.set("Email")
e1=Entry(y,textvariable=email,width=30,bd=2)
e1.pack(pady=20)
password=StringVar()
password.set("password")
e2=Entry(y,textvariable=password,width=30,bd=2)
e2.pack()

#buttons
b=tk.Button(y,text="Log in",bg="blue",fg="white",width=27,command=log).pack(pady=8)
create=tk.Button(y,text="create New account",fg="blue",width=15,command=new).pack(pady=8)
forget=tk.Button(y,text="forget password",bg="green",fg="white",width=15).pack(pady=8)

y.mainloop()
