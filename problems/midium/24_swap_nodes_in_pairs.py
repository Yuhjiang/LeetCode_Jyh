# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        def swap(root):
            if not root or not root.next:
                return root

            ans = root.next
            tmp = ans.next
            ans.next = root
            root.next = swap(tmp)

            return ans

        result = swap(head)
        return result


# 迭代速度更快
class NewSolution:
    def swapPairs(self, head: ListNode) -> ListNode:

        dummy = ListNode(-1)
        prev_node = dummy

        while head and head.next:
            first = head
            second = head.next

            prev_node.next = second
            first.next = second.next
            second.next = first

            prev_node = first
            head = first.next
        prev_node.next = head

        return dummy.next


if __name__ == '__main__':
    from problems.utils import create_list, print_list
    print_list(NewSolution().swapPairs(create_list([1, 2, 3, 4])))
    print_list(NewSolution().swapPairs(create_list([1, 2, 3])))
    print_list(NewSolution().swapPairs(create_list([1])))