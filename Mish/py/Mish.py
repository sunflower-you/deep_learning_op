import numpy as np


def softplus(x):
    return np.log(np.exp(x) + 1)


def mish(x):
    return x * np.tanh(softplus(x))