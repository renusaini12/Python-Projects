from tkinter import*
import tkinter as tk
from tkinter import ttk
import random
from tkinter import PhotoImage
root = tk.Tk()
root.title('Restaurant Mangement')
root.minsize(800,900)



Order = StringVar()
Cost = StringVar()
Pizza = StringVar()
Subtotal = StringVar()
Burger =  StringVar()
Tex =  StringVar()
Icecream =  StringVar()
Service =  StringVar()
Drinks =  StringVar()
Total =  StringVar()

Order.set(random.randint(1, 101))


def pri():
    Or = Order.get()
    Co = Cost.get()
    Pi = Pizza.get()
    Sub = Subtotal.get()
    Bur = Burger.get()
    Ta = Tex.get()
    Ice = Icecream.get()
    Ser = Service.get()
    Dri = Drinks.get()
    To = Total.get()


    
    print(Or)
    print(Co)
    print(Pi)
    print(Sub)
    print(Bur)
    print(Ta)
    print(Ice)
    print(Ser)
    print(Dri)
    print(To)

    
    Cost1 = int(Pi)*240 + int(Bur)*125 + int(Ice)*80 + int(Dri)*60
    Cost.set(Cost1)
    
    tax1 = Cost1*15/100
    Tex.set(tax1)
    
    Service.set(50)
    
    Subtotal.set(tax1+50)
    
    Total.set(Cost1+tax1+50)
    
def Reset():
    Order.set(random.randint(1, 101))   
    Cost.set("")
    Pizza.set("")
    Subtotal.set("")
    Burger.set("")
    Tex.set("")
    Icecream.set("")
    Service.set("")
    Drinks.set("")
    Total.set("")
    
def Exit():
    root.destroy()     
    
def popup():
    win = Tk()
    win.title("Feedback Form")
    win.geometry("600x600")
    
        
    
    var1=StringVar()

    def Submit():
        
        mm=var1.get()
        l1=""
        if(mm==1):
            l1="Exellent"
        elif(mm==2):
            l1 ="Good"
        elif(mm==3):
            l1 ="Average"
        elif(mm==4):
            l1= "Poor"
        
        print(l1)


    l1 = Label(win,text ='Thanks For Visiting',font=('arial',25,'bold'),bg='Red',fg='white',width=30)
    l1.place(x=0,y=0)
    
    l2 = Label(win,text ='We are glad you choose us! Please tell us how it was!',font =('arial',14,'bold'),fg ='black')
    l2.place(x=50,y=50)
    
    l3 = Label(win,text ='Name',font =('arial',14,'bold'),fg ='black')
    l3.place(x=30,y=150)
    
    e3 = Entry(win,font=('arial',12,'bold'),bg='white',fg='black',width=18,bd=5,)
    e3.place(x=30,y=200)
    
    l4 = Label(win,text ='E-mail',font =('arial',14,'bold'),fg ='black')
    l4.place(x=400,y=150)
    
    e4 = Entry(win,font=('arial',12,'bold'),bg='white',fg='black',width=18,bd=5,)
    e4.place(x=400,y=200)
    
    l4 = Label(win,text ='How would you rate us?',font =('arial',14,'bold'),fg ='black')
    l4.place(x=50,y=250)
    

    
    l5 = Radiobutton(win,text='Excellent',font=('arial',12),variable=var1,value=1)
    l5.place(x=50 ,y=300)
    
    l6 = Radiobutton(win,text='Good',font=('arial',12),variable=var1,value=2)
    l6.place(x=200 ,y=300)
    
    l7 = Radiobutton(win,text='Average',font=('arial',12),variable=var1,value=3)
    l7.place(x=350 ,y=300)
    
    l8 = Radiobutton(win,text='Poor',font=('arial',12),variable=var1,value=4)
    l8.place(x=500 ,y=300)
    
    l9 = Label(win,text ='Comments',font =('arial',14,'bold'),fg ='black')
    l9.place(x=50,y=350)
    
    e9 = Entry(win,font=('arial',30,'bold'),bg='white',fg='black',width=20,bd=5)
    e9.place(x=50,y=400)
    
    l10 = Button(win,text ='Submit',font =('arial',14,'bold'),bg ='green',fg ='white',
                 command=Submit)
    l10.place(x=180,y=500)
    
    l11 = Button(win,text ='Cancel',font =('arial',14,'bold'),bg ='Red',fg ='white')
    l11.place(x=280,y=500)
    
