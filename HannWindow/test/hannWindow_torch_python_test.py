
import torch
import numpy as np
import sys
sys.path.append('..')

from py.HannWindow import hann


np.random.seed(1001)

size = 10

'''
    1、symmetric window
'''

golden_output = torch.windows.hann(size, sym=True, dtype=torch.float32)
output = hann(size, output_datatype=1, periodic=0)

cos_sim = torch.cosine_similarity(golden_output.flatten(), torch.from_numpy(output).flatten(), dim=0).item()
print(f'torch golden output 和 python output 余弦相似度：{cos_sim}')


is_equal = torch.equal(golden_output.flatten(), torch.from_numpy(output).flatten())
print(f'torch golden output 和 python output 是否相等：{is_equal}')

print(size)
print(golden_output.flatten())
print(torch.from_numpy(output).flatten())


'''
    2、periodic window
'''
golden_output = torch.windows.hann(size, sym=False, dtype=torch.float32)
output = hann(size, output_datatype=1, periodic=1)

cos_sim = torch.cosine_similarity(golden_output.flatten(), torch.from_numpy(output).flatten(), dim=0).item()
print(f'torch golden output 和 python output 余弦相似度：{cos_sim}')


is_equal = torch.equal(golden_output.flatten(), torch.from_numpy(output).flatten())
print(f'torch golden output 和 python output 是否相等：{is_equal}')

print(size)
print(golden_output.flatten())
print(torch.from_numpy(output).flatten())