# import numpy as np
from math import sqrt

from utils import add_class, now, add_classes


# insert date
date = now()
pyscript.write('date', f"{date}")


output_el = Element('output').element

percent_el = Element('percent').element

oq_el = Element('openQ').element
cq_el = Element('closedQ').element
s_el = Element('slash').element
zero_el = Element('zero').element
one_el = Element('one').element
two_el = Element('two').element
three_el = Element('three').element
four_el = Element('four').element
five_el = Element('five').element
six_el = Element('six').element
seven_el = Element('seven').element
eight_el = Element('eight').element
nine_el = Element('nine').element
star_el = Element('star').element
minus_el = Element('minus').element
plus_el = Element('plus').element
dot_el = Element('dot').element


# Making button works
def display(*args):
    output_el.innerHTML = eval(str(sqrt(int(output_el.innerHTML))))
def display1(*args):
    output_el.innerHTML += percent_el.getAttribute('value')
def display2(*args):
    output_el.innerHTML += oq_el.getAttribute('value')
def display3(*args):
    output_el.innerHTML += cq_el.getAttribute('value')
def display4(*args):
    output_el.innerHTML += s_el.getAttribute('value')
def display5(*args):
    output_el.innerHTML += seven_el.getAttribute('value')
def display6(*args):
    output_el.innerHTML += eight_el.getAttribute('value')
def display7(*args):
    output_el.innerHTML += nine_el.getAttribute('value')
def display8(*args):
    output_el.innerHTML += star_el.getAttribute('value')
def display9(*args):
    output_el.innerHTML += four_el.getAttribute('value')
def display10(*args):
    output_el.innerHTML += five_el.getAttribute('value')
def display11(*args):
    output_el.innerHTML += six_el.getAttribute('value')
def display12(*args):
    output_el.innerHTML += minus_el.getAttribute('value')
def display13(*args):
    output_el.innerHTML += one_el.getAttribute('value')
def display14(*args):
    output_el.innerHTML += two_el.getAttribute('value')
def display15(*args):
    output_el.innerHTML += three_el.getAttribute('value')
def display16(*args):
    output_el.innerHTML += plus_el.getAttribute('value')
def display17(*args):
    output_el.innerHTML += zero_el.getAttribute('value')
def display18(*args):
    output_el.innerHTML += dot_el.getAttribute('value')


console.log(percent_el)



# setting C to clear LCD
def clear(*args):
    output_el.innerHTML = ''


# Delete functionality
def delete(*args):
    output_el.innerHTML = output_el.innerHTML[:-1]


#  making the calculaton
def calc(*args):
    try:
        output_el.innerHTML = eval(output_el.innerHTML)
    except:
        output_el.innerHTML = 'XXXXXXXXXXXXXXXX!'



#  Enable Keyboard Input
def key(e):
    if e.key == "Enter":
        calc()
    elif (e.which):
        keynum = e.which
        console.log(ord(keynum))
        display(ord(keynum))

output_el.onkeypress = key

output_el.onclick = calc

document.addEventListener("keydown", key, False)


# add classes on load
btn_yellow = 'bg-yellow-100 shadow-md rounded-2xl w-12 h-12 text-yellow-600 font-medium flex justify-center items-center cursor-pointer'
btn_orange = 'bg-yellow-500 shadow-md rounded-2xl w-12 h-12 text-white font-medium text-xl flex justify-center items-center cursor-pointer'
btn_grey = 'bg-gray-200 shadow-md rounded-2xl w-12 h-12 text-black font-medium flex justify-center items-center cursor-pointer'
btn_green = 'bg-green-500 shadow-md rounded-2xl w-12 h-12 text-white font-medium text-xl flex justify-center items-center cursor-pointer'
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
