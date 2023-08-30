
'''
torch:
    α=1.6732632423543772848170429916717
    scale=1.0507009873554804934193349852946

onnx:
    alpha=1.67326319217681884765625
    gamma=1.05070102214813232421875
'''

import numpy as np

def selu(x, gamma=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    y = (np.clip(x, 0, np.inf) + (np.exp(np.clip(x, -np.inf, 0)) - 1) * alpha) * gamma
    return y
