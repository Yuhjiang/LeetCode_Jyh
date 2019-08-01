"""
合并k个排好序的链表
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        new_list = ListNode(-1)
        temp = new_list

        all_nodes = []
        for l in lists:
            while l:
                all_nodes.append(l.val)
                l = l.next
        import heapq
        heapq.heapify(all_nodes)
        while all_nodes:
            temp.next = ListNode(heapq.heappop(all_nodes))
            temp = temp.next

        return new_list.next


def print_list(l):
    res = []
    while l:
        res.append(l.val)
        l = l.next
    print(res)
    return res


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)

    s = Solution()
    l4 = s.mergeKLists([l1, l2, l3])

    print_list(l4)
