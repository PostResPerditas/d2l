class Solution(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

if __name__=="__main__":
    val = [1, 2, 3]
    solution = Solution()
    pre = solution

    current = Solution(1)
    pre.next = current
    pre = current
    print
