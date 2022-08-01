import numpy as np
import math


def get_original(number, size):
    original_w = (number-1) % size
    original_h = (number-1) //size
    return original_w, original_h


def check_md(scramble):
    scramble = scramble.replace("/", " ")
    numbers = scramble.split(" ")
    mysize = int(math.sqrt(len(numbers)))
    myarray = np.asarray(numbers).reshape(mysize, mysize)
    mdsum = 0
    for h in range(0, mysize):
        for w in range(0, mysize):
            current_number = int(myarray[h, w])
            if current_number != 0:
                original_w, original_h = get_original(current_number, mysize)
                current_md = abs(original_h - h) + abs(original_w - w)
                mdsum += current_md
    return mdsum

