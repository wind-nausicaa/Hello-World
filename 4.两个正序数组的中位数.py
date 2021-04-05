# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 示例 1：

# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2

# 示例 2：

# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

# 示例 3：

# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 方法一：组合两个数组，调用sort函数排序后输出
class Solution():
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = nums1 + nums2
        ans.sort()
        if len(ans) % 2 == 0:
            return float((ans[int(len(ans) / 2) - 1] + ans[int(len(ans) / 2)]) / 2)
        else:
            return float(ans[int(len(ans) / 2)])
"""
拓展sort()方法和sorted()方法：https://zhuanlan.zhihu.com/p/106009216
sort()方法为list类型自建方法，不能用于其他数据类型，直接改变原list，用法：list.sort()
sorted()可用于任意可迭代对象，包括字符串，用法：sorted(str)，返回一个list类型，sorted(type, key = None, reverse = False)
"""