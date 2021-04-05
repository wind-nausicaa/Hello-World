# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 示例
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 解答一：
class Solution():
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        start = 0
        cur_len = 0
        max_len = 0
        len_s = len(s)
        for i in range(len_s):
            cur_len += 1
            while s[i] in my_set:
                cur_len -= 1
                my_set.remove(s[start])
                start += 1
            my_set.add(s[i])
            max_len = cur_len if cur_len > max_len else max_len
        return max_len
# 时间复杂度：O(n)
# 另一种解法（改用字典，同样有去重的作用）：
class Solution():
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0; max_len = 0; max_start = 0
        my_dict = {}
        for i in range(len(s)):
            if s[i] in my_dict:
                start = max(start, my_dict[s[i]] + 1)
            if max_len < i - start + 1:
                max_len = i - start + 1
                max_start = start
            my_dict[s[i]] = i
        return max_len
        # 返回不重复的最长子串
        # return s[max_start:max_start + max_len]