def popup121():
    window121 = Tk()
    window121.title("Menu Card")
    window121.geometry("200x200")    
    
    l1 = Label(window121,text ='ITEM LIST',font =('arial',12,'bold'),fg ='black')
    l1.place(x=0,y=0)
    
    l2 = Label(window121,text ='PRICES',font =('arial',12,'bold'),fg ='black')
    l2.place(x=120,y=0)
    
    l3 = Label(window121,text ='Pizza',font =('arial',12),fg ='black')
    l3.place(x=10,y=30)
    
    l4 = Label(window121,text ='burger',font =('arial',12),fg ='black')
    l4.place(x=10,y=70)
    
    l5 = Label(window121,text ='icecream',font =('arial',12),fg ='black')
    l5.place(x=10,y=110)
   
    l6 = Label(window121,text ='drinks',font =('arial',12),fg ='black')
    l6.place(x=10,y=150)
    
    l7 = Label(window121,text ='240',font =('arial',12),fg ='black')
    l7.place(x=120,y=30)
    
    l8 = Label(window121,text ='125',font =('arial',12),fg ='black')
    l8.place(x=120,y=70)

    l1 = Label(window121,text ='80',font =('arial',12),fg ='black')
    l1.place(x=120,y=110)
    
    l1 = Label(window121,text ='60',font =('arial',12),fg ='black')
    l1.place(x=120,y=150)


image_path = PhotoImage(file=r"D:\Renu saini\python work\restarent\pic1.png")
bg_image=Label(root,image=image_path,width=1366)
bg_image.pack()


rightframe = Frame(root,width=1200,height=400)
rightframe.place(x=600,y=400)


my_tree = ttk.Treeview(rightframe)
my_tree['columns'] = ('ordno.','piz','bur','ice','dr','ct','tx','ser','st','ttl')

horizontal_bar= ttk.Scrollbar(rightframe,orient='horizontal')
horizontal_bar.configure(command=my_tree.xview)
my_tree.configure(xscrollcommand=horizontal_bar.set)
horizontal_bar.pack(fill=X,side=BOTTOM)


vertical_bar= ttk.Scrollbar(rightframe,orient='vertical')
vertical_bar.configure(command=my_tree.yview)
my_tree.configure(yscrollcommand=vertical_bar.set)
vertical_bar.pack(fill=Y,side=RIGHT)


# defining columns for table

my_tree.column('#0', width=0,minwidth=0)
my_tree.column('ordno.',anchor=CENTER, width=60,minwidth=25)
my_tree.column('piz',anchor=CENTER, width=60,minwidth=25)
my_tree.column('bur',anchor=CENTER, width=60,minwidth=25)
my_tree.column('ice',anchor=CENTER, width=60,minwidth=25)
my_tree.column('dr',anchor=CENTER, width=60,minwidth=25)
my_tree.column('ct',anchor=CENTER, width=60,minwidth=25)
my_tree.column('tx',anchor=CENTER, width=60,minwidth=25)
my_tree.column('ser',anchor=CENTER, width=60,minwidth=25)
my_tree.column('st',anchor=CENTER, width=60,minwidth=25)
my_tree.column('ttl',anchor=CENTER, width=60,minwidth=25)


# defing heading for table

my_tree.heading('ordno.',text='Order no.',anchor=CENTER)
my_tree.heading('piz',text='Pizza',anchor=CENTER)
my_tree.heading('bur',text='Burger',anchor=CENTER)
my_tree.heading('ice',text='Icecream',anchor=CENTER)
my_tree.heading('dr',text='Drink',anchor=CENTER)
my_tree.heading('ct',text='Cost',anchor=CENTER)
my_tree.heading('tx',text='Tax',anchor=CENTER)
my_tree.heading('ser',text='Service',anchor=CENTER)
my_tree.heading('st',text='Subtotal',anchor=CENTER)
my_tree.heading('ttl',text='Total',anchor=CENTER)    
my_tree.pack()
        

l1 = Label(root,text ='Restaurant Mangement System',
           font =('arial',30,'bold'),bg ='Red',fg ='white',width=60)
l1.place(x=0,y=0)

