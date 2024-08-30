from tkinter import*
r = Tk()
r.geometry("500x400")

name = StringVar()

def dis():
    n1=name.get()
    print(n1)
   
l1 = Label(r,text ="Name")
l1.place(x=100,y=100)

e1 = Entry(r,textvariable = name)
e1.place(x=200,y=100)

b1 = Button(r,text ="print",command=dis)
b1.place(x=150,y=150)


r.mainloop()