# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

# 示例 1：

# 输入：nums = [3,2,3]
# 输出：3
# 示例 2：

# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
 

# 提示：
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # 解题思路，单独搞一个计数器来统计每个数字出现的次数，当某个数字出现次数超过n/2时，直接返回
        # 用字典进行统计
        n = {}
        # 以i为指针遍历nums
        for i in range(len(nums)):
            # 如果是没出现过的数字，那么写入字典里，且这个数字的计数+1
            if nums[i] not in n.keys():
                n[nums[i]] = 1
            # 如果这个数字已经出现并且存入字典了，那么出现次数直接+1即可
            else:
                n[nums[i]] += 1
        # 遍历完了，在字典n中找到那个出现最多的数字，然后返回键值
        num_max = max(n, key = lambda k: n[k])
        # 判断出现的次数是大于n/2次的，则返回
        if n[num_max] > len(nums) / 2:
            return num_max
        else:
            return 0