# deep_learning_op

# 算子调研指导
建议先查看onnx相关的链接，功能参数介绍比较详细，有些后处理算子没有需要查看别的框架，如果看算子源码建议先看ncnn、darknet，相对简洁一点

1. onnx官方文档

'''

op：

https://onnx.ai/onnx/operators/

op example：

https://github.com/onnx/onnx/blob/main/docs/Operators.md#examples-1

op python code：
https://github.com/onnx/onnx/blob/main/onnx/backend/test/case/node/averagepool.py

'''

2. torch官方文档

https://pytorch.org/docs/stable/generated/torch.nn.GELU.html?highlight=gelu


3. tensorflow官方文档


https://tensorflow.google.cn/api_docs/python/tf/math/argmin



4. darknet

https://github.com/AlexeyAB/darknet/blob/master/src/softmax_layer.c


6. ncnn

https://github.com/BVLC/caffe/blob/master/src/caffe/layers/argmax_layer.cpp



# 算子实现 和 验证正确性

1. 链接

    https://github.com/sunflower-you/deep_learning_op
2. 目录结构

'''

以mish为列，其他op基本一致

    Mish
        - cpp
            Mish.cpp
        - py
            Mish.py
        - test
            mish_torch_python_test.py
            mish_torch_cpp_test.py

整体分两部分:
    
    1. python源码以及测试脚本
        python源码: Mish.py
        golden和python实现比对测试脚本: mish_torch_python_test.py

        测试命令： python mish_torch_python_test.py

    2. cpp源码以及测试脚本
        cpp源码: Mish.cpp
        golden和cpp实现比对测试脚本: mish_torch_cpp_test.py

        测试命令： 
            g++ Mish.cpp -o Mish
            ./Mish
            python mish_torch_cpp_test.py

    3. 正确性验证标准
        1. 余弦相似度
            测试脚本会打印余弦相似度，大于0.9999可认为实现基本没问题
        2. 绝对误差
            golden 和 实现 差值的绝对值小于 0.001 确保实现没问题

'''


https://mip.yht7.com/news/279939
