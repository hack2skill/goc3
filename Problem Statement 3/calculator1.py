from tkinter import *

def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator=""
    text_Input.set("")

def btnEquals():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
cal=Tk()
cal.title("Calculator")
operator=""
text_Input=StringVar()
txtDisplay= Entry(cal, font=('arial', 20, 'bold'), textvariable= text_Input, bd=30, insertwidth= 3, bg= "#FFFFFF", justify="right").grid(columnspan=4)

##################################################################################################################################################
button7= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='7', command= lambda:btnClick(7))
button7.grid(row=1, column=0)

button8= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='8', command= lambda:btnClick(8))
button8.grid(row=1, column=1)

button9= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='9', command= lambda:btnClick(9))
button9.grid(row=1, column=2)

buttonAdd= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20 , 'bold'), text='+', command= lambda:btnClick("+"))
buttonAdd.grid(row=1, column=3)

##################################################################################################################################################
button4= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='4', command= lambda:btnClick(4))
button4.grid(row=2, column=0)

button5= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='5', command= lambda:btnClick(5))
button5.grid(row=2, column=1)

button6= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20 , 'bold'), text='6 ', command= lambda:btnClick(6))
button6.grid(row=2, column=2)

buttonSub= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='-', command= lambda:btnClick("-"))
buttonSub.grid(row=2, column=3)

##################################################################################################################################################
button1= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='1', command= lambda:btnClick(1))
button1.grid(row=3, column=0)

button2= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='2', command= lambda:btnClick(2))
button2.grid(row=3, column=1)

button3= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='3', command= lambda:btnClick(3))
button3.grid(row=3, column=2)

buttonMul= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20 , 'bold'), text='X', command= lambda:btnClick("*"))
buttonMul.grid(row=3, column=3)

##################################################################################################################################################
button0= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='0', command= lambda:btnClick(0))
button0.grid(row=4, column=0)

buttonClr= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20 , 'bold'), text='C', command= lambda:btnClear())
buttonClr.grid(row=4, column=1)

buttonequal= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='=', command= lambda:btnEquals())
buttonequal.grid(row=4, column=2)

buttonDiv= Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='/', command= lambda:btnClick("/"))
buttonDiv.grid(row=4, column=3)





cal.mainloop()
