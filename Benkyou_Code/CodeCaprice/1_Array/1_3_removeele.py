'''
https://blog.csdn.net/qq_45056135/article/details/132543410
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        for temp in nums:
            if temp != val:
                nums[slow] = temp
                slow += 1
        return slow, nums

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    solution = Solution()
    result, nums_n = solution.removeElement(nums, val)
    print(f"result: {result, nums_n}")