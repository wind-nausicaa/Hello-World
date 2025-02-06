# 27. 移除元素
# 简单
# 相关标签
# 相关企业
# 提示
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

# 假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

# 更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
# 返回 k。
# 用户评测：

# 评测机将使用以下代码测试您的解决方案：

# int[] nums = [...]; // 输入数组
# int val = ...; // 要移除的值
# int[] expectedNums = [...]; // 长度正确的预期答案。
#                             // 它以不等于 val 的值排序。

# int k = removeElement(nums, val); // 调用你的实现

# assert k == expectedNums.length;
# sort(nums, 0, k); // 排序 nums 的前 k 个元素
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# 如果所有的断言都通过，你的解决方案将会 通过。

 

# 示例 1：

# 输入：nums = [3,2,2,3], val = 3
# 输出：2, nums = [2,2,_,_]
# 解释：你的函数函数应该返回 k = 2, 并且 nums 中的前两个元素均为 2。
# 你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
# 示例 2：

# 输入：nums = [0,1,2,2,3,0,4,2], val = 2
# 输出：5, nums = [0,1,4,0,3,_,_,_]
# 解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
# 注意这五个元素可以任意顺序返回。
# 你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
 

# 提示：

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        # # 可以直接使用python的剔除函数
        # # 剔除无效值val
        # my_list = list(filter((val).__ne__, nums))
        # n = len(nums)
        # nums[0:n] = my_list
        # return n

        # 方法二
        try:
            while(True):
                nums.remove(val)
        except ValueError:
            pass
        return len(nums)

        # # 最简单的办法，new一个数组，把需要的数字填充进来，判断完了之后再把这个数组赋值给nums的前几位
        # tar = []
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         tar.append(nums[i])
        # n = len(tar)
        # nums[0:n] = tar
        # return n

        # # 如果不想新建一个数组，那么可以在原数组上操作
        # # 对list进行遍历，如果不是目标数字，则填充过去，有个指针指向下一个应当填充的位置；
        # p1 = 0
        # for i in range(len(nums)):
        #     # 如果不是目标数字，则填充到第一个位置，同时指针指向下个位置，并持续做判断；
        #     if nums[i] != val:
        #         nums[p1] = nums[i]
        #         p1 += 1
        #     # i通过for进行增加，从而遍历到下个数字进行判断
        # return p1

        # # 如果想用while循环，那么退出循环的条件就是
        # # i为索引值，目的进行索引
        # i = 0
        # # 指针p1指向需要填充的位置
        # p1 = 0
        # while(True):
        #     if i == len(nums):
        #         break
        #     # 寻找可以填充的数字
        #     if nums[i] != val:
        #         # 假如找到了，那么就填充进去，同时p的位置加1
        #         nums[p1] = nums[i]
        #         p1 += 1
        #     # 循环判断下一个值是不是目标值
        #     i += 1
        # return p1