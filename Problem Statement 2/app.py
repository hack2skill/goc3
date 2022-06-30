from tkinter import ttk, filedialog, Canvas
from ttkthemes import ThemedTk
import os
from PIL import ImageTk, Image, ImageEnhance, ImageFilter, ImageGrab

EDIT_COUNTER = -1


def openfilename():
    filename = filedialog.askopenfilename(title='"pen')
    return filename


def show_img(filename):
    img = Image.open(filename)
    img = img.resize((300, 250), Image.ANTIALIAS)
    img.save(f'edit_{EDIT_COUNTER}.jpg')
    image = ImageTk.PhotoImage(img)
    image_label.create_image(0, 0, image=image, anchor='nw')
    # image_label.configure(image = image)
    image_label.image = image


def save_img():
    img = Image.open(f'edit_{EDIT_COUNTER}.jpg')
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    img.save(filename)


def open_img(filename=''):
    global EDIT_COUNTER
    if EDIT_COUNTER == -1:
        filename = openfilename()
        EDIT_COUNTER += 1
        open_save_btn['text'] = 'Save Image'
        show_img(filename)
    else:
        save_img()


def blurImg():
    global EDIT_COUNTER
    if EDIT_COUNTER > -1:
        img = Image.open(f'edit_{EDIT_COUNTER}.jpg')
        EDIT_COUNTER += 1
        img.filter(ImageFilter.BLUR).save(f'edit_{EDIT_COUNTER}.jpg')
        show_img(filename=f'edit_{EDIT_COUNTER}.jpg')


def guass_blurImg():
    global EDIT_COUNTER
    if EDIT_COUNTER > -1:
        img = Image.open(f'edit_{EDIT_COUNTER}.jpg')
        EDIT_COUNTER += 1
        img.filter(ImageFilter.GaussianBlur(radius=2)
                   ).save(f'edit_{EDIT_COUNTER}.jpg')
        show_img(filename=f'edit_{EDIT_COUNTER}.jpg')


def enhanceImg():
    global EDIT_COUNTER
    if EDIT_COUNTER > -1:
        img = Image.open(f'edit_{EDIT_COUNTER}.jpg')
        EDIT_COUNTER += 1
        enh = ImageEnhance.Contrast(img)
        enh.enhance(1.5).save(f'edit_{EDIT_COUNTER}.jpg')
        show_img(filename=f'edit_{EDIT_COUNTER}.jpg')


def rotateImg():
    global EDIT_COUNTER
    if EDIT_COUNTER > -1:
        img = Image.open(f'edit_{EDIT_COUNTER}.jpg')
        EDIT_COUNTER += 1
        img.rotate(90, Image.NEAREST, expand=1).save(
            f'edit_{EDIT_COUNTER}.jpg')
        show_img(filename=f'edit_{EDIT_COUNTER}.jpg')


def contourImg():
    global EDIT_COUNTER
    if EDIT_COUNTER > -1:
        img = Image.open(f'edit_{EDIT_COUNTER}.jpg')
        EDIT_COUNTER += 1
        img.filter(ImageFilter.CONTOUR()).save(f'edit_{EDIT_COUNTER}.jpg')
        show_img(filename=f'edit_{EDIT_COUNTER}.jpg')

def embossImg():
    global EDIT_COUNTER
    if EDIT_COUNTER > -1:
        img = Image.open(f'edit_{EDIT_COUNTER}.jpg')
        EDIT_COUNTER += 1
        img.filter(ImageFilter.EMBOSS()).save(f'edit_{EDIT_COUNTER}.jpg')
        show_img(filename=f'edit_{EDIT_COUNTER}.jpg')


def black_whiteImg():
    global EDIT_COUNTER
    if EDIT_COUNTER > -1:
        img = Image.open(f'edit_{EDIT_COUNTER}.jpg')
        EDIT_COUNTER += 1
        ImageEnhance.Color(img).enhance(0.0).save(f'edit_{EDIT_COUNTER}.jpg')
        show_img(filename=f'edit_{EDIT_COUNTER}.jpg')


def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y


def draw_smth(event):
    global lasx, lasy
    image_label.create_line(
        (lasx, lasy, event.x, event.y), fill='red', width=2)
    lasx, lasy = event.x, event.y


def draw_onImg():
    global EDIT_COUNTER
    if EDIT_COUNTER > -1:
        img = Image.open(f'edit_{EDIT_COUNTER}.jpg')
        image = ImageTk.PhotoImage(img)
        draw_done.place(x=490, y=150)
        image_label.bind("<Button-1>", get_x_and_y)
        image_label.bind("<B1-Motion>", draw_smth)


def draw_doneImg():
    global EDIT_COUNTER
    if EDIT_COUNTER > -1:
        EDIT_COUNTER += 1
        x = window.winfo_rootx()+image_label.winfo_x()
        y = window.winfo_rooty()+image_label.winfo_y()
        x1 = x+image_label.winfo_width()
        y1 = y+image_label.winfo_height()
        im = ImageGrab.grab(bbox=(x, y, x1, y1))
        im.save(f'edit_{EDIT_COUNTER}.jpg')
        image_label.unbind("<Button-1>")
        image_label.unbind("<B1-Motion>")
        draw_done.place_forget()

def undo_cmd():
    global EDIT_COUNTER
    if EDIT_COUNTER != 0:
        os.remove(f'edit_{EDIT_COUNTER}.jpg')
        EDIT_COUNTER -= 1
        show_img(filename=f'edit_{EDIT_COUNTER}.jpg')
    

def quit_command():
    window.destroy()

# Tkinter Arrangement


window = ThemedTk(theme="breeze")
window.title("Editor")
window.geometry("600x500")

title = ttk.Label(text="Image Editing App",
                  font=("Arial", 15)).place(x=230, y=5)

open_save_btn = ttk.Button(window, text='open image', command=open_img)
open_save_btn.place(x=260, y=35)


image_label = Canvas(window, height=248, width=298, background='black')
image_label.place(x=160, y=75)

enhance = ttk.Button(window, text="Enhance",command=enhanceImg).place(x=50, y=350)
rotate = ttk.Button(window, text="Rotate",command=rotateImg).place(x=150, y=350)
blur = ttk.Button(window, text="Blur", command=blurImg).place(x=250, y=350)
guass_blur = ttk.Button(window, text="Gaussian Blur",command=guass_blurImg).place(x=350, y=350)
draw = ttk.Button(window, text="Draw", command=draw_onImg).place(x=460, y=350)
draw_done = ttk.Button(window, text="Done", command=draw_doneImg)
contour = ttk.Button(window, text="Contour", command=contourImg).place(x=150, y=390)
emboss = ttk.Button(window, text="Emboss", command=embossImg).place(x=250, y=390)
black_white = ttk.Button(window, text="Black & White", command=black_whiteImg).place(x=350, y=390)

undo = ttk.Button(window, text="Undo",command=undo_cmd).place(x=210, y=460)
ttk.Button(window, text="Quit", command=quit_command).place(x=310, y=460)

window.mainloop()
