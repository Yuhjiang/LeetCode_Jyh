# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.merge_sort(head)

    def merge_sort(self, root: ListNode):
        if not root or not root.next:
            return root

        slow, fast = root, root.next
        if fast.next:
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid, slow.next = slow.next, None

        left, right = self.merge_sort(root), self.merge_sort(mid)

        new_root = ListNode(0)
        tmp = new_root
        while left and right:
            if left.val < right.val:
                tmp.next = left
                left = left.next
            else:
                tmp.next = right
                right = right.next
            tmp = tmp.next
        if left:
            tmp.next = left
        else:
            tmp.next = right
        return new_root.next


class NewSolution:
    def sortList(self, head: ListNode) -> ListNode:
        tmp = head
        length = 0
        while tmp:
            length += 1
            tmp = tmp.next

        interval = 1
        new_head = ListNode(0)
        new_head.next = head
        while interval <= length:
            tmp, h = new_head, new_head.next
            while h:
                tmp_h1, pos = h, interval    # 每个分组的初始值
                while h and pos:
                    h = h.next
                    pos -= 1
                if pos:
                    # 这个interval之后没有node
                    break
                tmp_h2, pos = h, interval
                while h and pos:
                    h = h.next
                    pos -= 1
                left, right = interval, interval - pos
                while left and right:
                    if tmp_h1.val < tmp_h2.val:
                        tmp.next = tmp_h1
                        tmp_h1 = tmp_h1.next
                        left -= 1
                    else:
                        tmp.next = tmp_h2
                        tmp_h2 = tmp_h2.next
                        right -= 1
                    tmp = tmp.next
                tmp.next = tmp_h1 if left else tmp_h2
                while left > 0 or right > 0:
                    tmp = tmp.next
                    left -= 1
                    right -= 1
                tmp.next = h
            interval *= 2
        return new_head.next


if __name__ == '__main__':
    from utils import create_list, print_list
    # print_list(NewSolution().sortList(create_list([-1, 5, 3, 4, 0])))
    print_list(NewSolution().sortList(create_list([4,2,1,3])))