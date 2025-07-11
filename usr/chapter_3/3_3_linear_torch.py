import numpy as np
import torch
from torch.utils import data
from d2l import torch as d2l

# 生成数据集
def synthetic_data(w, b, num_example):
    '''生成数据集 y=Xw+b+epsilon'''
    X = torch.normal(0, 1, (num_example, len(w)))
    y = X @ w + b
    y += torch.normal(0, 0.001, y.shape)

    return X, y.reshape((-1, 1))

true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = synthetic_data(true_w, true_b, 1000)

def load_array(data_arrays, batch_size, is_train=True):  #@save
    """构造一个PyTorch数据迭代器"""
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)

batch_size = 10
data_iter = load_array((features, labels), batch_size)

# print(next(iter(data_iter)))

# 定义模型
from torch import nn

net = nn.Sequential(nn.Linear(2, 1))
net[0].weight.data.normal_(0, 0.01)
print(net[0].bias.data.fill_(0))

# 定义损失函数
loss = nn.MSELoss()

# 定义优化算法
trainer = torch.optim.SGD(net.parameters(), lr=0.03)

# 训练
num_epochs = 3
for epoch in range(num_epochs):
    for X, y in data_iter:
        l = loss(net(X), y)
        trainer.zero_grad()
        l.backward()
        trainer.step()
    l = loss(net(features), labels)
    print(f'epoch {epoch + 1}, loss {l:f}')

w = net[0].weight.data
print('w 的估计误差:', true_w - w.reshape(true_w.shape))
b = net[0].bias.data
print('b 的估计误差:', true_b - b)