l2 = tk.Button(root,text ='Feedback Form',font =('arial',14,'bold'),bg ='green',fg ='white',command=popup)
l2.place(x=10,y=70)

l3 = Button(root,text ='Menu Card',font =('arial',14,'bold'),bg ='green',fg ='white',command=popup121)
l3.place(x=1200,y=70)

l4 = Label(root,text ='Order No.',font =('arial',12,'bold'),fg ='black')
l4.place(x=10,y=165)

e4 = Entry(root,font=('arial',12,'bold'),bg='white',fg='black',width=8,bd=5,textvariable=Order)
e4.place(x=100,y=160)

l5 = Label(root,text ='Cost',font =('arial',12,'bold'),fg ='black')
l5.place(x=200,y=165)

e5 = Entry(root,font=('arial',12,'bold'),bg='white',fg='black',width=12,bd=5,textvariable=Cost)
e5.place(x=290,y=160)

l6 = Label(root,text ='Pizza',font =('arial',12,'bold'),fg ='black')
l6.place(x=10,y=210)

e6 = Entry(root,font=('arial',12,'bold'),bg='white',fg='black',width=8,bd=5,textvariable=Pizza)
e6.place(x=100,y=210)


l7 = Label(root,text ='Burger',font =('arial',12,'bold'),fg ='black')
l7.place(x=10,y=260)

e7 = Entry(root,font=('arial',12,'bold'),bg='white',fg='black',width=8,bd=5,textvariable=Burger)
e7.place(x=100,y=260)

l8 = Label(root,text ='Tax',font =('arial',12,'bold'),fg ='black')
l8.place(x=200,y=210)

e8 = Entry(root,font=('arial',12,'bold'),bg='white',fg='black',width=12,bd=5,textvariable=Tex)
e8.place(x=290,y=210)

l7 = Label(root,text ='Subtotal',font =('arial',12,'bold'),fg ='black')
l7.place(x=200,y=310)

e7 = Entry(root,font=('arial',12,'bold'),bg='white',fg='black',width=12,bd=5,textvariable=Subtotal)
e7.place(x=290,y=310)

l9 = Label(root,text ='Ice Cream',font =('arial',12,'bold'),fg ='black')
l9.place(x=10,y=310)

e9 = Entry(root,font=('arial',12,'bold'),bg='white',fg='black',width=8,bd=5,textvariable=Icecream)
e9.place(x=100,y=310)

l10 = Label(root,text ='Service',font =('arial',12,'bold'),fg ='black')
l10.place(x=200,y=260)

e10 = Entry(root,font=('arial',12,'bold'),bg='white',fg='black',width=12,bd=5,textvariable=Service)
e10.place(x=290,y=260)

l11 = Label(root,text ='Drinks',font =('arial',12,'bold'),fg ='black')
l11.place(x=10,y=360)

e11 = Entry(root,font=('arial',12,'bold'),bg='white',fg='black',width=8,bd=5,textvariable=Drinks)
e11.place(x=100,y=360)

l12 = Label(root,text ='Total',font =('arial',12,'bold'),fg ='black')
l12.place(x=200,y=360)

e12 = Entry(root,font=('arial',12,'bold'),bg='white',fg='black',width=12,bd=5,textvariable=Total)
e12.place(x=290,y=360)

l13 = Button(root,text ='Total',font =('arial',14,'bold'),bg ='green',fg ='white',width=10,command=pri)
l13.place(x=15,y=500)

l14 = Button(root,text ='Reset',font =('arial',14,'bold'),bg ='green',fg ='white',width=10,command=Reset)
l14.place(x=155,y=500)

l15 = Button(root,text ='Exit the System',font =('arial',14,'bold'),bg ='green',fg ='white',width=12,command=Exit)
l15.place(x=295,y=500)

l16 = Label(root,text ='Date & Time-Tue Mar 19 11:08:18 2024 ',font =('arial',14,'bold'),bg ='Red',fg ='white',width=30)
l16.place(x=50,y=600)

l17 = Button(root,text ='Delete Record',font =('arial',14,'bold'),bg ='green',fg ='white',width=12)
l17.place(x=1180,y=320)

l17 = Button(root,text ='Add Record',font =('arial',14,'bold'),bg ='green',fg ='white',width=12)
l17.place(x=1000,y=320)

root.mainloop()