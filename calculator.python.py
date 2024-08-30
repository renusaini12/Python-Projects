from tkinter import *
root = Tk()
root.title('Caculator')

operator=""
txt_input=StringVar()

root.geometry("361x400+588+288")

def btnCLK(number):
    global operator
    operator=operator+str(number)
    txt_input.set(operator)
    
    
def btnClrDisp():
    global operator
    operator= "" 
    txt_input.set("")


def equalSum():
    global operator
    sums=str(eval(operator))
    txt_input.set(sums)
    operator=sums


display = Entry(root,font=('arial',40,'bold'),bg='powderblue',bd = 20,width=11
                ,justify="right",textvariable=txt_input)
display.grid(row=0,columnspan=2)

l1 = Button(root,text ='7',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK(7))
l1.place(x=0,y=120)

l2 = Button(root,text ='4',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK(4))
l2.place(x=0,y=190)

l3 = Button(root,text ='1',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK(1))
l3.place(x=0,y=260)

l4 = Button(root,text ='c',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=btnClrDisp)
l4.place(x=0,y=330)

l5 = Button(root,text ='8',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK(8))
l5.place(x=90,y=120)

l6 = Button(root,text ='5',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK(5))
l6.place(x=90,y=190)

l7 = Button(root,text ='2',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK(2))
l7.place(x=90,y=260)

l8 = Button(root,text ='0',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK(0))
l8.place(x=90,y=330)

l9 = Button(root,text ='9',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK(9))
l9.place(x=180,y=120)

l10 = Button(root,text ='6',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK(6))
l10.place(x=180,y=190)

l11 = Button(root,text ='3',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK(3))
l11.place(x=180,y=260)

l12 = Button(root,text ='=',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black'
             ,width=4,command=equalSum)
l12.place(x=180,y=330)

l13 = Button(root,text ='+',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK("+"))
l13.place(x=270,y=120)

l14 = Button(root,text ='-',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK("-"))
l14.place(x=270,y=190)

l15 = Button(root,text ='*',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK("*"))
l15.place(x=270,y=260)

l16 = Button(root,text ='/',font =('arial',20,'bold'),bd=10,bg ='white',fg ='black',width=4,command=lambda:btnCLK("/"))
l16.place(x=270,y=330)


root.mainloop()