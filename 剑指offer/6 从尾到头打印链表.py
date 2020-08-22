from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        ans = []

        def reverse(root: ListNode):
            if root.next:
                reverse(root.next)
            ans.append(root.val)

        reverse(head)
        return ans


if __name__ == '__main__':
    from problems.utils import create_list, print_list
    print(Solution().reversePrint(create_list([1, 2, 3])))