from tkinter import *

def btnClick(number):
    global operator
    operator=operator+str(number)
    strrvar.set(operator)

def btnClear():
    global operator
    operator=''
    strvar.set(operator)

def result():
    global opearator
    res=str(eval(operator))
    strvar.set(res)

root=Tk()
root.title("Calculator")
operator=''
strvar=StringVar()

ent=Entry(root,width=50, bd=5, font=
