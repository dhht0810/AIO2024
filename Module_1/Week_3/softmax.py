import torch

import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.softmax(x, dim=0)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x - torch.max(x))
        return x_exp / x_exp.sum(dim=0)


data = torch.Tensor([1, 2, 300000000])
softmax = Softmax()
output = softmax(data)
print(output)

data = torch.Tensor([5, 2, 4])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)
