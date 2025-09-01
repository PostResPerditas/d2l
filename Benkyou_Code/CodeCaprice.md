# Code Caprice

## 1 数组

### 1.1 数组理论基础

数组是存放在连续内存空间上的相同类型数据的集合
>数组下标都是从0开始的。
数组内存空间的地址是连续的

### 1.2 二分查找

>给定一个 n 个元素有序的(升序)整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

方式 1

```cpp{.line-numbers}
int left, right; // 初始化左边界和右边界
while (left <= right) {
    int middle = (left + right) / 2; // 指定中间值(int 类型取整)
    if (nums[middle] > target)
        right = middle - 1; // target 在左区间
    else if(nums[middle < target])
        left = middle + 1; // target 在右区间
    else
        return middle;
}
return -1;
```

```python{.line-numbers}
class Solution(object)
    def search(self, nums, target):
        # main

if __name__ == '__main__':
    nums = []; target =  ; # 初始化变量
    solution = Solution() # 初始化类
    result = solution.search(nums, target) # 调用类函数
```
