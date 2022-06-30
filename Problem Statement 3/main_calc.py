from ast import Try
from cgitb import text
from tkinter import *
from tkinter import messagebox
from math import pi, e, sin, cos, tan, log
import tkinter.font
import random
import math
from datetime import date






window = Tk()

window.geometry("722x400")
window.resizable(0, 0)
window.title("Calcualtor")

icon = PhotoImage(file="./images/logo2.png")

window.iconphoto(False, icon)
window.iconbitmap("./images/logo2.ico")



cal = Frame(window, width=300, height=500)
cal.grid()
cal.config(bg='#f0f0f0')
equation = StringVar()

# Area to input the equation
input_area = Entry(cal, textvariable=equation, width=60, font=("Comic Sans MS", 15), bd=10, justify=LEFT, state=DISABLED,
             disabledbackground="white", disabledforeground="black")
input_area.insert(0, "0")
input_area.grid(row=0, columnspan=8)

font = tkinter.font.Font(size=12, weight="bold", family='Helvetica',)


def about():
    messagebox.showinfo(
        'About', "\n \n \n   Made by : Chetan Chinchulkar   \n Institute : IIT Guwahati \n Branch : Engineering Physics \n \n")


def standard():
    window.geometry('361x400')
    input_area['width'] = 28
    input_area.grid(row=0, columnspan=4, sticky=EW)
    window.title("Standard Calculator")

def scientific():
    window.geometry('722x400')
    input_area['width'] = 60
    input_area.grid(row=0, columnspan=8)
    window.title("Scientific Calculator")

def sgn(a):
    return 1 if a>0 else -1 if a<0 else 0

def age_cal():
    import age_calculator

new_menu = Menu(window)
filemenu = Menu(new_menu, tearoff=0)
new_menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command=standard)
filemenu.add_command(label="Scientific", command=scientific)
filemenu.add_separator()
filemenu.add_command(label="Age Calculator", command=age_cal)
filemenu.add_separator()
filemenu.add_command(label="About", command=about)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
window.config(menu=new_menu)


value = ""
ans = ""
expression = ""
history = {}


h = 2
w = 7
actvbgnd = 'white'
bg1 = 'wheat3'
bg2 = "burlywood1"
bg3 = "burlywood2"
bg4 = "tan1"
fg1 = "white"
fg2 = "black"

numberpad = [7, 8, 9, 4, 5, 6, 1, 2, 3]

