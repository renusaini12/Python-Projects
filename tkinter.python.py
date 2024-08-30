from tkinter import *
root = Tk()
root.title('MY GUI')
root.minsize(800,900)

l1 = Label(root,text ='Registration form',
           font =('arial',40,'bold'),bg ='blue',fg ='white',width=45)
l1.place(x=0,y=0)

l2 = Label(root,text ='Name:',font =('arial',20,'bold'),bg ='blue',fg ='white')
l2.place(x=50,y=100)

e1 = Entry(root,font=('arial',20,'bold'),width = 50,bg='lightgray')
e1.place(x=300,y=100)

l3 = Label(root,text ='Father name:',font =('arial',20,'bold'),bg ='blue',fg ='white')
l3.place(x=50,y=180)

e2 = Entry(root,font=('arial',20,'bold'),width = 50,bg='lightgray')
e2.place(x=300,y=180)

l4 = Label(root,text ='Mother name:',font =('arial',20,'bold'),bg ='blue',fg ='white')
l4.place(x=50,y=260)

e3 = Entry(root,font=('arial',20,'bold'),width = 50,bg='lightgray')
e3.place(x=300,y=260)

l5 = Label(root,text ='Roll No:',font =('arial',20,'bold'),bg ='blue',fg ='white')
l5.place(x=50,y=350)

e4 = Entry(root,font=('arial',20,'bold'),width = 50,bg='lightgray')
e4.place(x=300,y=350)

l6 = Label(root,text ='DOB:',font =('arial',20,'bold'),bg ='blue',fg ='white')
l6.place(x=50,y=430)

e5 = Entry(root,font=('arial',20,'bold'),width = 50,bg='lightgray')
e5.place(x=300,y=430)

l7 = Label(root,text ='Address:',font =('arial',20,'bold'),bg ='blue',fg ='white')
l7.place(x=50,y=520)

e6 = Entry(root,font=('arial',20,'bold'),width = 50,bg='lightgray')
e6.place(x=300,y=520)

l8 = Button(root,text ='Submit',font =('arial',20,'bold'),bg ='blue',fg ='white')
l8.place(x=300,y=580)


root.mainloop()