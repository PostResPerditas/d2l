'''
59.螺旋矩阵II
给定一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:
输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]
'''

'''
# ?? 思考
'''

# 定义类
class Solution():
    print('~class~')
    # 定义方法
    def generatematrix(self, num):
        print('~def~')
        top, down, left, right = 0, num-1, 0, num-1
        number = 1
        result = [[0] * num for _ in range(num)]
        while number <= num ** 2:
            for i in range(left, right + 1):
                result[top][i] = number
                number += 1
            top += 1
            for i in range(top, down + 1):
                result[i][right] = number
                number += 1
            right -= 1
            for i in range(right, left - 1, -1):
                result[down][i] = number
                number += 1
            down -= 1
            for i in range(down, top - 1, -1):
                result[i][left] = number
                number += 1
            left += 1
        return result

# 定义主函数
if __name__ == '__main__':
    print('~main~')
    num = 3
    solution = Solution()
    result = solution.generatematrix(num)

    print(f'result, nums:\n {result}')