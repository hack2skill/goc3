import tkinter as tk
from math import *

# used to switch between units of rad, and deg
cons = 1
f = 1

obj = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#777777',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#888888"
}


def fsin(arg):
    return sin(arg * cons)


def fcos(arg):
    return cos(arg * cons)


def ftan(arg):
    return tan(arg * cons)


def arcsin(arg):
    return f * (asin(arg))


def arccos(arg):
    return f * (acos(arg))


def arctan(arg):
    return f * (atan(arg))


class Calc:
    def __init__(self, master):
        # ex that will be displayed on screen
        self.ex = ""
        # be used to store data in memory
        self.recall = ""
        # self.answ
        self.versum = ""
        # create string for text input
        self.intxt = tk.StringVar()
        # assign instance to master
        self.master = master
        # set frame showing inputs and title
        top_frame = tk.Frame(master, width=650, height=20, bd=4, relief='flat', bg='#999999')
        top_frame.pack(side=tk.TOP)
        # set frame showing all buttons
        btfr = tk.Frame(master, width=650, height=470, bd=4, relief='flat', bg='white')
        btfr.pack(side=tk.BOTTOM)
        # name of calculator
        my_item = tk.Label(top_frame, text="Simple Scientific GUI Calculator",
                           font=('arial', 14), fg='white', width=26, bg='#888888')
        my_item.pack()
        # entry interface for inputs
        txt_display = tk.Entry(top_frame, font=('arial', 36), relief='flat',
                               bg='#666666', fg='white', textvariable=self.intxt, width=60, bd=4, justify='right')
        txt_display.pack()

        # row 0
        # left bracket button
        self.btn_left_brack = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange', text="(", command=lambda: self.cli('('))
        self.btn_left_brack.grid(row=0, column=0)
        # right bracket button
        self.btn_right_brack = tk.Button(btfr, **obj, text=")", foreground='pink', activeforeground='orange', command=lambda: self.cli(')'))
        self.btn_right_brack.grid(row=0, column=1)
        # takes e to some exponent that you insert into the function
        self.btn_exp = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange', text="exp", command=lambda: self.cli('exp('))
        self.btn_exp.grid(row=0, column=2)
        # constant pi
        self.btn_pi = tk.Button(btfr, **obj, text="π", foreground='pink', activeforeground='orange', command=lambda: self.cli('pi'))
        self.btn_pi.grid(row=0, column=3)
        # clears self.ex
        self.btn_clear = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange', text="C", command=self.ac)
        self.btn_clear.grid(row=0, column=4)
        # deletes last string input
        self.btn_del = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange', text="del", command=self.clr)
        self.btn_del.grid(row=0, column=5)
        # inputs a negative sign to the next entry
        self.btn_change_sign = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange', text="+/-", command=self.uni)
        self.btn_change_sign.grid(row=0, column=6)
        # division
        self.btn_div = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange', text="/", command=lambda: self.cli('/'))
        self.btn_div.grid(row=0, column=7)
        # square root
        self.btrqt = tk.Button(btfr, **obj, text="sqrt", foreground='pink', activeforeground='orange', command=lambda: self.cli('sqrt('))
        self.btrqt.grid(row=0, column=8)
        # row 1
        # changes trigonometric function outputs to degrees
        self.dbn = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange', text="Deg",
                                 command=self.rtd)
        self.dbn.grid(row=1, column=0)
        # changes trig function outputs to default back to radians
        self.rbn = tk.Button(btfr, **obj, foreground='orange', activeforeground='orange', text="Rad",
                                 command=self.dtr)
        self.rbn.grid(row=1, column=1)
        # cubes a value
        self.cube = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange', text=u"x\u00B3", command=lambda: self.cli('**3'))
        self.cube.grid(row=1, column=2)
        # takes the absolute value of an ex
        self.btn_abs = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="abs", command=lambda: self.cli('abs' + '('))
        self.btn_abs.grid(row=1, column=3)
        # seven
        self.btn_7 = tk.Button(btfr, **obj, foreground='white', activeforeground='orange',text="7", command=lambda: self.cli(7))
        self.btn_7.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_7.grid(row=1, column=4)
        # eight
        self.btn_8 = tk.Button(btfr, **obj, foreground='white', activeforeground='orange',text="8", command=lambda: self.cli(8))
        self.btn_8.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_8.grid(row=1, column=5)
        # nine
        self.btn_9 = tk.Button(btfr, **obj, foreground='white', activeforeground='orange',text="9", command=lambda: self.cli(9))
        self.btn_9.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_9.grid(row=1, column=6)
        # multiplication
        self.btn_mul = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="x", command=lambda: self.cli('*'))
        self.btn_mul.grid(row=1, column=7)
        # 'memory clear' button. Wipes self.recall to an empty string
        self.btn_MC = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="MC", command=self.memc)
        self.btn_MC.grid(row=1, column=8)
        # row 2
        # sin function that returns value from -1 to 1 by default
        self.btn_sin = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="sin", command=lambda: self.cli('fsin('))
        self.btn_sin.grid(row=2, column=0)
        # cos function that returns value from -1 to 1 by default
        self.btn_cos = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="cos", command=lambda: self.cli('fcos('))
        self.btn_cos.grid(row=2, column=1)
        # tan function
        self.btn_tan = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="tan", command=lambda: self.cli('ftan('))
        self.btn_tan.grid(row=2, column=2)
        # log function
        self.btn_log = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="log", command=lambda: self.cli('log('))
        self.btn_log.grid(row=2, column=3)
        # four
        self.btn_4 = tk.Button(btfr, **obj, foreground='white', activeforeground='orange',text="4", command=lambda: self.cli(4))
        self.btn_4.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_4.grid(row=2, column=4)
        # five
        self.btn_5 = tk.Button(btfr, **obj, foreground='white', activeforeground='orange',text="5", command=lambda: self.cli(5))
        self.btn_5.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_5.grid(row=2, column=5)
        # six
        self.btn_6 = tk.Button(btfr, **obj, foreground='white', activeforeground='orange',text="6", command=lambda: self.cli(6))
        self.btn_6.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_6.grid(row=2, column=6)
        # subtraction
        self.btnSub = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="-", command=lambda: self.cli('-'))
        self.btnSub.grid(row=2, column=7)
        # outputs what is in self.recall
        self.btn_MR = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="MR", command=self.again)
        self.btn_MR.grid(row=2, column=8)
        # row 3

        # cos inverse function
        self.btn_cos_inverse = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text=u"cos-\u00B9",
                                         command=lambda: self.cli('arccos('))
        self.btn_cos_inverse.grid(row=3, column=1)

        # takes the natural log
        self.btn_ln = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="ln", command=lambda: self.cli('log1p('))
        self.btn_ln.grid(row=3, column=3)
        # sin inverse function
        self.btn_sin_inverse = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text=u"sin-\u00B9",
                                         command=lambda: self.cli('arcsin('))
        self.btn_sin_inverse.grid(row=3, column=0)
        # one
        self.btn_1 = tk.Button(btfr, **obj, foreground='white', activeforeground='orange',text="1", command=lambda: self.cli(1))
        self.btn_1.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_1.grid(row=3, column=4)
        # tan inverse function
        self.btn_tan_inverse = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text=u"tan-\u00B9",
                                         command=lambda: self.cli('arctan('))
        self.btn_tan_inverse.grid(row=3, column=2)
        # two
        self.btn_2 = tk.Button(btfr, **obj, text="2", foreground='white', activeforeground='orange',command=lambda: self.cli(2))
        self.btn_2.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_2.grid(row=3, column=5)
        # three
        self.btn_3 = tk.Button(btfr, **obj, foreground='white', activeforeground='orange',text="3", command=lambda: self.cli(3))
        self.btn_3.configure(activebackground="#4d4d4d", bg='#4d4d4d')
        self.btn_3.grid(row=3, column=6)
        # addition
        self.btn_add = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="+", command=lambda: self.cli('+'))
        self.btn_add.grid(row=3, column=7)
        # adds current self.ex to self.recall string
        self.btum = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="M+", command=self.mema)
        self.btum.grid(row=3, column=8)
        # row 4
        # factorial function
        self.bttf = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="n!", command=lambda: self.cli('factorial('))
        self.bttf.grid(row=4, column=0)
        # square function
        self.btrq = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text=u"x\u00B2", command=lambda: self.cli('**2'))
        self.btrq.grid(row=4, column=1)
        # to the power of function
        self.btpo = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="x^y", command=lambda: self.cli('**'))
        self.btpo.grid(row=4, column=2)
        # stores previous ex as an answ value
        self.btns = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="ans", command=self.answ)
        self.btns.grid(row=4, column=3)
        # zero
        self.btn_0 = tk.Button(btfr, **obj, foreground='white', activeforeground='orange',text="0", command=lambda: self.cli(0))
        self.btn_0.configure(activebackground="#4d4d4d", bg='#4d4d4d', width=7, bd=5)
        self.btn_0.grid(row=4, column=4, columnspan=2)
        # equals button
        self.btqe = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text="=", command=self.beq)
        self.btqe.configure(bg='#ff9980', activebackground='#ff9980')
        self.btqe.grid(row=4, column=6)
        # decimal to convert to float
        self.btce = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text=".", command=lambda: self.cli('.'))
        self.btce.grid(row=4, column=7)
        # comma to allow for more than one parameter!
        self.btco = tk.Button(btfr, **obj, foreground='pink', activeforeground='orange',text=",", command=lambda: self.cli(','))
        self.btco.grid(row=4, column=8)

    # functions
    # allows button you click to be put into self.ex

    def cli(self, expv):
        if len(self.ex) >= 23:
            self.ex = self.ex
            self.intxt.set(self.ex)
        else:
            self.ex = self.ex + str(expv)
            self.intxt.set(self.ex)

    # clears last item in string

    def clr(self):
        self.ex = self.ex[:-1]
        self.intxt.set(self.ex)

    # adds in a negative sign

    def uni(self):
        self.ex = self.ex + '-'
        self.intxt.set(self.ex)

    # clears again

    def memc(self):
        self.recall = ""

    # adds whatever is on the screen to self.recall

    def mema(self):
        self.recall = self.recall + '+' + self.ex

    # uses whatever is stored in again

    def answ(self):
        self.answ = self.versum
        self.ex = self.ex + self.answ
        self.intxt.set(self.ex)

    # uses whatever is stored in again

    def again(self):
        if self.ex == "":
            self.intxt.set('0' + self.ex + self.recall)
        else:
            self.intxt.set(self.ex + self.recall)

    # changes self.cons to a string that allows degree conversion when button is clicked

    def rtd(self):
        global cons
        global f
        cons = pi / 180
        f = 180 / pi
        self.rbn["foreground"] = 'white'
        self.dbn["foreground"] = 'orange'

    def dtr(self):
        global cons
        global f
        cons = 1
        f = 1
        self.rbn["foreground"] = 'orange'
        self.dbn["foreground"] = 'white'

    # clears self.ex

    def ac(self):
        self.ex = ""
        self.intxt.set("")

    # converts self.ex into a mathematical ex and evaluates it

    def beq(self):
        self.versum = str(eval(self.ex))
        self.intxt.set(self.versum)
        self.ex = self.versum


# tkinter layout
root = tk.Tk()
b = Calc(root)
root.title("Simple Scientific GUI Calculator")
root.geometry("650x490+50+50")
root.resizable(False, False)
root.mainloop()