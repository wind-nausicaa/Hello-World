# 题目：
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解法一(list两层for循环)：
class Solution():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]
# 时间复杂度：O(n2)
# 解法二（利用dict缩短查找时间）：
class Solution():
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        my_dict={}
        for ind, num in enumerate(nums):
            my_dict[num] = ind
        for ind, num in enumerate(nums):
            j = my_dict.get(target - num)
            if j is not None and j != ind:
                return [ind, j]
# 时间复杂度：O(2n)
# 解法三（边建dict边查找）：
class Solution():
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        my_dict = {}
        for index, num in enumerate(nums):
            j = my_dict.get(target - num)
            if j is not None:
                return [index, j]
            my_dict[num] = index
# 时间复杂度：O(n)
