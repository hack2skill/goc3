from tkinter import*
import math
import parser
import speech_recognition as sr

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClear():
     global operator
     operator=""
     text_Input.set("")

def btnequal():
    global operator
    if(operator=='🔊'):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = "0"
        sumup=str(eval(text))
    elif(operator[0]=='s'):
        val = operator[3:]
        sumup = str(math.sin(eval(val)))
    elif(operator[0]=='c'):
        val = operator[3:]
        sumup = str(math.cos(eval(val)))
    elif(operator[0]=='l'):
        val = operator[3:]
        sumup = str(math.log(eval(val)))
    elif(operator[0]=='e'):
        val = operator[1:]
        sumup = str(pow(2.718281828459045,eval(val)))    
    else:
        sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
class Calc():
    def _init_(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False

def numberEnter(self,num):
  self.result=False
  firstnum=txtDisplay.get()
  secondnum=str(num)
  if self.input_value:
      self.current=secondnum
      self.input_value=False
  else:
      if secondnum =='.':
          if secondnum in firstnum:
              return
      self.current=firstnum+secondnum
  self.display(self.current)

def e(self):
    self.result=False
    self.current=math.e
    self.disolay(self.current)
    
added_value=Calc()




cal=Tk()
cal.title("Calculator")
operator=""
text_Input=StringVar()



txtDisplay=Entry(cal,font=('comic sans',20,'bold'),textvariable=text_Input, bd=30, insertwidth=4,bg="grey",justify='right').grid(columnspan=4)

#********************************************************************************************************************************************************************

btn7=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="(",bg="light blue",command=lambda:btnClick('(')).grid(row=1,column=0)
btn8=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text=")",bg="light blue",command=lambda:btnClick(')')).grid(row=1,column=1)
btn9=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text=".",bg="light blue",command=lambda:btnClick('.')).grid(row=1,column=2)
Addition=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="🔊",bg="light grey",command=lambda:btnClick('🔊')).grid(row=1,column=3)

#********************************************************************************************************************************************************************


btn7=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="7",bg="light blue",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="8",bg="light blue",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="9",bg="light blue",command=lambda:btnClick(9)).grid(row=2,column=2)
Addition=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text=" + ",bg="light grey",command=lambda:btnClick('+')).grid(row=2,column=3)


#********************************************************************************************************************************************************************


btn4=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="4",bg="light blue",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="5",bg="light blue",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="6",bg="light blue",command=lambda:btnClick(6)).grid(row=3,column=2)
Substraction=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text=" -  ",bg="light grey",command=lambda:btnClick('-')).grid(row=3,column=3)


#********************************************************************************************************************************************************************


btn1=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="1",bg="light blue",command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="2",bg="light blue",command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="3",bg="light blue",command=lambda:btnClick(3)).grid(row=4,column=2)
Multiply=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text=" x ",bg="light grey",command=lambda:btnClick('*')).grid(row=4,column=3)


#********************************************************************************************************************************************************************


btn0=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="0",bg="light blue",command=lambda:btnClick(0)).grid(row=5,column=0)
btnclear=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="C",bg="light blue",command=btnClear).grid(row=5,column=1)
btnequal=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text="=",bg="light blue",command=btnequal).grid(row=5,column=2)
division=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text=" /  ",bg="light grey",command=lambda:btnClick('/')).grid(row=5,column=3)


#********************************************************************************************************************************************************************


btns=Button(cal,padx=16,bd=8,fg="red",font=('comic sans',20,'bold'),text="sin",bg="light grey",command=lambda:btnClick('sin')).grid(row=6,column=0)
btnc=Button(cal,padx=16,bd=8,fg="red",font=('comic sans',20,'bold'),text="cos",bg="light grey",command=lambda:btnClick('cos')).grid(row=6,column=1)
btnl=Button(cal,padx=16,bd=8,fg="red",font=('comic sans',20,'bold'),text="log",bg="light grey",command=lambda:btnClick('log')).grid(row=6,column=2)
exp=Button(cal,padx=30,bd=8,fg="red",font=('comic sans',20,'bold'),text=" e ",bg="light grey",command=lambda:btnClick('e')).grid(row=6,column=3)









cal.mainloop()
