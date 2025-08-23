#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
	int search(vector<int>& nums, int target){
		int left = 0;
		int right = nums.size() - 1;// 定义target在左闭右闭的区间里，[left, right]
		while (left <= right)// 当left==right，区间[left, right]依然有效，所以用 <=
		{
			int middle = left + ((right - left) / 2);// 防止溢出 等同于(left + right)/2
			if (nums[middle] > target)// target 在左区间，所以[left, middle - 1]
				right = middle - 1;
			else if (nums[middle] < target)// target 在右区间，所以[middle + 1, right]
				left = middle + 1;
			else
				return middle;// 数组中找到目标值，直接返回下标
		}
        // 未找到
		return -1;
	}
};

int main(){
	vector<int> nums = { -1, 0, 3, 5, 9, 12 }; // 创建一个数组
	int target = 9;
	
	Solution obj;// 创建一个Solution类型的对象obj，
	
    int result;
	//通过obj对象调用search函数，并传入参数nums、target
	result = obj.search(nums, target);

    // 输出结果
	if (result == -1)
		cout << "没有查找到target, 输出为: " << result << endl;
	else
		cout << "查找到target, 输出为: " << result << endl;
    return 0;
}
