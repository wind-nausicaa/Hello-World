# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
# 这里采用大佬的解法：
class Solution():
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(l1.val + l2.val)
        cur = head
        ascii = 10
        while l1.next or l2.next:
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            cur.next = ListNode(l1.val + l2.val + cur.val // ascii)
            cur.val = cur.val % ascii
            cur = cur.next
        if cur.val >= ascii:
            cur.next = ListNode(cur.val // ascii)
            cur.val = cur.val % ascii
        return head
