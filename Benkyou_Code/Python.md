# Python

<style>
.center
{
  width: auto;
  display: table;
  margin-left: auto;
  margin-right: auto;
}
</style>

## 基本内容

```python
class cat():
    def __init__(self,age):
        self.age = age
        
    def age_increase(self): # 调用 __init__ 超越函数定义变量 age
        self.age += 1
        print("the age of the cat is "+str(self.age))

def year():
    Ragdoll = cat(3) # 调用 cat 类，传入 age 参数(由 __init__ 超越函数指定变量传输)
    Ragdoll.age_increase() # 调用 cat 类中函数

year()
```

获取当前 python 路径并添加路径

```python
import os

iges_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
iges_path = os.path.join(iges_file_path, 'model/blade_ed.igs')
```

```python
'''
两种解释：
1. 从右乘方式思考，即局部坐标系变换
    A*T 为 A 在坐标系 {A} 下进行了 T 的变换
    T*A 为 T 在坐标系 {T} 下进行了 A 的变换
2. 从左乘方式思考，即全局坐标系变换
    A*T 为 T 在坐标系 {W} 下进行了 A 的变换
    T*A 为 A 在坐标系 {W} 下进行了 T 的变换
'''
```
