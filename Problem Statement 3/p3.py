import tkinter

def wquit():
    print('Hello, getting out of here')

root=tkinter.Tk()
widget1=tkinter.Label(root, text='Hello there')
widget1.pack()
widget2=tkinter.Button(root, text='Click to quit', command=wquit)
widget2.pack()

root.mainloop()
