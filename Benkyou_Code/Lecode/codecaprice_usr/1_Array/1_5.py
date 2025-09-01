'''
209.长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，
并返回其长度。如果不存在符合条件的子数组，返回 0。
思路 1 按顺序累加，判断是否大于指定值(时间复杂度 O(n^2))

例题思路：滑动窗口
'''

'''
# ?? 思考
'''

# 定义类
class Solution(object):
    print('~class~')
    # 定义方法
    def minarray(self, target, nums):
        print('~def~')
        # 初始化参数
        left = 0
        left_right = 0
        right = len(nums) - 1
        min_length = float('inf')
        sum_window = 0
        while left_right <= right:
            sum_window += nums[left_right]

            while sum_window >= target:
                min_length = min(min_length, left_right - left + 1)
                sum_window -= nums[left]
                left += 1

            left_right += 1

        return min_length if min_length != float('inf') else 0

# 定义主函数
if __name__ == '__main__':
    print('~main~')
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    solution = Solution()
    result = solution.minarray(target, nums)

    print(f'result:\n {result}')