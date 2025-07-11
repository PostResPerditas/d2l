import random
import torch
from d2l import torch as d2l

def synthetic_data(w, b, num_example):
    '''生成数据集 y=Xw+b+epsilon'''
    X = torch.normal(0, 1, (num_example, len(w)))
    y = X @ w + b
    y += torch.normal(0, 0.001, y.shape)

    return X, y.reshape((-1, 1))

true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = synthetic_data(true_w, true_b, 1000)

# print('features:', features[0],'\nlabel:', labels[0])

# d2l.set_figsize()
# d2l.plt.scatter(features[:, (1)].detach().numpy(), labels.detach().numpy(), 1);
# d2l.plt.show()

###
# 读取数据集
###

def data_iter(batch_size, features, labels):
    '''随机读取数据'''
    num_example = len(features)
    indices = list(range(num_example))
    random.shuffle(indices)
    for i in range(0, num_example, batch_size):
        batch_indices = torch.tensor(indices[i: min(i+batch_size, num_example)])
        yield features[batch_indices], labels[batch_indices] # 暂停生成

batch_size = 10
# for X, y in data_iter(batch_size, features, labels):
#     print(X, '\n', y)
#     break

###
# 初始化模型参数
###

w = torch.normal(0, 0.01, size=(2,1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

def linreg(X, w, b):
    '''定义线性回归'''
    return X @ w + b

def squared_loss(y_hat, y):
    '''定义均方损失'''
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

def sgd(params, lr, batch_size):
    '''定义优化算法'''
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()

lr = 0.03
num_epochs= 3
net = linreg
loss = squared_loss

for epoch in range(num_epochs):
    for X,y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y)
        l.sum().backward() # 以此计算关于 [w, b] 的梯度
        sgd([w, b], lr, batch_size)
    with torch.no_grad():
        train_l = loss(net(features, w, b), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')
