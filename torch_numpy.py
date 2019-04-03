#coding=utf-8

import torch
import numpy as np
import math

# tensor numpy 数据转化
np_data = np.arange(6).reshape((2,3))
torch_data = torch.from_numpy(np_data)  #copy from np_data
tensor2array = torch_data.numpy()

print(
       '\nnumpy', np_data,
       '\ntorch', torch_data,
       '\ntensor2array', tensor2array,
      )

# torch数据运算
# abs, absolute
data = [-1, -2, 1, 2]
tensor = torch.FloatTensor(data)

print(
    '\nabs',
    '\nnumpy', np.abs(data),
    '\ntorch', torch.abs(tensor),
    )

# sin, Trigonometric functions
print(
    '\nsin',
    '\nnumpy', np.sin(data),
    '\ntorch', torch.sin(tensor),
    )

# mean
print(
    '\nmean',
    '\nnumpy', np.mean(data),
    '\ntorch', torch.mean(tensor),
    )

# matrix multiplication
data = [[-1, -2], [1, 2]]
tensor = torch.FloatTensor(data)
print(
    '\nmatrix multiplication (matmul)',
    '\nnumpy', np.matmul(data,data),
    '\ntorch', torch.mm(tensor,tensor),
    )


