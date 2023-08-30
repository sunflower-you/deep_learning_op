import torch
import numpy as np

size = (1,3,64,64)
input = np.fromfile("../cpp/input.bin", dtype=np.float32).reshape(size)
output = np.fromfile("../cpp/output.bin", dtype=np.float32).reshape(size)

golden_output = torch.atan(torch.from_numpy(input))

cos_sim = torch.cosine_similarity(golden_output.flatten(), torch.from_numpy(output).flatten(), dim=0).item()
print(f'torch golden output 和 cpp output 余弦相似度：{cos_sim}')


is_equal = torch.equal(golden_output.flatten(), torch.from_numpy(output).flatten())
print(f'torch golden output 和 cpp output 是否相等：{is_equal}')

print(input.flatten())
print(golden_output.flatten())
print(torch.from_numpy(output).flatten())