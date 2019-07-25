"""
移除链表里倒数第n个结点
设置两个结点，一个先走n步，然后两者同时走，
最后先走的节点走到头了，后出发的正好在倒数第n个位置
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp1 = temp2 = head

        for _ in range(n):
            temp1 = temp1.next
        if temp1 is None:
            return temp2.next

        while temp1.next:
            temp1 = temp1.next
            temp2 = temp2.next

        temp2.next = temp2.next.next

        return head
