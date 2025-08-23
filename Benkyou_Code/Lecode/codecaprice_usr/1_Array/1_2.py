'''
二分查找
'''

# 定义类
class Solution(object):
    print("~class solution~")
    # 定义方法
    def search(self, nums, target):
        '''
        type
        nums: List[int]
        target: int
        '''
        left = 0
        right = len(nums) - 1 # 定义左右边界
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # idx = 0
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#             elif i != len(nums) - 1:
#                 print
#             elif i == len(nums) - 1:
#                 return -1

# 定义主函数
if __name__=="__main__":
    # print("~main~")
    # 定义有序数组
    nums = [-1, 0, 3, 5, 9, 12] # len() = 6
    len_nums = len(nums)
    correspond_index = [0, 0, 0, 0, 0, 0]
    # target = -1
    # 初始化类
    solution = Solution()
    # result = solution.search(nums, target)
    for i in range(len_nums):
        result = solution.search(nums, nums[i])
        correspond_index[i] = result
    print(f"correspond_index: {correspond_index}")