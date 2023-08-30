import numpy as np

def mod(x_dividend, x_divisor , fmod=0):
    if fmod==0:
        y = np.mod(x_dividend, x_divisor)
    else:
        y = np.fmod(x_dividend, x_divisor)
    return y


