import torch
import numpy as np


'''
    1、symmetric window
'''
size = int(np.fromfile("../cpp/input0.bin", dtype=np.int32))
output0 = np.fromfile("../cpp/output0.bin", dtype=np.float32)

golden_output = torch.windows.hamming(size, sym=True, dtype=torch.float32)

cos_sim = torch.cosine_similarity(golden_output.flatten(), torch.from_numpy(output0).flatten(), dim=0).item()
print("test1 symmetric window")
print(f'torch golden output 和 cpp output 余弦相似度：{cos_sim}')


is_equal = torch.equal(golden_output.flatten(), torch.from_numpy(output0).flatten())
print(f'torch golden output 和 cpp output 是否相等：{is_equal}')


print(golden_output.flatten())
print(torch.from_numpy(output0).flatten())


'''
    2、periodic window
'''
size = int(np.fromfile("../cpp/input1.bin", dtype=np.int32))
output1 = np.fromfile("../cpp/output1.bin", dtype=np.float32)

golden_output = torch.windows.hamming(size, sym=False, dtype=torch.float32)

cos_sim = torch.cosine_similarity(golden_output.flatten(), torch.from_numpy(output1).flatten(), dim=0).item()
print("\ntest2 periodic window")
print(f'torch golden output 和 cpp output 余弦相似度：{cos_sim}')


is_equal = torch.equal(golden_output.flatten(), torch.from_numpy(output1).flatten())
print(f'torch golden output 和 cpp output 是否相等：{is_equal}')


print(golden_output.flatten())
print(torch.from_numpy(output1).flatten())