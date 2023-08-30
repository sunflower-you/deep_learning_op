
import torch
import numpy as np
import onnxruntime
import onnx
from onnx import helper, shape_inference
import sys
sys.path.append('..')

from py.Mod import mod


def build_onnx_model(input_names="input", output_names="output", input_shape=[1, 3, 224, 224], elem_type=onnx.TensorProto.FLOAT, fmod=1):
    # 创建一个空的图
    graph = helper.make_graph([], "Mod", [], [])

    # 添加输入和输出节点
    input_names = input_names
    output_names = output_names
    input_shape = input_shape  # 输入张量的形状

    # 创建输入节点
    for input_name in input_names:
        # input_type = helper.make_tensor_type(dtype=onnx.TensorProto.FLOAT, shape=input_shape)
        input_value_info = helper.make_tensor_value_info(input_name, elem_type=elem_type, shape=input_shape)
        graph.input.extend([input_value_info])

    # 创建输出节点
    for output_name in output_names:
        # output_type = helper.make_tensor_type(dtype=onnx.TensorProto.FLOAT, shape=input_shape)
        output_value_info = helper.make_tensor_value_info(output_name, elem_type=elem_type, shape=input_shape)
        graph.output.extend([output_value_info])

    # 创建算子节点
    node_name = "Mod_1"
    node_inputs = input_names
    node_outputs = output_names
    node = helper.make_node("Mod", node_inputs, node_outputs, name=node_name,fmod=fmod)
    graph.node.extend([node])

    # 添加图到模型
    model = helper.make_model(graph, producer_name="ModModel")

    return model

np.random.seed(1001)

low = -10
high = 10
size = (1,3,64,64)

'''
1、输入是float时, fmod必须是1  测试
'''
input0 = np.random.uniform(low,high,size).astype(np.float32)
input1 = np.random.uniform(low,high,size).astype(np.float32)

# build model
elem_type=onnx.TensorProto.FLOAT
model = build_onnx_model(input_names=["input0", "input1"], output_names=["output"], input_shape=size, elem_type=elem_type, fmod=1)
# load model 
session = onnxruntime.InferenceSession(model.SerializeToString(), providers=['CPUExecutionProvider'])
# inference
golden_output = session.run(None, {'input0': input0, 'input1': input1})[0]

output = mod(input0, input1, fmod=1)

cos_sim = torch.cosine_similarity(torch.from_numpy(golden_output.flatten()), torch.from_numpy(output).flatten(), dim=0).item()
print(f'onnx golden output 和 python output 余弦相似度：{cos_sim}')


is_equal = torch.equal(torch.from_numpy(golden_output.flatten()), torch.from_numpy(output).flatten())
print(f'onnx golden output 和 python output 是否相等：{is_equal}')

print(input0.flatten())
print(input1.flatten())
print(golden_output.flatten())
print(torch.from_numpy(output).flatten())



'''
2、输入int, fmod=0 测试
    int推理有问题
'''
# input0 = np.random.uniform(low,high,size).astype(np.int16)
# input1 = np.random.uniform(low,high,size).astype(np.int16)

# # build model
# elem_type=onnx.TensorProto.INT16
# model = build_onnx_model(input_names=["input0", "input1"], output_names=["output"], input_shape=size, elem_type=elem_type, fmod=0)
# # load model 
# session = onnxruntime.InferenceSession(model.SerializeToString(), providers=['CPUExecutionProvider'])
# # inference
# golden_output = session.run(None, {'input0': input0, 'input1': input1})[0]

# output = mod(input0, input1, fmod=0)

# cos_sim = torch.cosine_similarity(torch.from_numpy(golden_output.flatten()), torch.from_numpy(output).flatten(), dim=0).item()
# print(f'onnx golden output 和 python output 余弦相似度：{cos_sim}')


# is_equal = torch.equal(torch.from_numpy(golden_output.flatten()), torch.from_numpy(output).flatten())
# print(f'onnx golden output 和 python output 是否相等：{is_equal}')

# print(input0.flatten())
# print(input1.flatten())
# print(golden_output.flatten())
# print(torch.from_numpy(output).flatten())


'''
3、
'''
input0 = np.array([-4, 7, 5, 4, -7, 8]).astype(np.int16)
input1 = np.array([2, -3, 8, -2, 3, 5]).astype(np.int16)
output = mod(input0, input1, fmod=0)  # [ 0, -2,  5,  0,  2,  3]
print(output)


def np_mod(input0, input1):
    # np.mod(a, b) 等价于  a % b = a - (a // b) * b
    return input0 % input1 

res = []
for i in range(len(input0)):
    res.append(np_mod(input0[i], input1[i]))
print(res)  # [ 0, -2,  5,  0,  2,  3]
