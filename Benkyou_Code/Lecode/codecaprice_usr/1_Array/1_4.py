'''
977.有序数组的平方
给你一个按 非递减顺序 排序的整数数组 nums ，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序
思路 1 先平方再排序
思路 2 先绝对值、排序、再平方

例题思路：左右指针，分别对比左右两边平方值大小
'''

'''
# ?? 思考
'''

# 定义类
class Solution(object):
    print('~class~')
    # 定义方法
    def double_restore(self, nums):
        print('~def~')
        left = 0
        right = len(nums) - 1
        result = [float('inf')] * len(nums) # 需要提前定义列表，存放结果
        index = right
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                result[index] = nums[right] ** 2
                right -= 1
            else:
                result[index] = nums[left] ** 2
                left += 1
            index -= 1
        return result

# 定义主函数
if __name__ == '__main__':
    print('~main~')
    nums = [-4,-1,0,3,10]
    solution = Solution()
    result = solution.double_restore(nums)

    print(f'result, nums:\n {result}')