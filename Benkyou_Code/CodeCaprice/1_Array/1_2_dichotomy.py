"""
题目: 704. 二分查找
链接: https://leetcode.cn/problems/binary-search/description/
思路:
mid = left + right
方法1: 初始化 right = len(nums)-1, [left, right] left <= right 左闭右闭 那么right = mid-1, 因为 [mid, right] 已经考虑了 所以剩余[left, mid-1] mid
方法2: 初始化 right = len(nums)-1, [left, right) left < right 左闭右开 那么right = mid, 因为 [mid, right) 已经考虑了 所以剩余[left, mid) 这里就考虑mid了
两个方法的剩余考虑区间保持一致
left统一写法 left = mid +1
关键词: 有序，目标值， 查找，数组元组不重复
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                # right = mid -1
                right = right -1
            elif target > nums[mid]:
                # left = left + 1
                left = mid + 1
            else:
                return mid
        return -1
if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 5
    solution = Solution()
    result = solution.search(nums, target)

    print(f"result: {result}")
