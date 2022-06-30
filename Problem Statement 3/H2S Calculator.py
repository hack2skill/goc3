
#This a Basic Calculator program that uses tkinter framework which internally uses python
#Author: Shiva Kumar Terala
#submitted to:Hack2skill GAME OF CODES


#NOTE: Here "%" works for Modulation and Not for Percentage


from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font
from functools import partial
import math
import time



#create Root window
root=tkinter.Tk()

#create Window Title and dimensions
root.title("Calculator Project Hack2skill")
root.geometry("410x520")

expression=""
click=False


#this function will display the user's input on to the screen and updates expression value
def btnOnClick(data):
    global expression
    expression=expression+str(data)
    label1.config(text=expression)

def plusminus():
    global expression
    global click
    sample=expression
    if(click==False):
        print("clicked")
        label1.config(text="")
        expression="(-"+expression+")"
        label1.config(text=expression)
        click=True
    if(click):
        click=False
        expression=sample
        label1.config(text=expression)


#this function clears the screen
def clear():
    label1.config(text="")
    global expression
    expression=""
    
#this function works as backspace
def clearentry():
    global expression
    label1.config(text=expression[:len(expression)-1])
    expression=expression[:len(expression)-1]   
 
#calculate square root   
def sqroot():
    global expression
    label1.config(text="\u221A"+expression)
    try:
        label1.config(text="\u221A"+expression)
        time.sleep(1)
        expression=math.sqrt(int(expression))
        label1.config(text=expression)
    except:
        label1.config(text="Error")

#this function will display final output    
def equals():
    global expression
    if expression=="":
        label1.config(text="Error")
    try:
        ans=str(eval(expression))
        label1.config(text=ans)
        expression=""
    except:
        if(expression!=""):
            label1.config(text="Error")
#this function is to calculate "1/something"    
def oneby():
    global expression
    label1.config(text="")
    ans=str(eval("1/"+expression))
    label1.config(text=ans)
    expression=""
    

#Adding Buttons to the frame

#%button
button1=Button(root, text = "%", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("%"))
button1.place(x = 10, y = 160, width = 90, height = 52)


#1/x button
button2 = Button(root, text = "1/x",bg="#860cff", font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:oneby())
button2.place(x = 10, y = 220, width = 90, height = 52)

#7 button
button3 = Button(root, text = "7", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("7"))
button3.place(x = 10, y = 280, width = 90, height = 52)

#4 button
button4 = Button(root, text = "4", bg="#860cff",font = tkinter.font.Font(family ="Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("4"))
button4.place(x = 10, y = 340, width = 90, height = 52)

#1 button
button5 = Button(root, text = "1", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("1"))
button5.place(x = 10, y = 400, width = 90, height = 52)

#+/- button
button6 = Button(root, text = "+-", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:plusminus())
button6.place(x = 10, y = 460, width = 90, height = 52)

#CE button
button7 = Button(root, text = "CE",fg="#ffffff", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:clearentry())
button7.place(x = 110, y = 160, width = 90, height = 52)

#Backspace button
button8 = Button(root, text="\u232B",bg="#ffc53c",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:clearentry())
button8.place(x = 310, y = 160, width = 90, height = 52)

#Clear Button
button9 = Button(root, text="C", bg="#860cff" ,fg="#ffffff",font = tkinter.font.Font(family ="Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:clear())        
button9.place(x = 210, y = 160, width = 90, height = 52)

#Square button
button10 = Button(root, text="x\u00B2", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("**"))
button10.place(x = 110, y = 220, width = 90, height = 52)

#8 button
button11 = Button(root, text="8", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("8"))
button11.place(x = 110, y = 280, width = 90, height = 52)

#5 button
button12 = Button(root, text="5", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("5"))
button12.place(x = 110, y = 340, width = 90, height = 52)

#2 button
button13 = Button(root, text="2", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("2"))
button13.place(x = 110, y = 400, width = 90, height = 52)

#0 button
button14 = Button(root, text="0", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("0"))
button14.place(x = 110, y = 460, width = 90, height = 52)

#square root button
button15 = Button(root, text="\u221Ax", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:sqroot())
button15.place(x = 210, y = 220, width = 90, height = 52)

#9 button
button16 = Button(root, text="9", bg="#860cff",font = tkinter.font.Font(family ="Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("9"))
button16.place(x = 210, y = 280, width = 90, height = 52)

#6 button
button17 = Button(root, text="6", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("6"))
button17.place(x = 210, y = 340, width = 90, height = 52)

#3 button
button18 = Button(root, text="3", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("3"))
button18.place(x = 210, y = 400, width = 90, height = 52)

#. buttton
button19 = Button(root, text=".", bg="#860cff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("."))
button19.place(x = 210, y = 460, width = 90, height = 52)
        
#divide button
button20 = Button(root, text="\u00F7", bg="#ffc53c",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("/"))
button20.place(x = 310, y = 220, width = 90, height = 52)

#multipy button
button21 = Button(root, text="X", bg="#ffc53c",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("*"))
button21.place(x = 310, y = 280, width = 90, height = 52)

#subtract button
button22 = Button(root, text="\u2212", bg="#ffc53c",font = tkinter.font.Font(family ="Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("-"))
button22.place(x = 310, y = 340, width = 90, height = 52)

#addition button
button23 = Button(root, text="\u002B", bg="#ffc53c",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:btnOnClick("+"))
button23.place(x = 310, y = 400, width = 90, height = 52)
        
#equals button
button24 = Button(root, text="=",bg="#ff0000", fg="#ffffff",font = tkinter.font.Font(family = "Microsoft Sans Serif", size = 16), cursor = "arrow", state = "normal",command=lambda:equals())
button24.place(x = 310, y = 460, width = 90, height = 52)

#current expression Label
label1 = Label(root, text=expression,font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 20), cursor = "arrow", state = "normal")
label1.place(x = 260, y = 50, width = 170, height = 42)
label1.pack(padx=50,pady=80,side="right",anchor="nw")



root.mainloop()



