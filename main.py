import numpy as np
import random
from utils import add_class
output_el = Element('output').element
# console.log(output_el)

color = ['blue', 'red', 'yellow', 'purple', 'green', 'gray', 'orange']
random.seed(100)

arr = np.array([22, 15, 16, 80, 415, 66])
# pyscript.write('output', f'{arr}')
output_el.innerHTML = f'{arr}'

def shuffle_array(*args):
    #Shuffle
    shuffled = sorted(arr, key = lambda k: random.random())

    #Change color
    add_class(output_el, 'text-' + color[random.randint(0, len(color) - 1)] + '-500')
    # pyscript.write('output', shuffled)
    output_el.innerHTML = shuffled