from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        t = lists[0]

        for i in range(1, len(lists)):
            t = self.merge_town_lists(t, lists[i])
        return t

    def merge_town_lists(self, l1: ListNode, l2: ListNode):
        if not (l1 and l2):
            return l1 if l1 else l2
        t = ListNode(-1)
        temp = t
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 if l1 else l2

        return t.next


class NewSolution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        left, right = 0, len(lists) - 1
        return self.merge(lists, left, right)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        elif left > right:
            return None
        mid = (left + right) // 2
        return self.merge_town_lists(self.merge(lists, left, mid), self.merge(lists, mid+1, right))

    def merge_town_lists(self, l1: ListNode, l2: ListNode):
        if not (l1 and l2):
            return l1 if l1 else l2
        t = ListNode(-1)
        temp = t
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 if l1 else l2

        return t.next



import heapq


class QueueSolution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []
        for i in lists:
            heapq.heappush(q, [i.val, i])

        t = ListNode(-1)
        temp = t
        while q:
            p = heapq.heappop(q)[1]
            temp.next = p
            if p.next:
                heapq.heappush(q, [p.next.val, p.next])
            temp = temp.next
        return t.next


if __name__ == '__main__':
    from utils import create_list, print_list
    # listss = [
    #     create_list([1, 4, 5]),
    #     create_list([1, 3, 4]),
    #     create_list([2, 6])
    # ]
    listss = [
        create_list([0]),
        create_list([1,2, 3])
    ]
    print_list(QueueSolution().mergeKLists(listss))
