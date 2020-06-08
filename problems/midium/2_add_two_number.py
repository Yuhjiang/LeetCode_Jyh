# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        result = ListNode(-1)
        temp = result
        while l1 and l2:
            flag, t = divmod(l1.val + l2.val + flag, 10)
            temp.next = ListNode(t)
            l1 = l1.next
            l2 = l2.next
            temp = temp.next
        if l1:
            while l1:
                flag, t = divmod(l1.val + flag, 10)
                temp.next = ListNode(t)
                temp = temp.next
                l1 = l1.next
        elif l2:
            while l2:
                flag, t = divmod(l2.val + flag, 10)
                temp.next = ListNode(t)
                temp = temp.next
                l2 = l2.next
        if flag:
            temp.next = ListNode(flag)
        return result.next


if __name__ == '__main__':
    from utils import print_list, create_list
    l1 = create_list([1])
    l2 = create_list([9])
    print_list(Solution().addTwoNumbers(l1, l2))