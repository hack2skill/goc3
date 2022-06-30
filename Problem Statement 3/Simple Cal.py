# Import Tkinter
import tkinter as tk
# Constant Variables
LABEL_COLOR ="#3333cc"
FONT_STYLE = ("Arial",25,"bold")
LARFE_FONT = ("Arial",40,"bold")
white = "#000000"
digit_font = ("Arial",24,"bold")
default_font_style = ("Arial",20,"bold")
off_white = "#000000";
light_blue = "#3333cc";
# Calculator class
class Calculator:
    # Constructor
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Tanmay")
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {7:(1,1),8:(1,2),9:(1,3),
                       4:(2,1),5:(2,2),6:(2,3),
                       1:(3,1),2:(3,2),3:(3,3),0:(4,1),".":(4,2)}
        self.operations = {
            "/":"\u00F7","*":"\u00D7","-":"-","+":"+"
        }
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_button()
        self.create_operator_buttons()
        self.create_special_buttons()

    # Display Frame Method
    def create_display_frame(self):
        frame = tk.Frame(self.window,height=221,background="#f5f5f5")
        frame.pack(expand=True,fill="both")
        return frame
    # Expression creation method
    def add_to_expression(self,value):
        self.current_expression += str(value)
        self.update_label()

    # Digit button Method
    def create_digit_button(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame,text = str(digit),background=white,foreground=LABEL_COLOR
                               ,font=digit_font,borderwidth=0,command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)

    # Clear and equal button method
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equal_button()

    # Display Lablel method
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame,text = self.total_expression,anchor=tk.E,background=light_blue,foreground=off_white,padx=24,font=FONT_STYLE)
        total_label.pack(expand=True,fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, background=light_blue,
                               foreground=off_white, padx=24, font=LARFE_FONT)
        label.pack(expand=True, fill="both")

        return total_label,label

    def append_operator(self,operator):
        self.current_expression+= operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()
    # Create button method
    def create_operator_buttons(self):
        i = 0
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttons_frame,text = symbol,bg=off_white,fg=LABEL_COLOR,font=default_font_style
                               ,borderwidth=0,command=lambda x=operator: self.append_operator(x))
            button.grid(row= i,column=4,sticky=tk.NSEW)
            i+=1

    # Clear screen method
    def clear_method(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()


    def create_clear_button(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text="C", bg=off_white, fg=LABEL_COLOR, font=default_font_style
                               , borderwidth=0,command=self.clear_method)
            button.grid(row=0, column=1, sticky=tk.NSEW,columnspan=3)
            i += 1

    # Calculate Method
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        self.current_expression = str(eval(self.total_expression))
        self.total_expression = ""
        self.update_label()

    def create_equal_button(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text="=", bg=light_blue, fg=off_white, font=default_font_style
                               , borderwidth=0,command=self.evaluate)
            button.grid(row=4, column=3, sticky=tk.NSEW,columnspan=2)
            i += 1
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)
    # Run method
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
