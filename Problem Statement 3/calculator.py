
import tkinter
from tkinter import *
from tkinter import messagebox

operator= ""
val=""
A = 0


def B1_clicked():
    global val
    val=val+"1"
    data.set(val)

def B2_clicked():
    global val
    val=val+"2"
    data.set(val)

def B3_clicked():
    global val
    val=val+"3"
    data.set(val)

def B4_clicked():
    global val
    val=val+"4"
    data.set(val)

def B5_clicked():
    global val
    val=val+"5"
    data.set(val)

def B6_clicked():
    global val
    val=val+"6"
    data.set(val)


def B7_clicked():
    global val
    val=val+"7"
    data.set(val)

def B8_clicked():
    global val
    val=val+"8"
    data.set(val)

def B9_clicked():
    global val
    val=val+"9"
    data.set(val)

def B0_clicked():
    global val
    val=val+"0"
    data.set(val)

def BP_clicked():
    global A
    global operator
    global val
    A= int(val)
    operator= "+"
    val= val + "+"
    data.set(val)

def BM_clicked():
    global A
    global operator
    global val
    A= int(val)
    operator= "-"
    val= val + "-"
    data.set(val)

def BML_clicked():
    global A
    global operator
    global val
    A= int(val)
    operator= "*"
    val= val + "*"
    data.set(val)

def BD_clicked():
    global A
    global operator
    global val
    A= int(val)
    operator= "/"
    val= val + "/"
    data.set(val)

def c_clicked():
    global A
    global operator
    global val
    val=""
    A=0
    operator=""
    data.set(val)

def result():
    global A
    global operator
    global val
    val2 =val
    if operator == "+":
        x=int((val2.split("+")[1]))
        C= A + x
        data.set(C)
        val = str(C)
    elif operator == "-":
        x=int((val2.split("-")[1]))
        C= A - x
        data.set(C)
        val = str(C)
    elif operator == "*":
        x=int((val2.split("*")[1]))
        C= A * x
        data.set(C)
        val = str(C)
    elif operator == "/":
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("Error","Value can not be divided by 0")
            A=""
            val=""
            data.set(val)
        else:
            C=  int(A/x)
            data.set(C)
            val = str(C)



root = tkinter.Tk()
root.geometry("200x300+300+300")
#root.resizable(0,0)
root.title("Calculator")

data=StringVar()
lbl=Label(root, text= " ", anchor= SE,font= ("bold",26), textvariable= data,
bg="#ffffff")
lbl.pack(expand= True, fill="both")

brow1 = Frame(root)
brow1.pack(expand= True, fill="both")

brow2 = Frame(root)
brow2.pack(expand= True, fill="both")

brow3 = Frame(root)
brow3.pack(expand= True, fill="both")

brow4 = Frame(root)
brow4.pack(expand= True, fill="both")


btn1 = Button(
    brow1, text="1", font= ("bold",22)
    ,relief= GROOVE, border=0, command =B1_clicked
)
btn1.pack(side = LEFT, expand=True,fill="both")

btn2 = Button(
    brow1, text="2", font= ("bold",22),relief= GROOVE, border=0,command =B2_clicked
)
btn2.pack(side = LEFT, expand=True,fill="both")

btn3 = Button(
    brow1, text="3", font= ("bold",22),relief= GROOVE, border=0, command =B3_clicked
)
btn3.pack(side = LEFT, expand=True,fill="both")

btn4 = Button(
    brow1, text="+", font= ("bold",22),relief= GROOVE, border=0, command =BP_clicked
)
btn4.pack(side = LEFT, expand=True,fill="both")



btn1 = Button(
    brow2, text="4", font= ("bold",22),relief= GROOVE, border=0,command =B4_clicked
)
btn1.pack(side = LEFT, expand=True,fill="both")

btn2 = Button(
    brow2, text="5", font= ("bold",22),relief= GROOVE, border=0,command =B5_clicked
)
btn2.pack(side = LEFT, expand=True,fill="both")

btn3 = Button(
    brow2, text="6", font= ("bold",22),relief= GROOVE, border=0,command =B6_clicked
)
btn3.pack(side = LEFT, expand=True,fill="both")

btn4 = Button(
    brow2, text="-", font= ("bold",22),relief= GROOVE, border=0, command =BM_clicked
)
btn4.pack(side = LEFT, expand=True,fill="both")





btn1 = Button(
    brow3, text="7", font= ("bold",22),relief= GROOVE, border=0,command =B7_clicked
)
btn1.pack(side = LEFT, expand=True,fill="both")

btn2 = Button(
    brow3, text="8", font= ("bold",22),relief= GROOVE, border=0,command =B8_clicked
)
btn2.pack(side = LEFT, expand=True,fill="both")

btn3 = Button(
    brow3, text="9", font= ("bold",22),relief= GROOVE, border=0,command =B9_clicked
)
btn3.pack(side = LEFT, expand=True,fill="both")

btn4 = Button(
    brow3, text="*", font= ("bold",22),relief= GROOVE, border=0,command =BML_clicked
)
btn4.pack(side = LEFT, expand=True,fill="both")





btn1 = Button(
    brow4, text="c", font= ("bold",22),relief= GROOVE, border=0, command=c_clicked
)
btn1.pack(side = LEFT, expand=True,fill="both")

btn2 = Button(
    brow4, text="0", font= ("bold",22),relief= GROOVE, border=0,command =B0_clicked
)
btn2.pack(side = LEFT, expand=True,fill="both")

btn3 = Button(
    brow4, text="=", font= ("bold",22),relief= GROOVE, border=0, command= result
)
btn3.pack(side = LEFT, expand=True,fill="both")

btn4 = Button(
    brow4, text="/", font= ("bold",22),relief= GROOVE, border=0, command =BD_clicked
)
btn4.pack(side = LEFT, expand=True,fill="both")


root.mainloop()