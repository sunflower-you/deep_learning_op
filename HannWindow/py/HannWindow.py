import numpy as np


def hann(size,output_datatype=1,periodic=1):
    '''
        output_datatype:默认1，float
        periodic：默认1, 0的时候返回symmetric window
    '''
    if output_datatype == 1:
        dtype = np.float32
    # periodic window
    if periodic == 1:
        size = np.int32(size)
        a0 = 0.5
        a1 = 0.5
        y = a0 - a1 * np.cos(2 * np.pi * np.arange(0, size, 1, dtype=dtype) / size)
    #  symmetric window
    if periodic == 0:
        size = np.int32(10)
        a0 = 0.5
        a1 = 0.5
        y = a0 - a1 * np.cos(2 * np.pi * np.arange(0, size, 1, dtype=dtype) / (size - 1))
    return y