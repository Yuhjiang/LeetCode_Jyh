"""
每k个结点翻转一次
递归两次
k内部递归一次
k前的节点递归一次
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if self.length(head) < k:
            return head

        temp = head
        for i in range(k):
            temp = temp.next
        # k个结点后翻转的结果
        temp = self.reverseKGroup(temp, k)

        res = self.reverse_list(head, temp, 0, k)

        return res

    def length(self, head):
        res = 0
        while head:
            res += 1
            head = head.next
        return res

    def reverse_list(self, head, last, n, k):
        # 翻转指定k个长度内的链表，last表示原始链表k个结点的next
        if n == k - 1:
            return head

        temp = self.reverse_list(head.next, last, n + 1, k)
        head.next.next = head
        head.next = last

        return temp


def print_list(l):
    res = []
    while l:
        res.append(l.val)
        l = l.next
    print(res)
    return res


if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    s = Solution()
    # l = s.reverse_list(l, ListNode(4), 0, 2)
    l = s.reverseKGroup(l, 3)

    print_list(l)