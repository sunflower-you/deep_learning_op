
import torch
import numpy as np
import sys
sys.path.append('..')

from py.Sign import sign


np.random.seed(1001)

low = -10
high = 10
size = (1,3,64,64)
input = np.random.uniform(low,high,size)


golden_output = torch.sign(torch.from_numpy(input))
output = sign(input)

cos_sim = torch.cosine_similarity(golden_output.flatten(), torch.from_numpy(output).flatten(), dim=0).item()
print(f'torch golden output 和 python output 余弦相似度：{cos_sim}')


is_equal = torch.equal(golden_output.flatten(), torch.from_numpy(output).flatten())
print(f'torch golden output 和 python output 是否相等：{is_equal}')

print(input.flatten())
print(golden_output.flatten())
print(torch.from_numpy(output).flatten())