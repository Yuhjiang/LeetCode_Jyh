"""
两个用链表逆向排序的数据相加
1. 从头开始加，碰到进位的情况，在下一个节点加1
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = []
        temp = self

        while temp:
            s.append(str(temp.val))
            temp = temp.next

        return ' -> '.join(s)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        new_list = ListNode('Head')
        temp = new_list

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            carry, val = divmod(carry, 10)

            temp.next = ListNode(val)
            temp = temp.next

        return new_list.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(9)

    s = Solution()
    t = s.addTwoNumbers(l1, l2)
    print(t)