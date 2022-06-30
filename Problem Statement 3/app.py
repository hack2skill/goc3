#importing necessary modules
import tkinter as tk
import math
from tkinter import *

#Tkinter window setting with dimentions as 600*700
window = Tk()
window.geometry("650x700")
window.title("PyCalc")
icon = PhotoImage(file = "./calculator.png")
window.iconphoto(True, icon)
tk.Label(window, text="Python GUI Calculator with History", font=('Sans 18'), pady = 10).pack()
tk.Label(window, text="github.com/atombalan", font=('Sans 10'), pady = 5).pack()


#setting scrollbar for smooth UI
scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill = Y)
expression = ""
history = Text(window, wrap = None, yscrollcommand = scrollbar.set)
scrollbar.config(command=history.yview)

#USER INPUT FUNCTION
def butttonClicked(item):
    global expression
    expression = expression + str(item)
    inputText.set(expression)

def butttonClearEntry():
    global expression
    expression = expression[:-1]
    inputText.set(expression)

#EVALUVATION OF EXPRESSION and STORING
def butttonEqual():
    global expression
    try:
        result = str(eval(expression))
        inputText.set(result)
        hist = str(expression) + " = " + result + "\n"
        history.insert(END, hist)
    except:
        result = "Error!"
        inputText.set(result)
        hist = str(expression) + " = " + result + "\n"
        history.insert(END, hist)
    expression = ""

#INPUT EXPRESSION
inputText = StringVar()
inputFrame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "white", highlightcolor = "black", highlightthickness = 1)
inputFrame.pack(side = TOP)
inputField = Entry(inputFrame, font = ('Roboto', 18, 'bold'), textvariable = inputText, width = 50, bg = "#fff", bd = 0, justify = RIGHT)
inputField.grid(row = 0, column = 0)
inputField.pack(ipady = 10, pady = 3)

#BUTTONS
# frame for buttons
buttonsFrame = Frame(window, width = 312, height = 272.5, bg = "white")
buttonsFrame.pack()
piValue = Button(buttonsFrame, text = "π", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("math.pi")).grid(row = 0, column = 0, padx = 3, pady = 3)
factorial = Button(buttonsFrame, text = "x!", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("math.factorial(")).grid(row = 0, column = 1, padx = 3, pady = 3)
bracket1 = Button(buttonsFrame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("(")).grid(row = 0, column = 2, padx = 3, pady = 3)
bracket2 = Button(buttonsFrame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked(")")).grid(row = 0, column = 3, padx = 3, pady = 3)
modulo = Button(buttonsFrame, text = "%", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("%")).grid(row = 0, column = 4, padx = 3, pady = 3)
clearEntry = Button(buttonsFrame, text = "CE", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClearEntry()).grid(row = 0, column = 5, padx = 3, pady = 3)

eValue = Button(buttonsFrame, text = "e", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("math.e")).grid(row = 1, column = 0, padx = 3, pady = 3)
log = Button(buttonsFrame, text = "ln", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("math.log(")).grid(row = 1, column = 1, padx = 3, pady = 3)
seven = Button(buttonsFrame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#f1f3f4", cursor = "hand2", command = lambda: butttonClicked(7)).grid(row = 1, column = 2, padx = 3, pady = 3)
eight = Button(buttonsFrame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#f1f3f4", cursor = "hand2", command = lambda: butttonClicked(8)).grid(row = 1, column = 3, padx = 3, pady = 3)
nine = Button(buttonsFrame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#f1f3f4", cursor = "hand2", command = lambda: butttonClicked(9)).grid(row = 1, column = 4, padx = 3, pady = 3)
divide = Button(buttonsFrame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("/")).grid(row = 1, column = 5, padx = 3, pady = 3)

sine = Button(buttonsFrame, text = "sin", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("math.sin(")).grid(row = 2, column = 0, padx = 3, pady = 3)
log10 = Button(buttonsFrame, text = "log", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("math.log10(")).grid(row = 2, column = 1, padx = 3, pady = 3)
four = Button(buttonsFrame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#f1f3f4", cursor = "hand2", command = lambda: butttonClicked(4)).grid(row = 2, column = 2, padx = 3, pady = 3)
five = Button(buttonsFrame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#f1f3f4", cursor = "hand2", command = lambda: butttonClicked(5)).grid(row = 2, column = 3, padx = 3, pady = 3)
six = Button(buttonsFrame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#f1f3f4", cursor = "hand2", command = lambda: butttonClicked(6)).grid(row = 2, column = 4, padx = 3, pady = 3)
multiply = Button(buttonsFrame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("*")).grid(row = 2, column = 5, padx = 3, pady = 3)

cosine = Button(buttonsFrame, text = "cos", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("math.cos(")).grid(row = 3, column = 0, padx = 3, pady = 3)
squareroot = Button(buttonsFrame, text = "√", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("math.sqrt(")).grid(row = 3, column = 1, padx = 3, pady = 3)
one = Button(buttonsFrame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#f1f3f4", cursor = "hand2", command = lambda: butttonClicked(1)).grid(row = 3, column = 2, padx = 3, pady = 3)
two = Button(buttonsFrame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#f1f3f4", cursor = "hand2", command = lambda: butttonClicked(2)).grid(row = 3, column = 3, padx = 3, pady = 3)
three = Button(buttonsFrame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#f1f3f4", cursor = "hand2", command = lambda: butttonClicked(3)).grid(row = 3, column = 4, padx = 3, pady = 3)
minus = Button(buttonsFrame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("-")).grid(row = 3, column = 5, padx = 3, pady = 3)

tangent = Button(buttonsFrame, text = "tan", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("math.tan(")).grid(row = 4, column = 0, padx = 3, pady = 3)
xPowery = Button(buttonsFrame, text = u"exp", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("**")).grid(row = 4, column = 1, padx = 3, pady = 3)
zero = Button(buttonsFrame, text = "0", fg = "black", width = 10, height = 3, bd = 0, bg = "#f1f3f4", cursor = "hand2", command = lambda: butttonClicked(0)).grid(row = 4, column = 2, padx = 3, pady = 3)
point = Button(buttonsFrame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#f1f3f4", cursor = "hand2", command = lambda: butttonClicked(".")).grid(row = 4, column = 3, padx = 3, pady = 3)
equals = Button(buttonsFrame, text = "=", fg = "white", width = 10, height = 3, bd = 0, bg = "#4285f4", cursor = "hand2", command = lambda: butttonEqual()).grid(row = 4, column = 4, padx = 3, pady = 3)
plus = Button(buttonsFrame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#dadce0", cursor = "hand2", command = lambda: butttonClicked("+")).grid(row = 4, column = 5, padx = 3, pady = 3)


tk.Label(window, text="History:", font=('Sans'), pady = 10).pack()

#HISTORY DISPLAY
history.pack()

#APP RUN LOOP
window.mainloop()




