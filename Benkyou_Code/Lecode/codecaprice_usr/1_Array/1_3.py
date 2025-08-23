'''
移除元素
给你一个数组 nums 和一个值 val ，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。
元素的顺序可以改变，你不需要考虑数组中超出新长度后面的元素。
注意数组在内存空间的地址唯一，且连续
'''

'''
# ?? 思考，生成的新 nums 如何裁剪去末端
'''

# 定于类
class Solution(object):
    print('~class~')
    # 定义方法
    def removeele(self, nums, val):
        print('~def~')
        # 定义快慢指针
        fast = 0
        slow = 0
        len_nums = len(nums)
        while fast < len_nums:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow, nums
# 定义主函数
if __name__ == '__main__':
    print('~main~')
    nums = [3, 2, 2, 3]
    val = 3
    solution = Solution()
    result, nums_new = solution.removeele(nums, val)

    print(f'result, nums:\n {result, nums_new}')