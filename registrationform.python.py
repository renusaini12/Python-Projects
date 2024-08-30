from tkinter import*
import sqlite3 as s
from tkcalendar import DateEntry
root = Tk()
root.title('MY GUI')
root.minsize(800,900)

name1=StringVar()
name2=StringVar()
name3=StringVar()
name4=StringVar()
name5=StringVar()
name6=StringVar()


def dis():
    n1=name1.get()
    n2=name2.get()
    n3=name3.get()
    n4=name4.get()
    n5=name5.get()
    n6=name6.get()

    
    print(n1)
    print(n2)
    print(n3)
    print(n4)
    print(n5)
    print(n6)
    
    c = e3.get()
    print("DOB",c)
    
    
    con = s.connect("Registration.db")
    with con:
        cur = con.cursor()
    cur.execute("create table if not exists student(id integer primary key,\
                Name text,Father_name text,Mother_name text,DOB text,\
                    Email text,Contect text,Address text,Language text,Gender \
                        text,State text)")


    
    con.commit()
    con.close()

l1 = Label(root,text ='Registration Form For Admission',
           font =('arial',30,'bold'),bg ='orange',fg ='black',width=60)
l1.place(x=0,y=0)

l2 = Label(root,text ='Candidate Name:',font =('arial',18,'bold'),bg ='orange',fg ='black',width=18)
l2.place(x=50,y=100)

e1 = Entry(root,textvariable=name1,font=('arial',20,'bold'),width = 40,bg='white')
e1.place(x=450,y=100)

l3 = Label(root,text ='Candidate Father Name:',font =('arial',18,'bold'),bg ='orange',fg ='black',width=18)
l3.place(x=50,y=160)

e2 = Entry(root,textvariable=name2,font=('arial',20,'bold'),width = 40,bg='white')
e2.place(x=450,y=160)

l17 = Label(root,text ='Candidate Mother Name:',font =('arial',18,'bold'),bg ='orange',fg ='black',width=18)
l17.place(x=50,y=220)

e17 = Entry(root,textvariable=name6,font=('arial',20,'bold'),width = 40,bg='white')
e17.place(x=450,y=220)


l4 = Label(root,text ='Date of Birth:',font =('arial',18,'bold'),bg ='orange',fg ='black',width=18)
l4.place(x=50,y=280)

e3 = DateEntry(root,font=('arial',18,'bold'),width = 45,bg='white')
e3.place(x=450,y=280)

l5 = Label(root,text ='Email id:',font =('arial',18,'bold'),bg ='orange',fg ='black',width=18)
l5.place(x=50,y=340)

e4 = Entry(root,textvariable=name3,font=('arial',20,'bold'),width = 40,bg='white')
e4.place(x=450,y=340)

l6 = Label(root,text ='Mobile Number:',font =('arial',18,'bold'),bg ='orange',fg ='black',width=18)
l6.place(x=50,y=400)

e5 = Entry(root,textvariable=name4,font=('arial',20,'bold'),width = 40,bg='white')
e5.place(x=450,y=400)

l7 = Label(root,text ='Adress:',font =('arial',18,'bold'),bg ='orange',fg ='black',width=18)
l7.place(x=50,y=460)

e6 = Entry(root,textvariable=name5,font=('arial',20,'bold'),width = 40,bg='white')
e6.place(x=450,y=460)

l8 = Label(root,text ='Language:',font =('arial',18,'bold'),bg ='orange',fg ='black',width=18)
l8.place(x=50,y=520)

var1 = StringVar()
var2 = StringVar()
l9 = Checkbutton(root,text='Hindi',variable=var1,font="time 15")
l9.place(x=500 ,y=520)

l10 = Checkbutton(root,text='English',variable=var2,font="time 15")
l10.place(x=650 ,y=520)

l11 = Label(root,text ='Gender:',font =('arial',18,'bold'),bg ='orange',fg ='black',width=18)
l11.place(x=50,y=580)

gen=IntVar()
l12 = Radiobutton(root,text='Male',variable=gen,font="time 15",value=1)
l12.place(x=500,y=580)

l13 = Radiobutton(root,text='Female',variable=gen,font="time 15",value=2)
l13.place(x=650,y=590)

l14 = Label(root,text ='State:',font =('arial',18,'bold'),bg ='orange',fg ='black',width=18)
l14.place(x=50,y=640)


lists = ["Andhra Pradesh","Haryana","Nagaland","Uttarakhand","Odisha","Madhya Pardesh"
         ,"Maharashtra","Punjab","Bihar","Chhattisgarh","Goa","Gujrat","Karnataka"]
listroom = StringVar(root)
listroom.set("Select Your State Type")
menu = OptionMenu(root,listroom,*lists)
menu.place(x=450,y=640,width=450)


l16 = Button(root,text ='Submit',font =('arial',20,'bold'),bg ='red',fg ='white',width=10,command=dis)
l16.place(x=350,y=680)

root.mainloop()