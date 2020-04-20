# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_A, len_B = 0, 0
        temp_A = headA
        temp_B = headB

        # 遍历获取链表长度
        while temp_A or temp_B:
            if temp_A:
                len_A += 1
                temp_A = temp_A.next
            if temp_B:
                len_B += 1
                temp_B = temp_B.next

        temp_A, temp_B = headA, headB
        if len_A > len_B:
            skip = len_A - len_B
            for i in range(skip):
                temp_A = temp_A.next
        else:
            skip = len_B - len_A
            for i in range(skip):
                temp_B = temp_B.next
        while temp_A and temp_B:
            if temp_A == temp_B:
                return temp_A
            temp_A = temp_A.next
            temp_B = temp_B.next

        return None


if __name__ == '__main__':
    a = ListNode(4)
    temp = a
    a_list = [1, 8, 4, 5]
    for i in a_list:
        temp.next = ListNode(i)
        temp = temp.next

    b = ListNode(5)
    temp = b
    b_list = [0, 1, 8, 4, 5]
    for i in b_list:
        temp.next = ListNode(i)
        temp = temp.next

    s = Solution()
    print(s.getIntersectionNode(a, b))