class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        res = temp = ListNode(-1)
        res.next = l = r = head     # 表示k各结点的范围

        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    # 翻转k个结点
                    cur.next, cur, pre = pre, cur.next, cur
                temp.next, temp, l = pre, l, r
            else:
                return res.next


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