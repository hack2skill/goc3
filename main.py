# import numpy as np
# import random

from utils import add_class, now, add_classes


# insert date
date = now()
pyscript.write('date', f"{date}")


output_el = Element('output').element


# setting C to clear LCD
def clear():
    # document.getElementById('output').innerText = '';
    output_el.innerText = '';
    # output_el.clear()
    # Element('output').clear()


# Del functionality
def delete():
    # document.getElementById('output').innerText = document.getElementById('output').innerText.slice(0, -1)
    output_el.innerText = output_el.innerText[:-1]

# Making button works


def display(n):
    # document.getElementById('output').innerText += n
    output_el.innerText += n


#  making the calculaton
def calc():
    try:
        # document.getElementById('output').innerText = eval(document.getElementById('output').innerText)
        output_el.innerText = eval(output_el.innerText)
    except:
        # document.getElementById('output').innerText = 'XXXXXXXXXXXXXXXXXXXXX!'
        output_el.innerText = 'XXXXXXXXXXXXXXXX!'


# def key(e):
#     global keynum
#     if (window.event):
#         keynum = e.keyCode
#     elif (e.which):
#         keynum = e.which

#     console.log(String.fromCharCode(keynum))
#     display(String.fromCharCode(keynum))


#  Enable Keyboard Input
def key(e):
    if e.key == "Enter":
         calc()
    elif (e.which):
        keynum = e.which
        console.log(ord(keynum))
        display(ord(keynum))

output_el.onkeypress = key

output_el.onclick = calc()



document.addEventListener("keydown", key, False)


# add classes on load
btn_yellow = 'bg-yellow-100 shadow-md rounded-2xl w-12 h-12 text-yellow-600 font-medium flex justify-center items-center cursor-pointer'
btn_orange = 'bg-yellow-500 shadow-md rounded-2xl w-12 h-12 text-white font-medium text-xl flex justify-center items-center cursor-pointer'
btn_grey = 'bg-gray-200 shadow-md rounded-2xl w-12 h-12 text-black font-medium flex justify-center items-center cursor-pointer'
btn_green = 'bg-green-500 shadow-md rounded-2xl w-12 h-12 text-white font-medium text-xl flex justify-center items- cursor-pointer'
btn_grey_jumbo = 'bg-gray-200 shadow-md rounded-2xl w-full h-12 text-black font-medium flex justify-center items-center cursor-pointer'

btn_yellow_el = document.getElementsByClassName('btn-yellow')
btn_orange_el = document.getElementsByClassName('btn-orange')
btn_grey_el = document.getElementsByClassName('btn-grey')
btn_green_el = document.getElementsByClassName('btn-green')
btn_grey_jumbo_el = document.getElementsByClassName('btn-grey-jumbo')


def onLoad(*args):
    def divLoop(divCollection, div_classes):
        for div in divCollection:
            add_classes(div, div_classes)

    divLoop(btn_yellow_el, btn_yellow)
    divLoop(btn_orange_el, btn_orange)
    divLoop(btn_grey_el, btn_grey)
    divLoop(btn_green_el, btn_green)
    divLoop(btn_grey_jumbo_el, btn_grey_jumbo)


onLoad()
