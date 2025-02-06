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
"""
拓展sort()方法和sorted()方法：https://zhuanlan.zhihu.com/p/106009216
sort()方法为list类型自建方法，不能用于其他数据类型，直接改变原list，用法：list.sort()
sorted()可用于任意可迭代对象，包括字符串，用法：sorted(str)，返回一个list类型，sorted(type, key = None, reverse = False)
"""
class Solution():
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        ans = nums1 + nums2
        ans.sort()
        if len(ans) % 2 == 0:
            return float((ans[int(len(ans) / 2) - 1] + ans[int(len(ans) / 2)]) / 2)
        else:
            return float(ans[int(len(ans) / 2)])
        
# 方法二：时间复杂度为O(log(m+n))
class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        def findKthInTwoArrays(start1, start2, k):
            # 处理边界问题：
            # case1：当nums1或nums2为空时：
            if start1 >= len(nums1):
                return nums2[start2 + k - 1]
            if start2 >= len(nums2):
                return nums1[start1 + k - 1]
            # case2：当索引的值超过某一数组的长度时，则处理另一数组：
            if start1 + k // 2 > len(nums1):
                # 将nums1用于对比的值nums1_c设置为比nums2_c大1
                nums2_c = nums2[start2 + k // 2 - 1]
                nums1_c = nums2_c + 1
            elif start2 + k // 2 > len(nums2):
                # 将nums2用于对比的值nums2_c设置为比nums1_c大1
                nums1_c = nums1[start1 + k // 2 - 1]
                nums2_c = nums1_c + 1
            else:
                nums1_c = nums1[start1 + k // 2 - 1]; nums2_c = nums2[start2 + k // 2 - 1]
            # case3：当k为1时，直接将两数组中当前索引的值进行对比，输出最小的那个
            if k == 1:
                return nums1[start1] if nums1[start1] < nums2[start2] else nums2[start2]
            # case4：二分法寻找第k个数，分别在两个数组中寻找第k//2个数，如果nums1[k//2] < nums2[k//2]那么说明要找的第k个数肯定不在nums1的前k//2个数中，则舍去这些数，具体方法为左指针往右移k//2个数

            if nums1_c < nums2_c:
                start1 = start1 + k // 2
            else:
                start2 = start2 + k // 2
            return findKthInTwoArrays(start1, start2, k - k // 2)
        # 统一将两数组的中位数记为nums1和nums2组成数组的第(len_1 + len_2 + 1) // 2位和第(len_1 + len_2 + 2) // 2位的平均值
        len_1 = len(nums1); len_2 = len(nums2); left = (len_1 + len_2 + 1) // 2; right = (len_1 + len_2 + 2) // 2
        return float((findKthInTwoArrays(0, 0, left) + findKthInTwoArrays(0, 0, right)) / 2)

if __name__ == "__main__":
    a = [1, 2]
    b = [3, 4]
    my_solution = Solution()
    d = my_solution.findMedianSortedArrays(a, b)
    print(d)