class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.createWidgets()

    def clearall(self):
        global expression
        global equation
        global value
        global ans
        expression=''
        value=''
        ans=''
        equation.set(expression)

    def clearback(self):
        result1=""
        result2=""
        global equation
        global expression
        global value
        global ans

        expression = input_area.get()
        temp1= list(expression)    
        temp2= list(value)
            
        if value=='':
            temp1=[]
            temp2=[]
        elif expression[-5:] in ["asin(","acos(","atan("]:
            for _ in range(5):temp1.pop()
            for _ in range(10):temp2.pop()
    
        elif expression[-4:]=="log(":
            for _ in range(4):temp1.pop()
            for _ in range(11):temp2.pop()
            
        elif expression[-4:] in ['sin(','cos(','tan(']:
            for _ in range(4): temp1.pop()
            for _ in range(9): temp2.pop()
        
        elif expression[-4:]=='sgn(':
            for _ in range(4): temp1.pop()
            for _ in range(4): temp2.pop()
            
        elif expression[-3:]=='ln(':
            for _ in range(3):temp1.pop()
            for _ in range(9): temp2.pop()
            
        elif expression[-2:]=='e^':
            for _ in range(2):temp1.pop()
            for _ in range(8): temp2.pop()
            
        elif expression[-1]=='^':
            for _ in range(1):temp1.pop()
            for _ in range(2): temp2.pop()

        elif expression[-1]=="√":
            for _ in range(1):temp1.pop()
            for _ in range(10):temp2.pop()
            
        elif expression[-1]=='π':
            for _ in range(1):temp1.pop()
            for _ in range(7): temp2.pop()
            
        elif expression[-1]=='e':
            for _ in range(1):temp1.pop()
            for _ in range(6): temp2.pop() 

        elif expression[-1]=='%':
            for _ in range(1):temp1.pop()
            for _ in range(4): temp2.pop()      
            
        else: 
            temp1.pop()
            temp2.pop()
            
        for element in range(len(temp1)):
            result1+=temp1[element]
        expression = result1
        equation.set(expression)
            
        for element in range(len(temp2)):
            result2+=temp2[element]
            
        value=result2
        try:ans = str(eval(value))
        except:pass
    
    def pressbtn(self,num):
        global expression 
        global value
        global ans
        expression = expression + str(num)
        equation.set(expression)
        if num in ["1","2","3","4","5","6","7","8","9","0","(",")","00"]:
            value += num
            try:ans = str(eval(value))
            except:ans = "Invalid Expression"
            
        elif num in ["+",'-','/','*','.','1/','sgn(']:
            value += num
            
        elif num in ['asin(','acos(','atan(','sin(','cos(','tan(']:
            value += 'math.'+ num
        
        elif num=='^':value += '**'
        
        elif num=='%':
            value += '/100'
            try:ans = str(eval(value))
            except:ans = "Invalid Expression"
        elif num=='^2':
            value += '**2'
            try:ans = str(eval(value))
            except:ans = "Invalid Expression"
        elif num=='^3':
            value += '**3'
            try:ans = str(eval(value))
            except:ans = "Invalid Expression"

        elif num=='√(':value += 'math.sqrt('
        
        elif num=='e':
            value += 'math.e'
            try:ans = str(eval(value))
            except:ans = "Invalid Expression"
        elif num=='π':
            value += 'math.pi'
            try:ans = str(eval(value))
            except:ans = "Invalid Expression"
        elif num=='log(':value += 'math.log10('
        elif num=='ln(':value += 'math.log('
        elif num=='e^':value += 'math.e**'


    def equal_calc(self):
        global expression
        global ans
        global value

        # print(expression)
        # print(ans)
        # print(value)

        if expression=='':
            messagebox.showerror("Error", "Please enter an expression")
        else:
            try:
                ans = str(eval(value))
                equation.set(ans)
                history[expression] = ans

                # print(result)
                messagebox.showinfo("Result", expression + " = " + str(ans))
                ans=''
                value=''
                expression=''
            except Exception as err:
                
                # messagebox.showerror("Calculation Error", err)
                messagebox.showerror("Calculation Error", "ERROR...")
                equation.set("ERROR...")

    def copy_res(self):
        global expression
        
        if expression=='':
                messagebox.showerror("Error", "Please enter an expression")
        else:
            import subprocess
            subprocess.run("pbcopy",universal_newlines=True, input=input_area.get())
            messagebox.showinfo("Copied", "Result copied to clipboard")

    def rand(self):
        # input_area.config(text= random.random())
        global ans
        global expression
        global value

        ans = (random.random())
        expression = str(ans)
        value = str(ans)
        equation.set(ans)

    def check_history(self):
        history_text = []
        for key,value in history.items():
            history_text.append(key + " : " + value)
        
        if history_text==[]:
            messagebox.showinfo("History", "No calculations done yet")
        else:
            messagebox.showinfo("History", "\n".join(history_text))

    def createWidgets(self):
        # self.display = Entry(self, font=("Helvetica", 16), borderwidth=0, relief=RAISED, justify=RIGHT)
        # self.display.insert(0, "0")
        # self.display.grid(row=0, column=0, columnspan=5)

        i=0
        for j in range(3):
            for k in range(3):
                Button(cal,command  = lambda x = str(numberpad[i]) : self.pressbtn(x), text = str(numberpad[i]), bg= bg1, fg=fg2,activebackground=actvbgnd,
                    height=h, width=w,font= font).grid(row=j+2,column=k)
                i+=1

        r=5
        c=7
        Button(cal,command  = lambda: self.pressbtn('0'),  text = "0", bg= bg1, fg=fg2, activebackground = actvbgnd, 
                        height=h, width=w,font= font).grid(row=r,column= c-7)

        Button(cal,command  = lambda: self.pressbtn('00'),text = "00", bg= bg1, fg=fg2, activebackground = actvbgnd, 
                        height=h, width=w,font= font).grid(row=r,column= c-6)

        Button(cal,command  = self.clearback,            text = "C", bg= bg2, fg=fg2, activebackground = actvbgnd, 
                        height=h, width=w,font= font).grid(row=r-4,column= c-7)

        Button(cal,command  = self.clearall,              text = "AC",bg= bg2, fg=fg2, activebackground = actvbgnd, 
                        height=h, width=w,font= font).grid(row=r-4,column= c-6)

        Button(cal,command  = lambda: self.pressbtn('.'), text = "•", bg= bg3, fg=fg2, activebackground = actvbgnd, 
                        height=h, width=w,font= font).grid(row=r,column=c-5)

        Button(cal,command  = lambda: self.pressbtn('+'), text = "+", bg= bg3, fg=fg2, activebackground = actvbgnd, 
                        height=h, width=w,font= font).grid(row=r-2,column=c-4)

        Button(cal,command  = lambda: self.pressbtn('-'),  text = "–", bg= bg3, fg=fg2, activebackground = actvbgnd, 
                        height=h, width=w,font= font).grid(row=r-3,column=c-4)

        Button(cal,command  = lambda: self.pressbtn('/'),   text = "/", bg= bg3, fg=fg2, activebackground = actvbgnd, 
                        height=h, width=w,font= font).grid(row=r-4,column=c-5)

        Button(cal,command  = lambda: self.pressbtn('*'),  text = "✶", bg= bg3, fg=fg2, activebackground = actvbgnd, 
                        height=h, width=w,font= font).grid(row=r-4,column=c-4)

        Button(cal,command  = self.equal_calc,   text = "=", bg= bg2, fg=fg2, activebackground = actvbgnd, 
                        height=3*h,width=w,font= font,pady=10).grid(row=r-1,column=c-4,rowspan=2,)
        
        Button(cal,command  = self.rand,  text = "Rand", bg= bg3, fg=fg2, activebackground = actvbgnd, 
                        height=h, width=w,font= font).grid(row=r+1,column=c-7)

        Button(cal,command  = self.copy_res,  text = "Copy Result", bg= bg3, fg=fg2, activebackground = actvbgnd, 
                        height=h, width=w ,font= font).grid(row=r+1,column=c-6)
        
        Button(cal,command  = self.check_history,  text = "Check History", bg= bg3, fg=fg2, activebackground = actvbgnd, 
                        height=h, width=2*w ,font= font).grid(row=r+1,column=c-5,columnspan=2)



        list1=['(',')','%','asin','sin','log','x^2','acos','cos','ln','x^3','atan','tan','e^x','1/x','x^y','e',"π",'√x','sgn']
        list2=['(',')','%','asin(','sin(','log(','^2','acos(','cos(','ln(','^3','atan(','tan(','e^','1/','^','e',"π",'√(','sgn(']
        i=0
        for j in range(5):
            for k in range(4):
                Button(cal,command  = lambda x= list2[i]: self.pressbtn(x),  text = list1[i], bg=bg4,  fg= fg2,activebackground=actvbgnd,
                    height=h,width=w,font= font).grid(row=j+1,column=k+4)
                i+=1

        msize=60
        cal.rowconfigure(0,minsize=50)
        for i in range(1,6):
            cal.rowconfigure(i,minsize=60)

        msize = 90
        for i in range(8): 
            cal.columnconfigure(i,minsize= msize)
    

     

app = Application(window)	

window.mainloop()
