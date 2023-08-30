
import torch
import numpy as np
import sys
sys.path.append('..')

from py.Atanh import atanh


np.random.seed(1001)

low = -1
high = 1
size = (1,3,64,64)
input = np.random.uniform(low,high,size)


golden_output = torch.atanh(torch.from_numpy(input))
output = atanh(input)

cos_sim = torch.cosine_similarity(golden_output.flatten(), torch.from_numpy(output).flatten(), dim=0).item()
print(f'torch golden output 和 python output 余弦相似度：{cos_sim}')


is_equal = torch.equal(golden_output.flatten(), torch.from_numpy(output).flatten())
print(f'torch golden output 和 python output 是否相等：{is_equal}')

print(input.flatten())
print(golden_output.flatten())
print(torch.from_numpy(output).flatten())