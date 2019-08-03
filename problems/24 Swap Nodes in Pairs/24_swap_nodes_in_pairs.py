"""
两两调换链表里的点
B.next = swap(B.next)
A.next = B.next
B.next = A
return B
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        temp = head.next
        temp.next = self.swapPairs(temp.next)
        head.next = temp.next
        temp.next = head

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

    s = Solution()
    l = s.swapPairs(l)

    print_list(l)