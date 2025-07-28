import torch
from IPython import display
from d2l import torch as d2l

class Accumulator:  #@save
    """在n个变量上累加"""
    def __init__(self, n):
        self.data = [0.0] * n

    def add(self, *args):
        self.data = [a + float(b) for a, b in zip(self.data, args)]

    def reset(self):
        self.data = [0.0] * len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

class Animator:  #@save
    """在动画中绘制数据"""
    def __init__(self, xlabel=None, ylabel=None, legend=None, xlim=None,
                 ylim=None, xscale='linear', yscale='linear',
                 fmts=('-', 'm--', 'g-.', 'r:'), nrows=1, ncols=1,
                 figsize=(3.5, 2.5)):
        # 增量地绘制多条线
        if legend is None:
            legend = []
        d2l.use_svg_display()
        self.fig, self.axes = d2l.plt.subplots(nrows, ncols, figsize=figsize)
        if nrows * ncols == 1:
            self.axes = [self.axes, ]
        # 使用lambda函数捕获参数
        self.config_axes = lambda: d2l.set_axes(
            self.axes[0], xlabel, ylabel, xlim, ylim, xscale, yscale, legend)
        self.X, self.Y, self.fmts = None, None, fmts
        # d2l.plt.show()

    def add(self, x, y):
        # 向图表中添加多个数据点
        if not hasattr(y, "__len__"):
            y = [y]
        n = len(y)
        if not hasattr(x, "__len__"):
            x = [x] * n
        if not self.X:
            self.X = [[] for _ in range(n)]
        if not self.Y:
            self.Y = [[] for _ in range(n)]
        for i, (a, b) in enumerate(zip(x, y)):
            if a is not None and b is not None:
                self.X[i].append(a)
                self.Y[i].append(b)
        self.axes[0].cla()
        for x, y, fmt in zip(self.X, self.Y, self.fmts):
            self.axes[0].plot(x, y, fmt)
        self.config_axes()
        display.display(self.fig)
        display.clear_output(wait=True)

class Trainer:
    def __init__(
            self,
            num_inputs=784,
            num_outputs=10,
            lr:float=0.1, # 学习率
            num_epochs:int=10, # 迭代次数
            train_iter=None,
            test_iter=None
        ):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.lr = lr
        self.num_epochs = num_epochs
        self.train_iter = train_iter
        self.test_iter = test_iter
        self.W = torch.normal(0, 0.01, size=(self.num_inputs, self.num_outputs), requires_grad=True)
        self.b = torch.zeros(self.num_outputs, requires_grad=True)
        pass
    
    def _softmax(self, X):
        '''输出层softmax'''
        X_exp = torch.exp(X)
        partition = X_exp.sum(1, keepdim=True)
        return X_exp / partition  # 这里应用了广播机制
    
    def _net(self, X):
        '''模型'''
        return self._softmax(torch.matmul(X.reshape((-1, self.W.shape[0])), self.W) + self.b)

    def _loss(self, y_hat, y):
        '''cross_entropy'''
        return - torch.log(y_hat[range(len(y_hat)), y])

    def _accuracy(self, y_hat, y):  #@save
        """计算预测正确的数量(单批精度)"""
        if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
            y_hat = y_hat.argmax(axis=1)
        cmp = y_hat.type(y.dtype) == y
        return float(cmp.type(y.dtype).sum())

    def _evaluate_accuracy(self, data_iter):  #@save
        """计算在指定数据集上模型的精度"""
        metric = Accumulator(2)  # 正确预测数、预测总数
        with torch.no_grad():
            for X, y in data_iter:
                metric.add(self._accuracy(self._net(X), y), y.numel())
        return metric[0] / metric[1]
    
    def _updater(self, batch_size):
        '''优化器'''
        return d2l.sgd([self.W, self.b], self.lr, batch_size)

    def _epoch(self, data_iter):  #@save
        """单个训练周期: 训练模型一个迭代周期（定义见第3章）"""
        # 训练损失总和、训练准确度总和、样本数
        metric = Accumulator(3)
        for X, y in data_iter:
            y_hat = self._net(X)
            l = self._loss(y_hat, y)
            # 定制的优化器和损失函数
            l.sum().backward()
            # 更新参数    
            self._updater(X.shape[0])
            # 累加器累加损失、准确度和样本数
            metric.add(float(l.sum()), self._accuracy(y_hat, y), y.numel())
        # 返回训练损失和训练精度
        return metric[0] / metric[2], metric[1] / metric[2]
    
    def epochs(self, train_iter, test_iter, num_epochs):  #@save
        """训练模型（定义见第3章）"""
        animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0.3, 0.9],
                            legend=['train loss', 'train acc', 'test acc'], figsize=(7, 5))
        for epoch in range(num_epochs):
            train_metrics = self._epoch(train_iter)
            test_acc = self._evaluate_accuracy(test_iter)
            animator.add(epoch + 1, train_metrics + (test_acc,))
        train_loss, train_acc = train_metrics
        assert train_loss < 0.5, train_loss
        assert train_acc <= 1 and train_acc > 0.7, train_acc
        assert test_acc <= 1 and test_acc > 0.7, test_acc

    def run(self):
        '''训练'''
        self.epochs(self.train_iter, self.test_iter, self.num_epochs)

    def predict(self, data_iter, n=6):
        """预测标签（定义见第3章）"""
        for X, y in data_iter:
            break
        trues = d2l.get_fashion_mnist_labels(y)
        preds = d2l.get_fashion_mnist_labels(self._net(X).argmax(axis=1))
        titles = [true +'\n' + pred for true, pred in zip(trues, preds)]
        d2l.show_images(
            X[0:n].reshape((n, 28, 28)), 1, n, titles=titles[0:n])

# 训练
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size=256)
trainer = Trainer(train_iter=train_iter, test_iter=test_iter)
trainer.run()

# 预测
# trainer.predict(test_iter, 10)