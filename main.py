import numpy as np
import random

from utils import add_class, now, add_classes


# insert date
date = now()
pyscript.write('date', f"{date}")


# add classes on load
btn_yellow = 'bg-yellow-100 shadow-md rounded-2xl w-12 h-12 text-yellow-600 font-medium flex justify-center items-center'
btn_orange = 'bg-yellow-500 shadow-md rounded-2xl w-12 h-12 text-white font-medium text-xl flex justify-center items-center'
btn_grey = 'bg-gray-200 shadow-md rounded-2xl w-12 h-12 text-black font-medium flex justify-center items-center'
btn_green = 'bg-green-500 shadow-md rounded-2xl w-12 h-12 text-white font-medium text-xl flex justify-center items-center'
btn_grey_jumbo = 'bg-gray-200 shadow-md rounded-2xl w-full h-12 text-black font-medium flex justify-center items-center'

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
